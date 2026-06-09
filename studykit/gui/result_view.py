"""
ResultView — Màn hình kết quả sau khi hoàn thành quiz trắc nghiệm.
"""

import customtkinter as ctk
from pathlib import Path
from typing import Callable

from studykit.core.models import QuizMode, UserResponse
from studykit.core.quiz_engine import QuizSession
from studykit.core.reporter import export_wrong_answers
from . import theme as T
from .widgets import AppButton, Card, SectionLabel, Divider

CHOICE_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H"]


class ResultView(ctk.CTkFrame):
    def __init__(
        self,
        master,
        session: QuizSession,
        on_home: Callable,
        on_retry: Callable,
    ):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._session  = session
        self._on_home  = on_home
        self._on_retry = on_retry

        self._result = session.get_result()
        self._mode   = session.config.mode
        self._report_path = ""

        if self._result.wrong_responses and self._mode == QuizMode.MULTIPLE_CHOICE:
            self._export_report()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self._build_topbar()
        self._build_body()

    def _export_report(self):
        tb_title  = self._session.testbank.title
        safe_name = "".join(c if c.isalnum() or c in "-_ " else "_" for c in tb_title)
        safe_name = safe_name.strip().replace(" ", "_")[:40]
        output    = Path("outputs") / f"{safe_name}.wrong.md"
        try:
            for resp in self._result.wrong_responses:
                try:
                    idx = int(resp.correct_answer)
                    resp.correct_answer = CHOICE_LETTERS[idx]
                except (ValueError, IndexError):
                    pass
            export_wrong_answers(self._result, output)
            self._report_path = str(output)
        except Exception as e:
            self._report_path = f"(Lỗi xuất file: {e})"

    # ── Topbar ────────────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=52)
        bar.grid(row=0, column=0, sticky="ew")
        bar.columnconfigure(1, weight=1)
        bar.grid_propagate(False)

        AppButton(bar, text="← Trang chủ", command=self._on_home,
                  style="neutral", width=120, height=T.BTN_HEIGHT_SM,
                  ).grid(row=0, column=0, padx=14, pady=10)

        ctk.CTkLabel(bar, text="Kết quả", font=T.FONT_HEADING,
                     text_color=T.TEXT_PRIMARY,
                     ).grid(row=0, column=1, pady=10)

        AppButton(bar, text="↺  Làm lại", command=self._on_retry,
                  style="secondary", width=100, height=T.BTN_HEIGHT_SM,
                  ).grid(row=0, column=2, padx=14, pady=10)

    # ── Body ─────────────────────────────────────────────────────────────────

    def _build_body(self):
        scroll = ctk.CTkScrollableFrame(
            self, fg_color=T.BG_PRIMARY, corner_radius=0,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.columnconfigure(0, weight=1)

        inner = ctk.CTkFrame(scroll, fg_color="transparent")
        inner.grid(row=0, column=0, sticky="ew",
                   padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        inner.columnconfigure(0, weight=1)

        self._build_score_card(inner)
        self._build_wrong_list(inner)

    def _build_score_card(self, parent):
        r          = self._result
        is_perfect = r.correct_count == r.total_questions
        pct        = int(r.correct_count / r.total_questions * 100) if r.total_questions else 0

        score_color = (
            T.TEXT_SUCCESS if is_perfect or pct >= 80
            else T.TEXT_WARNING if pct >= 50
            else T.TEXT_ERROR
        )

        card = Card(parent, color=T.BG_CARD)
        card.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=0)

        # Cột trái
        left = ctk.CTkFrame(card, fg_color="transparent")
        left.grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="w")

        ctk.CTkLabel(left, text="Kết quả bài làm",
                     font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
                     ).grid(row=0, column=0, sticky="w")

        ctk.CTkLabel(left, text=r.score_string,
                     font=(T.FONT_FAMILY, 34, "bold"), text_color=score_color,
                     ).grid(row=1, column=0, sticky="w", pady=(2, 0))

        ctk.CTkLabel(
            left,
            text="câu đúng" if self._mode == QuizMode.MULTIPLE_CHOICE else "câu hoàn thành",
            font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
        ).grid(row=2, column=0, sticky="w")

        # Cột phải: stat chips
        right = ctk.CTkFrame(card, fg_color="transparent")
        right.grid(row=0, column=1, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="e")

        self._stat(right, 0, "TỔNG CÂU",    str(r.total_questions), T.TEXT_PRIMARY)
        self._stat(right, 1, "ĐÚNG",        str(r.correct_count),   T.TEXT_SUCCESS)
        wrong_n = len(r.wrong_responses)
        self._stat(right, 2, "SAI",          str(wrong_n),           T.TEXT_ERROR if wrong_n else T.TEXT_TERTIARY)

        # Thông báo footer
        row_msg = 1
        if is_perfect:
            ctk.CTkLabel(card, text="Tuyệt vời! Bạn đạt điểm hoàn hảo!",
                         font=T.FONT_SMALL_BOLD, text_color=T.TEXT_SUCCESS,
                         ).grid(row=row_msg, column=0, columnspan=2,
                                padx=T.PADDING_INNER, pady=(0, T.PADDING_INNER), sticky="w")
        elif self._report_path and not self._report_path.startswith("(Lỗi"):
            ctk.CTkLabel(card, text=f"Báo cáo câu sai đã lưu:  {self._report_path}",
                         font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
                         ).grid(row=row_msg, column=0, columnspan=2,
                                padx=T.PADDING_INNER, pady=(0, T.PADDING_INNER), sticky="w")

    def _stat(self, parent, row: int, label: str, value: str, color: str):
        chip = ctk.CTkFrame(parent, fg_color=T.BG_SECONDARY, corner_radius=8, width=72)
        chip.grid(row=row, column=0, pady=3, sticky="ew")
        ctk.CTkLabel(chip, text=value,
                     font=(T.FONT_FAMILY, 18, "bold"), text_color=color,
                     ).pack(padx=10, pady=(8, 0))
        ctk.CTkLabel(chip, text=label,
                     font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
                     ).pack(padx=10, pady=(0, 8))

    # ── Wrong list ────────────────────────────────────────────────────────────

    def _build_wrong_list(self, parent):
        wrong = self._result.wrong_responses
        if not wrong:
            if self._mode == QuizMode.ESSAY:
                ctk.CTkLabel(parent,
                             text="Tự luận: xem lại đáp án ở trên để tự đánh giá.",
                             font=T.FONT_BODY, text_color=T.TEXT_TERTIARY,
                             ).grid(row=1, column=0, pady=20)
            return

        SectionLabel(parent, text=f"Câu làm sai  ({len(wrong)} câu)").grid(
            row=1, column=0, sticky="w", pady=(0, 10)
        )

        for i, resp in enumerate(wrong):
            self._build_wrong_card(parent, row=i + 2, resp=resp, num=i + 1)

    def _build_wrong_card(self, parent, row: int, resp: UserResponse, num: int):
        card = Card(parent, color=T.BG_CARD)
        card.grid(row=row, column=0, sticky="ew", pady=5)
        card.columnconfigure(0, weight=1)

        # Header
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.grid(row=0, column=0, padx=T.PADDING_INNER,
                    pady=(T.PADDING_INNER, 8), sticky="ew")
        header.columnconfigure(1, weight=1)

        ctk.CTkLabel(header, text=f" {num} ",
                     font=T.FONT_TINY_BOLD,
                     text_color=T.TEXT_TERTIARY,
                     fg_color=T.BG_SECONDARY, corner_radius=4,
                     ).grid(row=0, column=0, padx=(0, 8))

        ctk.CTkLabel(header, text=resp.question_content,
                     font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
                     wraplength=700, justify="left", anchor="w",
                     ).grid(row=0, column=1, sticky="w")

        Divider(card).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Đáp án
        ans = ctk.CTkFrame(card, fg_color="transparent")
        ans.grid(row=2, column=0, padx=T.PADDING_INNER, pady=8, sticky="ew")
        ans.columnconfigure(1, weight=1)
        ans.columnconfigure(3, weight=1)

        ctk.CTkLabel(ans, text="Bạn chọn:", font=T.FONT_TINY,
                     text_color=T.TEXT_TERTIARY).grid(row=0, column=0, padx=(0, 6))
        ctk.CTkLabel(ans, text=resp.user_answer, font=T.FONT_SMALL_BOLD,
                     text_color=T.TEXT_ERROR).grid(row=0, column=1, sticky="w")

        ctk.CTkLabel(ans, text="Đáp án đúng:", font=T.FONT_TINY,
                     text_color=T.TEXT_TERTIARY).grid(row=0, column=2, padx=(20, 6))
        ctk.CTkLabel(ans, text=resp.correct_answer, font=T.FONT_SMALL_BOLD,
                     text_color=T.TEXT_SUCCESS).grid(row=0, column=3, sticky="w")

        # Giải thích
        if resp.explanation:
            Divider(card).grid(row=3, column=0, sticky="ew", padx=T.PADDING_INNER)
            exp = ctk.CTkFrame(card, fg_color="transparent")
            exp.grid(row=4, column=0, padx=T.PADDING_INNER,
                     pady=(8, T.PADDING_INNER), sticky="ew")
            exp.columnconfigure(0, weight=1)

            ctk.CTkLabel(exp, text="Giải thích", font=T.FONT_TINY_BOLD,
                         text_color=T.TEXT_TERTIARY,
                         ).grid(row=0, column=0, sticky="w", pady=(0, 4))
            ctk.CTkLabel(exp, text=resp.explanation,
                         font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
                         wraplength=700, justify="left", anchor="nw",
                         ).grid(row=1, column=0, sticky="ew")
        else:
            ctk.CTkFrame(card, fg_color="transparent", height=6).grid(row=4, column=0)