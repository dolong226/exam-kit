"""
QuizView — Màn hình làm bài.
Xử lý cả 2 chế độ: Multiple Choice và Essay.

Fixes so với bản cũ:
- _show_mc_feedback: không còn destroy frame → dùng clear children đúng cách
- _reveal_essay_answer: fix điều kiện text nút "Xem kết quả" câu cuối
- Essay mode: luôn submit sau khi xem đáp án để engine tịnh tiến index đúng
"""

import customtkinter as ctk
from typing import Callable, List, Optional

from core.models import Question, QuizMode, UserResponse
from core.quiz_engine import QuizSession
from . import theme as T
from .widgets import (
    AppButton, Card, SectionLabel, BodyLabel,
    ProgressBar, ScoreChip, ExplanationBox, ChoiceButton, Divider,
)

CHOICE_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H"]


class QuizView(ctk.CTkFrame):
    def __init__(
        self,
        master,
        session: QuizSession,
        on_finish: Callable[[QuizSession], None],
        on_back: Callable,
    ):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._session = session
        self._on_finish = on_finish
        self._on_back = on_back

        self._total = len(session.questions)
        self._current_q: Optional[Question] = None
        self._answered = False
        self._answer_revealed = False
        self._correct_so_far = 0
        self._choice_buttons: List[ChoiceButton] = []
        self._feedback_frame: Optional[ctk.CTkFrame] = None
        self._essay_answer_frame: Optional[ctk.CTkFrame] = None

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
            bar, text="", font=T.FONT_BODY_BOLD, text_color=T.TEXT_PRIMARY,
        )
        self._progress_label.grid(row=0, column=1, pady=10)

        self._score_chip = ScoreChip(bar, "0/0")
        self._score_chip.grid(row=0, column=2, padx=12, pady=10)

    def _build_body(self):
        self._body = ctk.CTkScrollableFrame(
            self, fg_color=T.BG_PRIMARY, corner_radius=0,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._body.grid(row=1, column=0, sticky="nsew")
        self._body.columnconfigure(0, weight=1)

    def _build_bottombar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=64)
        bar.grid(row=2, column=0, sticky="ew")
        bar.columnconfigure(0, weight=1)

        self._progress_bar = ProgressBar(bar)
        self._progress_bar.grid(row=0, column=0, columnspan=3, sticky="ew", padx=0, pady=(0, 0))
        self._progress_bar.set(0)

        btn_frame = ctk.CTkFrame(bar, fg_color="transparent")
        btn_frame.grid(row=1, column=0, columnspan=3, pady=(8, 8))

        self._reveal_btn = AppButton(
            btn_frame, text="👁  Xem đáp án",
            command=self._reveal_essay_answer,
            style="secondary", width=160, height=T.BTN_HEIGHT_SM,
        )
        self._reveal_btn.grid(row=0, column=0, padx=8)

        self._next_btn = AppButton(
            btn_frame, text="Tiếp theo →",
            command=self._next_question,
            style="primary", width=160, height=T.BTN_HEIGHT_SM,
        )
        self._next_btn.grid(row=0, column=1, padx=8)

        self._reveal_btn.grid_remove()
        self._next_btn.grid_remove()

    # ── Render câu hỏi ───────────────────────────────────────────────────────

    def _clear_body(self):
        for widget in self._body.winfo_children():
            widget.destroy()
        self._choice_buttons = []
        self._feedback_frame = None
        self._essay_answer_frame = None
        self._answered = False
        self._answer_revealed = False
        self._reveal_btn.grid_remove()
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
        self._score_chip.update_score(self._correct_so_far, self._session.current_index)
        self._progress_bar.set(self._session.current_index / self._total)

        if q.type == QuizMode.MULTIPLE_CHOICE:
            self._render_mc_question(q)
        else:
            self._render_essay_question(q)

    def _render_mc_question(self, q: Question):
        outer = ctk.CTkFrame(self._body, fg_color="transparent")
        outer.grid(row=0, column=0, sticky="nsew", padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        outer.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            outer, text="  TRẮC NGHIỆM  ",
            font=T.FONT_SMALL_BOLD, text_color=T.BTN_PRIMARY,
            fg_color=T.BG_CARD, corner_radius=4,
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        q_card = Card(outer, color=T.BG_SECONDARY)
        q_card.grid(row=1, column=0, sticky="ew", pady=(0, 16))
        q_card.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            q_card, text=q.content,
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
            wraplength=700, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        choices_frame = ctk.CTkFrame(outer, fg_color="transparent")
        choices_frame.grid(row=2, column=0, sticky="ew")
        choices_frame.columnconfigure(0, weight=1)

        for i, choice_text in enumerate(q.choices or []):
            letter = CHOICE_LETTERS[i] if i < len(CHOICE_LETTERS) else str(i)
            btn = ChoiceButton(
                choices_frame, letter=letter, text=choice_text,
                command=lambda i=i: self._on_mc_answer(i),
            )
            btn.grid(row=i, column=0, sticky="ew", pady=4)
            self._choice_buttons.append(btn)

        # Vùng feedback (ẩn ban đầu, dùng CTkFrame thật để có thể add child sau)
        self._feedback_frame = ctk.CTkFrame(outer, fg_color="transparent")
        self._feedback_frame.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        self._feedback_frame.columnconfigure(0, weight=1)

    def _render_essay_question(self, q: Question):
        outer = ctk.CTkFrame(self._body, fg_color="transparent")
        outer.grid(row=0, column=0, sticky="nsew", padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        outer.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            outer, text="  TỰ LUẬN  ",
            font=T.FONT_SMALL_BOLD, text_color=T.TEXT_WARNING,
            fg_color=T.BG_CARD, corner_radius=4,
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        q_card = Card(outer, color=T.BG_SECONDARY)
        q_card.grid(row=1, column=0, sticky="ew", pady=(0, 16))
        q_card.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            q_card, text=q.content,
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
            wraplength=700, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        ctk.CTkLabel(
            outer,
            text='Hãy suy nghĩ câu trả lời, sau đó bấm "Xem đáp án" để kiểm tra.',
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY, justify="left",
        ).grid(row=2, column=0, sticky="w", pady=(0, 12))

        self._essay_answer_frame = ctk.CTkFrame(outer, fg_color="transparent")
        self._essay_answer_frame.grid(row=3, column=0, sticky="ew")
        self._essay_answer_frame.columnconfigure(0, weight=1)

        self._reveal_btn.grid()
        self._next_btn.grid_remove()

    # ── Logic trả lời ────────────────────────────────────────────────────────

    def _on_mc_answer(self, chosen_idx: int):
        if self._answered:
            return
        self._answered = True

        for btn in self._choice_buttons:
            btn.configure(state="disabled")

        correct_idx = int(self._current_q.correct_answer)

        for i, btn in enumerate(self._choice_buttons):
            if i == correct_idx:
                btn.set_state("correct")
            elif i == chosen_idx and chosen_idx != correct_idx:
                btn.set_state("wrong")

        response = self._session.submit_answer(chosen_idx)

        if response.is_correct:
            self._correct_so_far += 1

        self._score_chip.update_score(self._correct_so_far, self._session.current_index)

        # Luôn hiện feedback inline (đáp án đúng/sai + giải thích nếu có)
        self._show_mc_feedback(response, chosen_idx, correct_idx)

        is_last = self._session.current_index >= self._total
        self._next_btn.configure(
            text="🏁  Xem kết quả" if is_last else "Tiếp theo →"
        )
        self._next_btn.grid()

    def _show_mc_feedback(self, response: UserResponse, chosen: int, correct: int):
        """Hiện kết quả đúng/sai và giải thích trong feedback_frame."""
        # Xóa nội dung cũ trong frame (KHÔNG destroy frame)
        for w in self._feedback_frame.winfo_children():
            w.destroy()

        if response.is_correct:
            status_color = T.TEXT_SUCCESS
            status_text = "✓  Đúng rồi!"
        else:
            correct_letter = CHOICE_LETTERS[correct] if correct < len(CHOICE_LETTERS) else str(correct)
            status_color = T.TEXT_ERROR
            status_text = f"✗  Sai!  Đáp án đúng là:  {correct_letter}"

        ctk.CTkLabel(
            self._feedback_frame, text=status_text,
            font=T.FONT_BODY_BOLD, text_color=status_color,
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        if response.explanation:
            ctk.CTkLabel(
                self._feedback_frame, text="Giải thích:",
                font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
            ).grid(row=1, column=0, sticky="w", pady=(0, 4))

            ExplanationBox(
                self._feedback_frame, text=response.explanation, height=100,
            ).grid(row=2, column=0, sticky="ew")

    def _reveal_essay_answer(self):
        if self._answer_revealed:
            return
        self._answer_revealed = True
        self._reveal_btn.configure(state="disabled")

        q = self._current_q
        container = self._essay_answer_frame
        container.columnconfigure(0, weight=1)

        Divider(container).grid(row=0, column=0, sticky="ew", pady=(0, 12))

        ctk.CTkLabel(
            container, text="Đáp án mẫu:",
            font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
        ).grid(row=1, column=0, sticky="w", pady=(0, 6))

        answer_box = ctk.CTkFrame(
            container, fg_color=T.BG_CARD, corner_radius=8,
            border_width=1, border_color=T.BORDER_SUCCESS,
        )
        answer_box.grid(row=2, column=0, sticky="ew", pady=(0, 12))
        answer_box.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            answer_box, text=str(q.correct_answer),
            font=T.FONT_BODY, text_color=T.TEXT_SUCCESS,
            wraplength=680, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        if q.explanation:
            ctk.CTkLabel(
                container, text="Giải thích:",
                font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
            ).grid(row=3, column=0, sticky="w", pady=(0, 6))

            ExplanationBox(
                container, text=q.explanation, height=100,
            ).grid(row=4, column=0, sticky="ew", pady=(0, 12))

        # Submit để engine tịnh tiến index
        self._session.submit_answer("[đã xem đáp án]")

        # Fix: kiểm tra đúng sau khi submit (current_index đã tăng)
        is_last = self._session.current_index >= self._total
        self._next_btn.configure(
            text="🏁  Xem kết quả" if is_last else "Tiếp theo →"
        )
        self._next_btn.grid()

    # ── Điều hướng ───────────────────────────────────────────────────────────

    def _next_question(self):
        if self._session.current_index >= self._total:
            self._finish()
        else:
            self._load_current_question()

    def _finish(self):
        self._progress_bar.set(1.0)
        self._on_finish(self._session)

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