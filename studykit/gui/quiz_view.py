"""
QuizView — Màn hình làm bài.
Xử lý cả 2 chế độ: Multiple Choice và Essay.

Fixes:
- ChoiceButton mới dùng Frame layout → text dài tự wrap, không bị cắt
- _show_mc_feedback: clear children đúng cách, không destroy frame
- Essay: luôn submit sau khi xem đáp án để engine tịnh tiến index
"""

import customtkinter as ctk
from typing import Callable, List, Optional

from studykit.core.models import Question, QuizMode, UserResponse
from studykit.core.quiz_engine import QuizSession
from . import theme as T
from .widgets import (
    AppButton, Card, SectionLabel, BodyLabel,
    ProgressBar, ScoreChip, ExplanationBox,
    ChoiceButton, Divider, ModeTag,
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
        self._session  = session
        self._on_finish = on_finish
        self._on_back   = on_back

        self._total    = len(session.questions)
        self._current_q: Optional[Question] = None
        self._answered         = False
        self._answer_revealed  = False
        self._correct_so_far   = 0
        self._choice_buttons:  List[ChoiceButton] = []
        self._feedback_frame:  Optional[ctk.CTkFrame] = None
        self._essay_ans_frame: Optional[ctk.CTkFrame] = None

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_topbar()
        self._build_body()
        self._build_bottombar()
        self._load_current_question()

    # ── Build UI ─────────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=52)
        bar.grid(row=0, column=0, sticky="ew")
        bar.columnconfigure(1, weight=1)
        bar.grid_propagate(False)

        AppButton(
            bar, text="← Thoát", command=self._confirm_back,
            style="neutral", width=80, height=T.BTN_HEIGHT_SM,
        ).grid(row=0, column=0, padx=14, pady=10)

        self._progress_label = ctk.CTkLabel(
            bar, text="", font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SECONDARY,
        )
        self._progress_label.grid(row=0, column=1, pady=10)

        self._score_chip = ScoreChip(bar, "0/0")
        self._score_chip.grid(row=0, column=2, padx=14, pady=10)

    def _build_body(self):
        self._body = ctk.CTkScrollableFrame(
            self, fg_color=T.BG_PRIMARY, corner_radius=0,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._body.grid(row=1, column=0, sticky="nsew")
        self._body.columnconfigure(0, weight=1)

    def _build_bottombar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=60)
        bar.grid(row=2, column=0, sticky="ew")
        bar.columnconfigure(0, weight=1)
        bar.grid_propagate(False)

        self._progress_bar = ProgressBar(bar)
        self._progress_bar.grid(row=0, column=0, columnspan=3, sticky="ew", padx=0, pady=(0, 0))
        self._progress_bar.set(0)

        btn_frame = ctk.CTkFrame(bar, fg_color="transparent")
        btn_frame.grid(row=1, column=0, columnspan=3, pady=(8, 8))

        self._reveal_btn = AppButton(
            btn_frame, text="Xem đáp án",
            command=self._reveal_essay_answer,
            style="secondary", width=140, height=T.BTN_HEIGHT_SM,
        )
        self._reveal_btn.grid(row=0, column=0, padx=6)

        self._next_btn = AppButton(
            btn_frame, text="Tiếp theo →",
            command=self._next_question,
            style="primary", width=140, height=T.BTN_HEIGHT_SM,
        )
        self._next_btn.grid(row=0, column=1, padx=6)

        self._reveal_btn.grid_remove()
        self._next_btn.grid_remove()

    # ── Clear & Load ──────────────────────────────────────────────────────────

    def _clear_body(self):
        for w in self._body.winfo_children():
            w.destroy()
        self._choice_buttons  = []
        self._feedback_frame  = None
        self._essay_ans_frame = None
        self._answered         = False
        self._answer_revealed  = False
        self._reveal_btn.configure(state="normal")
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

        self._progress_label.configure(text=f"Câu  {idx} / {self._total}")
        self._score_chip.update_score(self._correct_so_far, self._session.current_index)
        self._progress_bar.set(self._session.current_index / self._total)

        if q.type == QuizMode.MULTIPLE_CHOICE:
            self._render_mc(q)
        else:
            self._render_essay(q)

    # ── Render câu hỏi ───────────────────────────────────────────────────────

    def _render_mc(self, q: Question):
        outer = ctk.CTkFrame(self._body, fg_color="transparent")
        outer.grid(row=0, column=0, sticky="nsew",
                   padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        outer.columnconfigure(0, weight=1)

        ModeTag(outer, mode="mc").grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Câu hỏi
        q_card = Card(outer, color=T.BG_CARD)
        q_card.grid(row=1, column=0, sticky="ew", pady=(0, 14))
        q_card.columnconfigure(0, weight=1)
        ctk.CTkLabel(
            q_card, text=q.content,
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
            wraplength=700, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        # Choices
        choices_frame = ctk.CTkFrame(outer, fg_color="transparent")
        choices_frame.grid(row=2, column=0, sticky="ew")
        choices_frame.columnconfigure(0, weight=1)

        for i, text in enumerate(q.choices or []):
            letter = CHOICE_LETTERS[i] if i < len(CHOICE_LETTERS) else str(i)
            btn = ChoiceButton(
                choices_frame, letter=letter, text=text,
                command=lambda i=i: self._on_mc_answer(i),
            )
            btn.grid(row=i, column=0, sticky="ew", pady=3)
            self._choice_buttons.append(btn)

        # Feedback placeholder
        self._feedback_frame = ctk.CTkFrame(outer, fg_color="transparent")
        self._feedback_frame.grid(row=3, column=0, sticky="ew", pady=(10, 0))
        self._feedback_frame.columnconfigure(0, weight=1)

    def _render_essay(self, q: Question):
        outer = ctk.CTkFrame(self._body, fg_color="transparent")
        outer.grid(row=0, column=0, sticky="nsew",
                   padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        outer.columnconfigure(0, weight=1)

        ModeTag(outer, mode="essay").grid(row=0, column=0, sticky="w", pady=(0, 10))

        q_card = Card(outer, color=T.BG_CARD)
        q_card.grid(row=1, column=0, sticky="ew", pady=(0, 14))
        q_card.columnconfigure(0, weight=1)
        ctk.CTkLabel(
            q_card, text=q.content,
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
            wraplength=700, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        ctk.CTkLabel(
            outer,
            text='Hãy nghĩ câu trả lời, sau đó bấm "Xem đáp án" để kiểm tra.',
            font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY, justify="left",
        ).grid(row=2, column=0, sticky="w", pady=(0, 10))

        self._essay_ans_frame = ctk.CTkFrame(outer, fg_color="transparent")
        self._essay_ans_frame.grid(row=3, column=0, sticky="ew")
        self._essay_ans_frame.columnconfigure(0, weight=1)

        self._reveal_btn.grid()
        self._next_btn.grid_remove()

    # ── Logic MC ─────────────────────────────────────────────────────────────

    def _on_mc_answer(self, chosen_idx: int):
        if self._answered:
            return
        self._answered = True

        for btn in self._choice_buttons:
            btn.disable()

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
        self._show_mc_feedback(response, chosen_idx, correct_idx)

        is_last = self._session.current_index >= self._total
        self._next_btn.configure(text="Xem kết quả  🏁" if is_last else "Tiếp theo →")
        self._next_btn.grid()

    def _show_mc_feedback(self, response: UserResponse, chosen: int, correct: int):
        for w in self._feedback_frame.winfo_children():
            w.destroy()

        is_correct = response.is_correct
        accent     = T.BORDER_SUCCESS if is_correct else T.BORDER_ERROR
        bg         = T.BTN_SUCCESS    if is_correct else T.BTN_DANGER

        # Banner
        banner = ctk.CTkFrame(
            self._feedback_frame,
            fg_color=bg, corner_radius=8,
        )
        banner.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        banner.columnconfigure(1, weight=1)

        # Accent bar bên trái
        ctk.CTkFrame(
            banner, width=3, fg_color=accent, corner_radius=0,
        ).grid(row=0, column=0, sticky="ns", padx=(0, 12), pady=0)

        if is_correct:
            status_text  = "Đúng rồi!"
            status_color = T.TEXT_SUCCESS
        else:
            letter       = CHOICE_LETTERS[correct] if correct < len(CHOICE_LETTERS) else str(correct)
            status_text  = f"Sai  —  Đáp án đúng là  {letter}"
            status_color = T.TEXT_ERROR

        ctk.CTkLabel(
            banner, text=status_text,
            font=T.FONT_SMALL_BOLD, text_color=status_color,
        ).grid(row=0, column=1, padx=(0, 12), pady=10, sticky="w")

        if response.explanation:
            ctk.CTkLabel(
                self._feedback_frame, text="Giải thích",
                font=T.FONT_TINY_BOLD, text_color=T.TEXT_TERTIARY,
            ).grid(row=1, column=0, sticky="w", pady=(0, 4))

            ExplanationBox(
                self._feedback_frame, text=response.explanation, height=90,
            ).grid(row=2, column=0, sticky="ew")

    # ── Logic Essay ───────────────────────────────────────────────────────────

    def _reveal_essay_answer(self):
        if self._answer_revealed:
            return
        self._answer_revealed = True
        self._reveal_btn.configure(state="disabled")

        q         = self._current_q
        container = self._essay_ans_frame
        container.columnconfigure(0, weight=1)

        Divider(container).grid(row=0, column=0, sticky="ew", pady=(0, 12))

        ctk.CTkLabel(
            container, text="Đáp án mẫu",
            font=T.FONT_TINY_BOLD, text_color=T.TEXT_TERTIARY,
        ).grid(row=1, column=0, sticky="w", pady=(0, 6))

        ans_card = ctk.CTkFrame(
            container, fg_color=T.BG_CARD, corner_radius=8,
            border_width=1, border_color=T.BORDER_SUCCESS,
        )
        ans_card.grid(row=2, column=0, sticky="ew", pady=(0, 12))
        ans_card.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            ans_card, text=str(q.correct_answer),
            font=T.FONT_BODY, text_color=T.TEXT_SUCCESS,
            wraplength=680, justify="left", anchor="nw",
        ).grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ew")

        if q.explanation:
            ctk.CTkLabel(
                container, text="Giải thích",
                font=T.FONT_TINY_BOLD, text_color=T.TEXT_TERTIARY,
            ).grid(row=3, column=0, sticky="w", pady=(0, 6))
            ExplanationBox(
                container, text=q.explanation, height=90,
            ).grid(row=4, column=0, sticky="ew", pady=(0, 12))

        self._session.submit_answer("[đã xem đáp án]")

        is_last = self._session.current_index >= self._total
        self._next_btn.configure(text="Xem kết quả  🏁" if is_last else "Tiếp theo →")
        self._next_btn.grid()

    # ── Navigation ────────────────────────────────────────────────────────────

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
            text="Thoát bài làm?\nTiến độ hiện tại sẽ không được lưu.",
            font=T.FONT_BODY, text_color=T.TEXT_SECONDARY, justify="center",
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