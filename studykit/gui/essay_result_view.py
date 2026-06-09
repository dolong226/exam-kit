"""
EssayResultView — Màn hình tổng kết sau khi chấm xong toàn bộ câu tự luận.
"""

import customtkinter as ctk
from pathlib import Path
from typing import Callable, List

from studykit.core.models import EssayGradeResult, GradeLevel
from studykit.core.reporter import export_essay_grades
from . import theme as T
from .widgets import AppButton, Card, SectionLabel, Divider


_GRADE_META = {
    GradeLevel.EXCELLENT: ("XUẤT SẮC",  T.TEXT_SUCCESS,  T.BTN_SUCCESS),
    GradeLevel.GOOD:      ("TỐT",        "#4ec3ca",       "#0e2a2a"),
    GradeLevel.PARTIAL:   ("MỘT PHẦN",  T.TEXT_WARNING,  "#2a1e10"),
    GradeLevel.INCORRECT: ("CHƯA ĐẠT",  T.TEXT_ERROR,    T.BTN_DANGER),
}


class EssayResultView(ctk.CTkFrame):
    def __init__(
        self,
        master,
        grades: List[EssayGradeResult],
        testbank_title: str,
        on_home: Callable,
        on_retry: Callable,
    ):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._grades          = grades
        self._testbank_title  = testbank_title
        self._on_home         = on_home
        self._on_retry        = on_retry
        self._report_path     = ""

        self._export_report()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self._build_topbar()
        self._build_body()

    # ── Export ────────────────────────────────────────────────────────────────

    def _export_report(self):
        safe = "".join(c if c.isalnum() or c in "-_ " else "_" for c in self._testbank_title)
        safe = safe.strip().replace(" ", "_")[:40] or "essay"
        output = Path("outputs") / f"{safe}.essay_grades.md"
        try:
            export_essay_grades(self._grades, output, testbank_title=self._testbank_title)
            self._report_path = str(output)
        except Exception as e:
            self._report_path = f"(Lỗi xuất: {e})"

    # ── Topbar ────────────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=52)
        bar.grid(row=0, column=0, sticky="ew")
        bar.columnconfigure(1, weight=1)
        bar.grid_propagate(False)

        AppButton(bar, text="← Trang chủ", command=self._on_home,
                  style="neutral", width=120, height=T.BTN_HEIGHT_SM,
                  ).grid(row=0, column=0, padx=14, pady=10)

        ctk.CTkLabel(bar, text="Kết quả Tự luận",
                     font=T.FONT_HEADING, text_color=T.TEXT_PRIMARY,
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

        self._build_summary(inner)
        self._build_detail_list(inner)

    # ── Summary card ──────────────────────────────────────────────────────────

    def _build_summary(self, parent):
        total  = len(self._grades)
        avg    = int(sum(g.score_pct for g in self._grades) / total) if total else 0
        errors = sum(1 for g in self._grades if g.error)

        avg_color = (
            T.TEXT_SUCCESS if avg >= 80
            else T.TEXT_WARNING if avg >= 50
            else T.TEXT_ERROR
        )

        card = Card(parent, color=T.BG_CARD)
        card.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=0)

        # Cột trái: điểm trung bình
        left = ctk.CTkFrame(card, fg_color="transparent")
        left.grid(row=0, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="w")

        ctk.CTkLabel(left, text="Điểm trung bình",
                     font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
                     ).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(left, text=str(avg),
                     font=(T.FONT_FAMILY, 34, "bold"), text_color=avg_color,
                     ).grid(row=1, column=0, sticky="w", pady=(2, 0))
        ctk.CTkLabel(left, text="/ 100",
                     font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
                     ).grid(row=2, column=0, sticky="w")

        # Cột phải: phân loại
        right = ctk.CTkFrame(card, fg_color="transparent")
        right.grid(row=0, column=1, padx=T.PADDING_INNER, pady=T.PADDING_INNER, sticky="ne")

        counts = {lv: 0 for lv in GradeLevel}
        for g in self._grades:
            counts[g.grade] = counts.get(g.grade, 0) + 1

        for r_idx, (level, (label, fg, bg)) in enumerate(_GRADE_META.items()):
            chip = ctk.CTkFrame(right, fg_color=bg, corner_radius=6, width=150)
            chip.grid(row=r_idx, column=0, pady=2, sticky="ew")
            ctk.CTkLabel(chip, text=f"{label}:  {counts[level]} câu",
                         font=T.FONT_TINY_BOLD, text_color=fg,
                         ).pack(padx=10, pady=5, anchor="w")

        # Footer card
        row_footer = 1
        if errors:
            ctk.CTkLabel(card,
                         text=f"⚠  {errors} câu không chấm được do lỗi API.",
                         font=T.FONT_TINY, text_color=T.TEXT_WARNING,
                         ).grid(row=row_footer, column=0, columnspan=2,
                                padx=T.PADDING_INNER, pady=(0, T.PADDING_INNER), sticky="w")
        elif self._report_path and not self._report_path.startswith("(Lỗi"):
            ctk.CTkLabel(card,
                         text=f"Báo cáo đã lưu:  {self._report_path}",
                         font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
                         ).grid(row=row_footer, column=0, columnspan=2,
                                padx=T.PADDING_INNER, pady=(0, T.PADDING_INNER), sticky="w")

    # ── Detail list ───────────────────────────────────────────────────────────

    def _build_detail_list(self, parent):
        SectionLabel(parent, text=f"Chi tiết từng câu  ({len(self._grades)} câu)").grid(
            row=1, column=0, sticky="w", pady=(0, 10)
        )
        for i, g in enumerate(self._grades):
            self._build_grade_card(parent, row=i + 2, g=g, num=i + 1)

    def _build_grade_card(self, parent, row: int, g: EssayGradeResult, num: int):
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

        ctk.CTkLabel(header, text=g.question_content,
                     font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
                     wraplength=580, justify="left", anchor="w",
                     ).grid(row=0, column=1, sticky="w")

        # Grade badge inline (nếu không lỗi)
        if not g.error:
            label, fg, bg = _GRADE_META.get(g.grade, ("N/A", T.TEXT_TERTIARY, T.BG_SECONDARY))
            ctk.CTkLabel(header,
                         text=f"  {label}  {g.score_pct}/100  ",
                         font=T.FONT_TINY_BOLD, text_color=fg, fg_color=bg,
                         corner_radius=4,
                         ).grid(row=0, column=2, padx=(8, 0))

        Divider(card).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Detail
        detail = ctk.CTkFrame(card, fg_color="transparent")
        detail.grid(row=2, column=0, padx=T.PADDING_INNER, pady=8, sticky="ew")
        detail.columnconfigure(0, weight=1)

        if g.error:
            ctk.CTkLabel(detail, text=f"⚠  {g.error}",
                         font=T.FONT_SMALL, text_color=T.TEXT_WARNING,
                         wraplength=680, justify="left",
                         ).grid(row=0, column=0, sticky="w")
            return

        # Nhận xét
        if g.feedback:
            ctk.CTkLabel(detail, text="Nhận xét",
                         font=T.FONT_TINY_BOLD, text_color=T.TEXT_TERTIARY,
                         ).grid(row=0, column=0, sticky="w", pady=(0, 2))
            ctk.CTkLabel(detail, text=g.feedback,
                         font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
                         wraplength=680, justify="left",
                         ).grid(row=1, column=0, sticky="w", pady=(0, 8))

        # Đáp án mẫu (rút gọn)
        ref_short = (g.reference_answer[:120] + "…"
                     if len(g.reference_answer) > 121 else g.reference_answer)

        ctk.CTkLabel(detail, text="Đáp án mẫu",
                     font=T.FONT_TINY_BOLD, text_color=T.TEXT_TERTIARY,
                     ).grid(row=2, column=0, sticky="w", pady=(0, 2))
        ctk.CTkLabel(detail, text=ref_short,
                     font=T.FONT_SMALL, text_color=T.TEXT_SUCCESS,
                     wraplength=680, justify="left",
                     ).grid(row=3, column=0, sticky="w")