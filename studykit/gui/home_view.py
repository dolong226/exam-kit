"""
HomeView — Màn hình chính.
Cấu trúc testbanks:
    testbanks/
        <Môn học>/
            <Trắc nghiệm | Tự luận>/
                <file.md>

Navigation: chọn Môn học → chọn Loại → chọn File → Bắt đầu
"""

import customtkinter as ctk
from pathlib import Path
from typing import Callable, List, Optional

from core.parser import detect_mode_from_path
from . import theme as T
from .widgets import AppButton, Card, SectionLabel, BodyLabel, Divider

TESTBANKS_DIR = Path(__file__).parent.parent.parent / "testbanks"

# Tên folder tự luận (so sánh lowercase stripped)
_ESSAY_FOLDERS = {"tự luận", "tu luan", "essay"}
_MC_FOLDERS = {"trắc nghiệm", "trac nghiem", "multiple_choice", "multiplechoice"}


def _is_supported_file(p: Path) -> bool:
    return p.is_file() and p.suffix.lower() in (".yaml", ".yml", ".md", ".markdown")


def _scan_subjects() -> List[str]:
    """Trả về danh sách tên môn học (folder con trực tiếp của testbanks/)."""
    if not TESTBANKS_DIR.exists():
        return []
    return sorted(
        d.name for d in TESTBANKS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def _scan_types(subject: str) -> List[str]:
    """Trả về các loại (Trắc nghiệm / Tự luận) trong môn học."""
    subject_dir = TESTBANKS_DIR / subject
    if not subject_dir.exists():
        return []
    return sorted(
        d.name for d in subject_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def _scan_files(subject: str, type_name: str) -> List[Path]:
    """Trả về danh sách file trong môn/loại."""
    folder = TESTBANKS_DIR / subject / type_name
    if not folder.exists():
        return []
    return sorted(p for p in folder.iterdir() if _is_supported_file(p))


class HomeView(ctk.CTkFrame):
    """
    Frame chính màn hình Home.
    Callback on_start(file_path, shuffle) được gọi khi user bấm Bắt đầu.
    Mode được suy ra tự động từ tên folder chứa file.
    """

    def __init__(self, master, on_start: Callable[[Path, bool], None]):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._on_start = on_start
        self._selected_file: Optional[Path] = None

        # State navigation
        self._selected_subject: Optional[str] = None
        self._selected_type: Optional[str] = None

        # Button lists để highlight
        self._subject_buttons: List[ctk.CTkButton] = []
        self._type_buttons: List[ctk.CTkButton] = []
        self._file_buttons: List[ctk.CTkButton] = []

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
            header, text="📚  Exam Kit",
            font=T.FONT_TITLE, text_color=T.TEXT_ACCENT,
        ).grid(row=0, column=0, padx=T.PADDING_OUTER, pady=(18, 4), sticky="w")

        ctk.CTkLabel(
            header, text="Chọn bộ đề và bắt đầu luyện tập",
            font=T.FONT_SUBTITLE, text_color=T.TEXT_SECONDARY,
        ).grid(row=1, column=0, padx=T.PADDING_OUTER, pady=(0, 14), sticky="w")

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=T.BG_PRIMARY, corner_radius=0)
        body.grid(row=1, column=0, sticky="nsew", padx=T.PADDING_OUTER, pady=T.PADDING_OUTER)
        # 3 cột: môn học | loại + file | cấu hình
        body.columnconfigure(0, weight=2)
        body.columnconfigure(1, weight=3)
        body.columnconfigure(2, weight=2)
        body.rowconfigure(0, weight=1)

        self._build_subject_panel(body)
        self._build_file_panel(body)
        self._build_config_panel(body)

    def _build_subject_panel(self, parent):
        """Panel trái: danh sách môn học."""
        panel = Card(parent)
        panel.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(panel, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=T.PADDING_INNER, pady=(T.PADDING_INNER, 8))
        header_frame.columnconfigure(0, weight=1)

        SectionLabel(panel, text="Môn học").grid(
            row=0, column=0, padx=T.PADDING_INNER, pady=(T.PADDING_INNER, 4), sticky="w"
        )
        Divider(panel).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        self._subject_list = ctk.CTkScrollableFrame(
            panel, fg_color=T.BG_SECONDARY, corner_radius=8,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._subject_list.grid(row=2, column=0, sticky="nsew", padx=T.PADDING_INNER, pady=(8, T.PADDING_INNER))
        self._subject_list.columnconfigure(0, weight=1)

        AppButton(
            panel, text="↻  Làm mới", command=self._reload_all,
            style="secondary", width=110, height=T.BTN_HEIGHT_SM,
        ).grid(row=3, column=0, padx=T.PADDING_INNER, pady=(0, T.PADDING_INNER), sticky="e")

        self._reload_subjects()

    def _build_file_panel(self, parent):
        """Panel giữa: chọn loại (Trắc nghiệm/Tự luận) + file."""
        panel = Card(parent)
        panel.grid(row=0, column=1, sticky="nsew", padx=6)
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(3, weight=1)

        SectionLabel(panel, text="Loại bài").grid(
            row=0, column=0, padx=T.PADDING_INNER, pady=(T.PADDING_INNER, 4), sticky="w"
        )
        Divider(panel).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Nút loại (Trắc nghiệm / Tự luận) — dạng toggle buttons
        self._type_frame = ctk.CTkFrame(panel, fg_color="transparent")
        self._type_frame.grid(row=2, column=0, sticky="ew", padx=T.PADDING_INNER, pady=8)

        SectionLabel(panel, text="Bài quiz").grid(
            row=3, column=0, padx=T.PADDING_INNER, pady=(4, 4), sticky="w"
        )
        Divider(panel).grid(row=4, column=0, sticky="ew", padx=T.PADDING_INNER)

        self._file_list = ctk.CTkScrollableFrame(
            panel, fg_color=T.BG_SECONDARY, corner_radius=8,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._file_list.grid(row=5, column=0, sticky="nsew", padx=T.PADDING_INNER, pady=(8, T.PADDING_INNER))
        self._file_list.columnconfigure(0, weight=1)
        panel.rowconfigure(5, weight=1)

        self._render_type_placeholder()
        self._render_file_placeholder("Chọn môn học và loại bài trước")

    def _build_config_panel(self, parent):
        """Panel phải: thông tin + tùy chọn + nút bắt đầu."""
        panel = Card(parent)
        panel.grid(row=0, column=2, sticky="nsew", padx=(6, 0))
        panel.columnconfigure(0, weight=1)

        SectionLabel(panel, text="Cấu hình").grid(
            row=0, column=0, padx=T.PADDING_INNER, pady=(T.PADDING_INNER, 4), sticky="w"
        )
        Divider(panel).grid(row=1, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Bộ đề đang chọn
        ctk.CTkLabel(
            panel, text="Bài đang chọn",
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
        ).grid(row=2, column=0, padx=T.PADDING_INNER, pady=(12, 2), sticky="w")

        self._selected_label = ctk.CTkLabel(
            panel, text="— Chưa chọn —",
            font=T.FONT_BODY_BOLD, text_color=T.TEXT_WARNING,
            wraplength=200, justify="left",
        )
        self._selected_label.grid(row=3, column=0, padx=T.PADDING_INNER, pady=(0, 8), sticky="w")

        Divider(panel).grid(row=4, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Thông tin bộ đề
        self._info_label = ctk.CTkLabel(
            panel, text="",
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
            wraplength=200, justify="left",
        )
        self._info_label.grid(row=5, column=0, padx=T.PADDING_INNER, pady=(10, 8), sticky="w")

        Divider(panel).grid(row=6, column=0, sticky="ew", padx=T.PADDING_INNER)

        # Shuffle toggle
        ctk.CTkLabel(
            panel, text="Tùy chọn",
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
        ).grid(row=7, column=0, padx=T.PADDING_INNER, pady=(12, 4), sticky="w")

        self._shuffle_var = ctk.BooleanVar(value=False)
        ctk.CTkSwitch(
            panel,
            text="Xáo trộn câu hỏi",
            variable=self._shuffle_var,
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            fg_color=T.BG_CARD,
            progress_color=T.BTN_PRIMARY,
            button_color=T.TEXT_PRIMARY,
        ).grid(row=8, column=0, padx=T.PADDING_INNER, pady=(0, 12), sticky="w")

        # Spacer
        ctk.CTkFrame(panel, fg_color="transparent", height=1).grid(row=9, column=0, sticky="ew")
        panel.rowconfigure(9, weight=1)

        # Nút bắt đầu
        self._start_btn = AppButton(
            panel, text="▶  Bắt đầu",
            command=self._on_start_click,
            style="primary", width=180, height=T.BTN_HEIGHT,
        )
        self._start_btn.grid(row=10, column=0, padx=T.PADDING_INNER, pady=T.PADDING_INNER)
        self._start_btn.configure(state="disabled", fg_color="#555566")

    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=32)
        footer.grid(row=2, column=0, sticky="ew")
        ctk.CTkLabel(
            footer,
            text="github.com/dolong226/exam-kit",
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
        ).pack(side="right", padx=T.PADDING_OUTER, pady=6)

    # ── Reload / Render lists ─────────────────────────────────────────────────

    def _reload_all(self):
        self._selected_subject = None
        self._selected_type = None
        self._selected_file = None
        self._reload_subjects()
        self._render_type_placeholder()
        self._render_file_placeholder("Chọn môn học và loại bài trước")
        self._selected_label.configure(text="— Chưa chọn —", text_color=T.TEXT_WARNING)
        self._info_label.configure(text="")
        self._start_btn.configure(state="disabled", fg_color="#555566")

    def _reload_subjects(self):
        for w in self._subject_list.winfo_children():
            w.destroy()
        self._subject_buttons = []

        subjects = _scan_subjects()
        if not subjects:
            BodyLabel(
                self._subject_list,
                text="Không tìm thấy môn học.\nHãy tạo folder trong testbanks/",
                secondary=True,
            ).pack(padx=12, pady=20)
            return

        for name in subjects:
            btn = ctk.CTkButton(
                self._subject_list,
                text=f"  📖  {name}",
                anchor="w",
                font=T.FONT_BODY,
                fg_color=T.BG_CARD,
                hover_color=T.BTN_SECONDARY_HOVER,
                text_color=T.TEXT_PRIMARY,
                corner_radius=6,
                height=40,
                command=lambda n=name: self._select_subject(n),
            )
            btn.pack(fill="x", padx=4, pady=3)
            self._subject_buttons.append(btn)

    def _render_type_placeholder(self):
        for w in self._type_frame.winfo_children():
            w.destroy()
        self._type_buttons = []
        ctk.CTkLabel(
            self._type_frame,
            text="Chọn môn học trước",
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
        ).pack(anchor="w")

    def _render_types(self, types: List[str]):
        for w in self._type_frame.winfo_children():
            w.destroy()
        self._type_buttons = []

        if not types:
            ctk.CTkLabel(
                self._type_frame,
                text="Không có loại bài nào",
                font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
            ).pack(anchor="w")
            return

        for name in types:
            # Xác định icon
            key = name.strip().lower()
            if key in _ESSAY_FOLDERS:
                icon = "✍️"
            elif key in _MC_FOLDERS:
                icon = "📝"
            else:
                icon = "📁"

            btn = ctk.CTkButton(
                self._type_frame,
                text=f"  {icon}  {name}",
                anchor="w",
                font=T.FONT_BODY,
                fg_color=T.BG_CARD,
                hover_color=T.BTN_SECONDARY_HOVER,
                text_color=T.TEXT_PRIMARY,
                corner_radius=6,
                height=36,
                command=lambda n=name: self._select_type(n),
            )
            btn.pack(fill="x", padx=0, pady=3)
            self._type_buttons.append(btn)

    def _render_file_placeholder(self, msg: str):
        for w in self._file_list.winfo_children():
            w.destroy()
        self._file_buttons = []
        BodyLabel(self._file_list, text=msg, secondary=True).pack(padx=12, pady=20)

    def _render_files(self, files: List[Path]):
        for w in self._file_list.winfo_children():
            w.destroy()
        self._file_buttons = []

        if not files:
            BodyLabel(
                self._file_list,
                text="Không có file bài quiz nào.\nHãy thêm file .md hoặc .yaml vào folder.",
                secondary=True,
            ).pack(padx=12, pady=20)
            return

        for i, fpath in enumerate(files):
            btn = ctk.CTkButton(
                self._file_list,
                text=f"  📄  {fpath.stem}",
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

    # ── Selection logic ───────────────────────────────────────────────────────

    def _highlight_btn(self, btn_list: List, idx: int):
        for b in btn_list:
            b.configure(fg_color=T.BG_CARD, border_width=0)
        if 0 <= idx < len(btn_list):
            btn_list[idx].configure(
                fg_color=T.BTN_CHOICE_SELECTED,
                border_width=1,
                border_color=T.BORDER_ACCENT,
            )

    def _select_subject(self, name: str):
        self._selected_subject = name
        self._selected_type = None
        self._selected_file = None

        idx = [b.cget("text").strip().lstrip("📖").strip() == name
               or name in b.cget("text")
               for b in self._subject_buttons].index(True)
        # Highlight đơn giản hơn: tìm theo text
        for i, b in enumerate(self._subject_buttons):
            if name in b.cget("text"):
                self._highlight_btn(self._subject_buttons, i)
                break

        types = _scan_types(name)
        self._render_types(types)
        self._render_file_placeholder("Chọn loại bài trước")
        self._selected_label.configure(text="— Chưa chọn file —", text_color=T.TEXT_WARNING)
        self._info_label.configure(text="")
        self._start_btn.configure(state="disabled", fg_color="#555566")

    def _select_type(self, name: str):
        self._selected_type = name
        self._selected_file = None

        for i, b in enumerate(self._type_buttons):
            if name in b.cget("text"):
                self._highlight_btn(self._type_buttons, i)
                break

        files = _scan_files(self._selected_subject, name)
        self._render_files(files)
        self._start_btn.configure(state="disabled", fg_color="#555566")

    def _select_file(self, fpath: Path, idx: int):
        self._selected_file = fpath

        self._highlight_btn(self._file_buttons, idx)

        self._selected_label.configure(
            text=fpath.stem, text_color=T.TEXT_SUCCESS,
        )
        self._update_info(fpath)
        self._start_btn.configure(state="normal", fg_color=T.BTN_PRIMARY)

    def _update_info(self, fpath: Path):
        try:
            from core.parser import parse_testbank
            tb = parse_testbank(fpath)
            count = len(tb.questions)
            mode = detect_mode_from_path(fpath)
            mode_str = "Trắc nghiệm" if mode and "MULTIPLE" in mode.value.upper() else (
                "Tự luận" if mode else "Hỗn hợp"
            )
            info = f"📋  {tb.title}\n   • {count} câu hỏi\n   • {mode_str}"
            if tb.description:
                info += f"\n\n{tb.description}"
            self._info_label.configure(text=info, text_color=T.TEXT_SECONDARY)
        except Exception as e:
            self._info_label.configure(
                text=f"⚠ Không đọc được:\n{e}",
                text_color=T.TEXT_WARNING,
            )

    def _on_start_click(self):
        if not self._selected_file:
            return
        shuffle = self._shuffle_var.get()
        self._on_start(self._selected_file, shuffle)