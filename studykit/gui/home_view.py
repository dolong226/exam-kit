"""
HomeView — Màn hình chính.
Hiển thị danh sách testbank, cho phép chọn chế độ, rồi bắt đầu quiz.
"""

import customtkinter as ctk
from pathlib import Path
from typing import Callable, List, Optional

from . import theme as T
from .widgets import AppButton, Card, SectionLabel, BodyLabel, Divider


# Thư mục testbanks nằm cùng cấp với main.py
TESTBANKS_DIR = Path(__file__).parent.parent.parent / "testbanks"


def _scan_testbanks() -> List[Path]:
    """Quét đệ quy thư mục testbanks/ tìm tất cả file .yaml/.yml."""
    if not TESTBANKS_DIR.exists():
        return []
    files = sorted(
        p for p in TESTBANKS_DIR.rglob("*")
        if p.suffix.lower() in (".yaml", ".yml") and p.is_file()
    )
    return files


class HomeView(ctk.CTkFrame):
    """
    Frame chính của màn hình Home.
    Callback on_start(file_path, mode, show_immediately) được gọi khi user bấm Bắt đầu.
    """

    def __init__(self, master, on_start: Callable[[Path, str, bool], None]):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._on_start = on_start
        self._selected_file: Optional[Path] = None
        self._testbank_files: List[Path] = []

        self._build_ui()

    # ── Build UI ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self._build_header()
        self._build_body()
        self._build_footer()

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=80)
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            header,
            text="📚  Exam Kit",
            font=T.FONT_TITLE,
            text_color=T.TEXT_ACCENT,
        ).grid(row=0, column=0, padx=T.PADDING_OUTER, pady=(18, 4), sticky="w")

        ctk.CTkLabel(
            header,
            text="Chọn bộ đề và bắt đầu luyện tập",
            font=T.FONT_SUBTITLE,
            text_color=T.TEXT_SECONDARY,
        ).grid(row=1, column=0, padx=T.PADDING_OUTER, pady=(0, 14), sticky="w")

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=T.BG_PRIMARY, corner_radius=0)
        body.grid(row=1, column=0, sticky="nsew", padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        body.columnconfigure(0, weight=3)
        body.columnconfigure(1, weight=2)
        body.rowconfigure(0, weight=1)

        self._build_testbank_panel(body)
        self._build_config_panel(body)

    def _build_testbank_panel(self, parent):
        """Panel trái: danh sách testbank."""
        panel = Card(parent)
        panel.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)

        SectionLabel(panel, text="Bộ đề").grid(
            row=0, column=0, padx=T.PADDING_INNER, pady=(T.PADDING_INNER, 8), sticky="w"
        )

        Divider(panel).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Scrollable list
        self._list_frame = ctk.CTkScrollableFrame(
            panel,
            fg_color=T.BG_SECONDARY,
            corner_radius=8,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._list_frame.grid(row=2, column=0, sticky="nsew", padx=T.PADDING_INNER, pady=(8, T.PADDING_INNER))
        self._list_frame.columnconfigure(0, weight=1)

        self._reload_testbank_list()

        # Nút reload
        AppButton(
            panel,
            text="↻  Làm mới",
            command=self._reload_testbank_list,
            style="secondary",
            width=110,
            height=T.BTN_HEIGHT_SM,
        ).grid(row=3, column=0, padx=T.PADDING_INNER, pady=(0, T.PADDING_INNER), sticky="e")

    def _build_config_panel(self, parent):
        """Panel phải: cấu hình quiz và nút bắt đầu."""
        panel = Card(parent)
        panel.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        panel.columnconfigure(0, weight=1)

        # ── File đang chọn ────────────────────────────────────────────────
        SectionLabel(panel, text="Cấu hình").grid(
            row=0, column=0, padx=T.PADDING_INNER, pady=(T.PADDING_INNER, 8), sticky="w"
        )
        Divider(panel).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        ctk.CTkLabel(
            panel,
            text="Bộ đề đang chọn",
            font=T.FONT_SMALL,
            text_color=T.TEXT_SECONDARY,
        ).grid(row=2, column=0, padx=T.PADDING_INNER, pady=(12, 2), sticky="w")

        self._selected_label = ctk.CTkLabel(
            panel,
            text="— Chưa chọn bộ đề nào —",
            font=T.FONT_BODY_BOLD,
            text_color=T.TEXT_WARNING,
            wraplength=230,
            justify="left",
        )
        self._selected_label.grid(row=3, column=0, padx=T.PADDING_INNER, pady=(0, 12), sticky="w")

        Divider(panel).grid(row=4, column=0, sticky="ew", padx=T.PADDING_INNER)

        # ── Chế độ ────────────────────────────────────────────────────────
        ctk.CTkLabel(
            panel,
            text="Chế độ",
            font=T.FONT_SMALL,
            text_color=T.TEXT_SECONDARY,
        ).grid(row=5, column=0, padx=T.PADDING_INNER, pady=(12, 4), sticky="w")

        self._mode_var = ctk.StringVar(value="multiple_choice")
        mode_frame = ctk.CTkFrame(panel, fg_color="transparent")
        mode_frame.grid(row=6, column=0, padx=T.PADDING_INNER, pady=(0, 12), sticky="w")

        ctk.CTkRadioButton(
            mode_frame,
            text="Trắc nghiệm",
            variable=self._mode_var,
            value="multiple_choice",
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            fg_color=T.BTN_PRIMARY,
            border_color=T.BORDER_DEFAULT,
        ).grid(row=0, column=0, padx=(0, 16))

        ctk.CTkRadioButton(
            mode_frame,
            text="Tự luận",
            variable=self._mode_var,
            value="essay",
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            fg_color=T.BTN_PRIMARY,
            border_color=T.BORDER_DEFAULT,
        ).grid(row=0, column=1)

        Divider(panel).grid(row=7, column=0, sticky="ew", padx=T.PADDING_INNER)

        # ── Tùy chọn hiện đáp án ─────────────────────────────────────────
        ctk.CTkLabel(
            panel,
            text="Hiển thị đáp án",
            font=T.FONT_SMALL,
            text_color=T.TEXT_SECONDARY,
        ).grid(row=8, column=0, padx=T.PADDING_INNER, pady=(12, 4), sticky="w")

        self._immediate_var = ctk.BooleanVar(value=False)
        switch_frame = ctk.CTkFrame(panel, fg_color="transparent")
        switch_frame.grid(row=9, column=0, padx=T.PADDING_INNER, pady=(0, 12), sticky="w")

        self._immediate_switch = ctk.CTkSwitch(
            switch_frame,
            text="Hiện ngay sau mỗi câu",
            variable=self._immediate_var,
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            fg_color=T.BG_CARD,
            progress_color=T.BTN_PRIMARY,
            button_color=T.TEXT_PRIMARY,
        )
        self._immediate_switch.grid(row=0, column=0)

        Divider(panel).grid(row=10, column=0, sticky="ew", padx=T.PADDING_INNER)

        # ── Thông tin bộ đề ───────────────────────────────────────────────
        self._info_label = ctk.CTkLabel(
            panel,
            text="",
            font=T.FONT_SMALL,
            text_color=T.TEXT_SECONDARY,
            wraplength=230,
            justify="left",
        )
        self._info_label.grid(row=11, column=0, padx=T.PADDING_INNER, pady=(10, 8), sticky="w")

        # ── Spacer ────────────────────────────────────────────────────────
        ctk.CTkFrame(panel, fg_color="transparent", height=1).grid(row=12, column=0, sticky="ew")
        panel.rowconfigure(12, weight=1)

        # ── Nút bắt đầu ───────────────────────────────────────────────────
        self._start_btn = AppButton(
            panel,
            text="▶  Bắt đầu",
            command=self._on_start_click,
            style="primary",
            width=200,
            height=T.BTN_HEIGHT,
        )
        self._start_btn.grid(row=13, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER)
        self._start_btn.configure(state="disabled", fg_color="#555566")

    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=32)
        footer.grid(row=2, column=0, sticky="ew")
        ctk.CTkLabel(
            footer,
            text="Exam Kit v2.0  ·  CLI + GUI",
            font=T.FONT_SMALL,
            text_color=T.TEXT_SECONDARY,
        ).pack(side="right", padx=T.PADDING_OUTER, pady=6)

    # ── Logic ─────────────────────────────────────────────────────────────────

    def _reload_testbank_list(self):
        """Quét lại thư mục testbanks và render danh sách."""
        for widget in self._list_frame.winfo_children():
            widget.destroy()

        self._testbank_files = _scan_testbanks()

        if not self._testbank_files:
            BodyLabel(
                self._list_frame,
                text="Không tìm thấy file testbank nào.\nHãy thêm file .yaml vào thư mục testbanks/",
                secondary=True,
            ).pack(padx=12, pady=20)
            return

        self._file_buttons: list = []
        for i, fpath in enumerate(self._testbank_files):
            # Hiển thị tên file + subfolder tương đối
            rel = fpath.relative_to(TESTBANKS_DIR)
            display_name = str(rel)

            btn = ctk.CTkButton(
                self._list_frame,
                text=f"  📄  {display_name}",
                anchor="w",
                font=T.FONT_BODY,
                fg_color=T.BG_CARD,
                hover_color=T.BTN_SECONDARY_HOVER,
                text_color=T.TEXT_PRIMARY,
                corner_radius=6,
                height=40,
                command=lambda p=fpath, idx=i: self._select_file(p, idx),
            )
            btn.pack(fill="x", padx=4, pady=3)
            self._file_buttons.append(btn)

    def _select_file(self, fpath: Path, idx: int):
        """Đánh dấu file được chọn và cập nhật UI."""
        self._selected_file = fpath

        # Reset màu tất cả button
        for b in self._file_buttons:
            b.configure(fg_color=T.BG_CARD, border_width=0)

        # Highlight button được chọn
        self._file_buttons[idx].configure(
            fg_color=T.BTN_CHOICE_SELECTED,
            border_width=1,
            border_color=T.BORDER_ACCENT,
        )

        # Cập nhật label
        rel = fpath.relative_to(TESTBANKS_DIR)
        self._selected_label.configure(
            text=str(rel),
            text_color=T.TEXT_SUCCESS,
        )

        # Thử đọc metadata để hiển thị thông tin
        self._update_info(fpath)

        # Kích hoạt nút bắt đầu
        self._start_btn.configure(state="normal", fg_color=T.BTN_PRIMARY)

    def _update_info(self, fpath: Path):
        """Đọc nhanh metadata testbank để hiển thị thông tin tóm tắt."""
        try:
            from core.parser import parse_testbank
            tb = parse_testbank(fpath)
            mc_count = sum(1 for q in tb.questions if q.type.value == "multiple_choice")
            essay_count = sum(1 for q in tb.questions if q.type.value == "essay")
            info = (
                f"📋  {tb.title}\n"
                f"   • Trắc nghiệm: {mc_count} câu\n"
                f"   • Tự luận: {essay_count} câu"
            )
            if tb.description:
                info += f"\n\n{tb.description}"
            self._info_label.configure(text=info, text_color=T.TEXT_SECONDARY)
        except Exception as e:
            self._info_label.configure(
                text=f"⚠ Không đọc được metadata:\n{e}",
                text_color=T.TEXT_WARNING,
            )

    def _on_start_click(self):
        if not self._selected_file:
            return
        mode = self._mode_var.get()
        immediate = self._immediate_var.get()
        self._on_start(self._selected_file, mode, immediate)