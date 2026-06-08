"""
EssayView — Màn hình làm bài tự luận (v3).

Luồng mỗi câu:
  1. Hiển thị câu hỏi
  2. User nhập câu trả lời vào TextArea
  3. Bấm "Nộp bài & Chấm" → gọi grader trong thread riêng (không block UI)
  4. Hiện kết quả: grade, điểm, nhận xét LLM, đáp án mẫu, giải thích
  5. Bấm "Câu tiếp theo" → lặp lại
  6. Sau câu cuối → on_finish(grades)
"""

import threading
import customtkinter as ctk
from typing import Callable, List, Optional

from core.models import Question, GraderConfig, EssayGradeResult, GradeLevel
from core.quiz_engine import QuizSession
from . import theme as T
from .widgets import AppButton, Card, SectionLabel, BodyLabel, Divider, ProgressBar


_GRADE_META = {
    GradeLevel.EXCELLENT: ("🟢  XUẤT SẮC",  T.TEXT_SUCCESS,  T.BTN_CHOICE_CORRECT,  T.BTN_CHOICE_CORRECT_BORDER),
    GradeLevel.GOOD:      ("🔵  TỐT",        "#4ec3ca",       "#1a3040",              "#4ec3ca"),
    GradeLevel.PARTIAL:   ("🟡  MỘT PHẦN",  T.TEXT_WARNING,  "#302010",              T.TEXT_WARNING),
    GradeLevel.INCORRECT: ("🔴  CHƯA ĐẠT",  T.TEXT_ERROR,   T.BTN_CHOICE_WRONG,     T.BTN_CHOICE_WRONG_BORDER),
}


class EssayView(ctk.CTkFrame):
    """
    Frame làm bài tự luận.
    on_finish(grades: list[EssayGradeResult]) được gọi khi xong tất cả câu.
    on_back() được gọi khi user thoát.
    """

    def __init__(
        self,
        master,
        session: QuizSession,
        grader_config: GraderConfig,
        on_finish: Callable[[List[EssayGradeResult]], None],
        on_back: Callable,
    ):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._session = session
        self._grader_config = grader_config
        self._on_finish = on_finish
        self._on_back = on_back

        self._total = len(session.questions)
        self._current_q: Optional[Question] = None
        self._grades: List[EssayGradeResult] = []
        self._grading = False  # đang chờ LLM không

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_topbar()
        self._build_body()
        self._build_bottombar()
        self._load_current_question()

    # ── Build UI ─────────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=56)
        bar.grid(row=0, column=0, sticky="ew")
        bar.columnconfigure(1, weight=1)

        AppButton(
            bar, text="← Thoát", command=self._confirm_back,
            style="neutral", width=90, height=T.BTN_HEIGHT_SM,
        ).grid(row=0, column=0, padx=12, pady=10)

        self._progress_label = ctk.CTkLabel(
            bar, text="", font=T.FONT_BODY_BOLD, text_color=T.TEXT_PRIMARY
        )
        self._progress_label.grid(row=0, column=1, pady=10)

        # Badge chế độ
        ctk.CTkLabel(
            bar,
            text="  TỰ LUẬN + AI CHẤM  ",
            font=T.FONT_SMALL_BOLD,
            text_color=T.TEXT_WARNING,
            fg_color=T.BG_CARD,
            corner_radius=4,
        ).grid(row=0, column=2, padx=12, pady=10)

    def _build_body(self):
        self._scroll = ctk.CTkScrollableFrame(
            self, fg_color=T.BG_PRIMARY, corner_radius=0,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._scroll.grid(row=1, column=0, sticky="nsew")
        self._scroll.columnconfigure(0, weight=1)

    def _build_bottombar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=64)
        bar.grid(row=2, column=0, sticky="ew")
        bar.columnconfigure(0, weight=1)

        self._progress_bar = ProgressBar(bar)
        self._progress_bar.grid(row=0, column=0, columnspan=3, sticky="ew")
        self._progress_bar.set(0)

        btn_frame = ctk.CTkFrame(bar, fg_color="transparent")
        btn_frame.grid(row=1, column=0, columnspan=3, pady=(8, 8))

        self._submit_btn = AppButton(
            btn_frame, text="📤  Nộp bài & Chấm",
            command=self._submit_answer,
            style="primary", width=180, height=T.BTN_HEIGHT_SM,
        )
        self._submit_btn.grid(row=0, column=0, padx=8)

        self._next_btn = AppButton(
            btn_frame, text="Câu tiếp theo →",
            command=self._next_question,
            style="secondary", width=160, height=T.BTN_HEIGHT_SM,
        )
        self._next_btn.grid(row=0, column=1, padx=8)
        self._next_btn.grid_remove()

    # ── Render câu hỏi ───────────────────────────────────────────────────────

    def _clear_body(self):
        for w in self._scroll.winfo_children():
            w.destroy()
        self._grading = False
        self._submit_btn.configure(state="normal", text="📤  Nộp bài & Chấm")
        self._next_btn.grid_remove()

    def _load_current_question(self):
        self._clear_body()
        q = self._session.get_next_question()
        if q is None:
            self._finish()
            return

        self._current_q = q
        idx = self._session.current_index + 1

        self._progress_label.configure(text=f"Câu {idx} / {self._total}")
        self._progress_bar.set((idx - 1) / self._total)

        outer = ctk.CTkFrame(self._scroll, fg_color="transparent")
        outer.grid(row=0, column=0, sticky="nsew", padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        outer.columnconfigure(0, weight=1)

        # Câu hỏi card
        q_card = Card(outer, color=T.BG_SECONDARY)
        q_card.grid(row=0, column=0, sticky="ew", pady=(0, 16))
        q_card.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            q_card, text=q.content,
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
            wraplength=700, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        # Label hướng dẫn
        ctk.CTkLabel(
            outer,
            text="✏️  Nhập câu trả lời của bạn bên dưới:",
            font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
        ).grid(row=1, column=0, sticky="w", pady=(0, 6))

        # TextArea nhập bài
        self._answer_box = ctk.CTkTextbox(
            outer,
            height=180,
            font=T.FONT_BODY,
            fg_color=T.BG_SECONDARY,
            text_color=T.TEXT_PRIMARY,
            border_color=T.BORDER_DEFAULT,
            border_width=1,
            corner_radius=8,
            wrap="word",
        )
        self._answer_box.grid(row=2, column=0, sticky="ew", pady=(0, 8))
        self._answer_box.focus()

        # Vùng kết quả (lấp đầy sau khi chấm)
        self._result_frame = ctk.CTkFrame(outer, fg_color="transparent")
        self._result_frame.grid(row=3, column=0, sticky="ew")
        self._result_frame.columnconfigure(0, weight=1)

    # ── Logic chấm ───────────────────────────────────────────────────────────

    def _submit_answer(self):
        if self._grading:
            return

        user_text = self._answer_box.get("0.0", "end").strip()
        if not user_text:
            self._show_inline_warning("Vui lòng nhập câu trả lời trước khi nộp.")
            return

        self._grading = True
        self._answer_box.configure(state="disabled")
        self._submit_btn.configure(state="disabled", text="⏳  Đang chấm...")

        # Gọi grader trong thread riêng để không block UI
        def _grade_thread():
            from core.grader import grade_essay
            result = grade_essay(self._current_q, user_text, self._grader_config)
            # Cập nhật UI phải chạy trên main thread
            self.after(0, lambda: self._on_grade_done(result))

        threading.Thread(target=_grade_thread, daemon=True).start()

    def _on_grade_done(self, grade_result: EssayGradeResult):
        """Callback trên main thread sau khi LLM trả kết quả."""
        self._grading = False
        self._grades.append(grade_result)

        # Submit engine (không cần chấm, chỉ để tịnh tiến index)
        self._session.submit_answer(grade_result.user_answer)

        self._submit_btn.configure(state="disabled", text="✓  Đã nộp")
        self._render_grade_result(grade_result)

        # Hiện nút next
        is_last = self._session.current_index >= self._total
        self._next_btn.configure(
            text="🏁  Xem kết quả" if is_last else "Câu tiếp theo →"
        )
        self._next_btn.grid()

        # Scroll xuống để thấy kết quả
        self.after(100, lambda: self._scroll._parent_canvas.yview_moveto(1.0))

    def _render_grade_result(self, g: EssayGradeResult):
        """Render kết quả chấm vào result_frame."""
        container = self._result_frame
        container.columnconfigure(0, weight=1)

        Divider(container).grid(row=0, column=0, sticky="ew", pady=(8, 12))

        if g.error:
            # Lỗi API
            err_card = Card(container, color="#2a1a1a")
            err_card.grid(row=1, column=0, sticky="ew", pady=(0, 12))
            err_card.columnconfigure(0, weight=1)
            ctk.CTkLabel(
                err_card,
                text=f"⚠  {g.error}",
                font=T.FONT_BODY, text_color=T.TEXT_WARNING,
                wraplength=680, justify="left",
            ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")
            current_row = 2
        else:
            # Grade badge
            label, text_color, bg_color, border_color = _GRADE_META.get(
                g.grade, ("⚪ KHÔNG RÕ", T.TEXT_SECONDARY, T.BG_CARD, T.BORDER_DEFAULT)
            )

            grade_card = ctk.CTkFrame(
                container, fg_color=bg_color, corner_radius=T.CORNER_RADIUS,
                border_width=1, border_color=border_color,
            )
            grade_card.grid(row=1, column=0, sticky="ew", pady=(0, 12))
            grade_card.columnconfigure(0, weight=1)
            grade_card.columnconfigure(1, weight=0)

            ctk.CTkLabel(
                grade_card, text=label,
                font=T.FONT_HEADING, text_color=text_color,
            ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="w")

            ctk.CTkLabel(
                grade_card,
                text=f"  {g.score_pct}/100  ",
                font=(T.FONT_FAMILY, 20, "bold"), text_color=text_color,
                fg_color=T.BG_PRIMARY, corner_radius=6,
            ).grid(row=0, column=1, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="e")

            # Nhận xét LLM
            if g.feedback:
                ctk.CTkLabel(
                    container,
                    text="💬  Nhận xét của AI:",
                    font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
                ).grid(row=2, column=0, sticky="w", pady=(0, 4))

                ctk.CTkLabel(
                    container,
                    text=g.feedback,
                    font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
                    wraplength=700, justify="left", anchor="nw",
                ).grid(row=3, column=0, sticky="ew", pady=(0, 12))

            current_row = 4

        # Đáp án mẫu
        ctk.CTkLabel(
            container,
            text="📖  Đáp án mẫu:",
            font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
        ).grid(row=current_row, column=0, sticky="w", pady=(0, 4))

        ans_card = ctk.CTkFrame(
            container, fg_color=T.BG_CARD, corner_radius=8,
            border_width=1, border_color=T.BORDER_SUCCESS,
        )
        ans_card.grid(row=current_row + 1, column=0, sticky="ew", pady=(0, 12))
        ans_card.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            ans_card,
            text=str(g.reference_answer),
            font=T.FONT_BODY, text_color=T.TEXT_SUCCESS,
            wraplength=680, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        # Giải thích gốc từ testbank
        if g.explanation:
            ctk.CTkLabel(
                container,
                text="📝  Giải thích:",
                font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
            ).grid(row=current_row + 2, column=0, sticky="w", pady=(0, 4))

            ctk.CTkLabel(
                container,
                text=g.explanation,
                font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
                wraplength=700, justify="left", anchor="nw",
            ).grid(row=current_row + 3, column=0, sticky="ew", pady=(0, 12))

    def _show_inline_warning(self, msg: str):
        """Hiện cảnh báo nhỏ gần nút submit."""
        warn = ctk.CTkLabel(
            self._result_frame,
            text=f"⚠  {msg}",
            font=T.FONT_SMALL, text_color=T.TEXT_WARNING,
        )
        warn.grid(row=99, column=0, sticky="w", pady=4)
        self.after(3000, warn.destroy)

    # ── Điều hướng ───────────────────────────────────────────────────────────

    def _next_question(self):
        if self._session.current_index >= self._total:
            self._finish()
        else:
            self._load_current_question()

    def _finish(self):
        self._progress_bar.set(1.0)
        self._on_finish(self._grades)

    def _confirm_back(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Xác nhận thoát")
        dialog.geometry("340x160")
        dialog.resizable(False, False)
        dialog.configure(fg_color=T.BG_SECONDARY)
        dialog.grab_set()
        dialog.focus()

        ctk.CTkLabel(
            dialog,
            text="Bạn chắc chắn muốn thoát?\nTiến độ hiện tại sẽ không được lưu.",
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY, justify="center",
        ).pack(pady=(24, 16))

        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack()

        AppButton(
            btn_frame, text="Tiếp tục làm", command=dialog.destroy,
            style="secondary", width=130, height=T.BTN_HEIGHT_SM,
        ).grid(row=0, column=0, padx=8)

        AppButton(
            btn_frame, text="Thoát",
            command=lambda: (dialog.destroy(), self._on_back()),
            style="danger", width=130, height=T.BTN_HEIGHT_SM,
        ).grid(row=0, column=1, padx=8)
