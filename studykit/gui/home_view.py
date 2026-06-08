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

from studykit.core.parser import detect_mode_from_path
from . import theme as T
from .widgets import AppButton, Card, SectionLabel, BodyLabel, Divider

TESTBANKS_DIR = Path(__file__).parent.parent.parent / "testbanks"

_ESSAY_FOLDERS = {"tự luận", "tu luan", "essay"}
_MC_FOLDERS = {"trắc nghiệm", "trac nghiem", "multiple_choice", "multiplechoice"}

# Màu avatar cho từng môn (cycle)
_AVATAR_COLORS = ["#5c6bc0", "#26a69a", "#ef5350", "#66bb6a", "#ffa726", "#ab47bc", "#29b6f6"]


def _is_supported_file(p: Path) -> bool:
    return p.is_file() and p.suffix.lower() in (".yaml", ".yml", ".md", ".markdown")


def _scan_subjects() -> List[str]:
    if not TESTBANKS_DIR.exists():
        return []
    return sorted(
        d.name for d in TESTBANKS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def _scan_types(subject: str) -> List[str]:
    subject_dir = TESTBANKS_DIR / subject
    if not subject_dir.exists():
        return []
    return sorted(
        d.name for d in subject_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def _scan_files(subject: str, type_name: str) -> List[Path]:
    folder = TESTBANKS_DIR / subject / type_name
    if not folder.exists():
        return []
    return sorted(p for p in folder.iterdir() if _is_supported_file(p))


class HomeView(ctk.CTkFrame):
    def __init__(self, master, on_start: Callable[[Path, bool], None]):
        super().__init__(master, fg_color="#0d0d0d", corner_radius=0)
        self._on_start = on_start
        self._selected_file: Optional[Path] = None
        self._selected_subject: Optional[str] = None
        self._selected_type: Optional[str] = None

        self._subject_buttons: List[ctk.CTkFrame] = []
        self._subject_names: List[str] = []
        self._type_buttons: List[ctk.CTkButton] = []
        self._file_buttons: List[ctk.CTkFrame] = []
        self._file_paths: List[Path] = []

        # Info state for config panel
        self._info_title = ""
        self._info_subtitle = ""
        self._info_mode = ""

        self._build_ui()

    # ── Build UI ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self._build_header()
        self._build_body()
        self._build_footer()

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color="#0d0d0d", corner_radius=0, height=52)
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(1, weight=1)
        header.grid_propagate(False)

        # Dot accent
        ctk.CTkLabel(
            header, text="●",
            font=(T.FONT_FAMILY, 13), text_color=T.BTN_PRIMARY,
        ).grid(row=0, column=0, padx=(20, 8), pady=14)

        ctk.CTkLabel(
            header, text="Exam Kit",
            font=T.FONT_TITLE, text_color=T.TEXT_PRIMARY,
        ).grid(row=0, column=1, pady=14, sticky="w")

    def _build_body(self):
        # Nền body tối hơn một chút
        body = ctk.CTkFrame(self, fg_color="#111118", corner_radius=0)
        body.grid(row=1, column=0, sticky="nsew")
        body.columnconfigure(0, weight=2)
        body.columnconfigure(1, weight=3)
        body.columnconfigure(2, weight=2)
        body.rowconfigure(0, weight=1)

        self._build_subject_panel(body)
        self._build_file_panel(body)
        self._build_config_panel(body)

    def _build_subject_panel(self, parent):
        """Panel trái: MÔN HỌC."""
        panel = ctk.CTkFrame(parent, fg_color="#111118", corner_radius=0)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)

        # Header label
        ctk.CTkLabel(
            panel, text="MÔN HỌC",
            font=(T.FONT_FAMILY, 11, "bold"),
            text_color="#505060",
        ).grid(row=0, column=0, padx=16, pady=(20, 8), sticky="w")

        # Scrollable list
        self._subject_list = ctk.CTkScrollableFrame(
            panel, fg_color="transparent", corner_radius=0,
            scrollbar_button_color="#222230",
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._subject_list.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self._subject_list.columnconfigure(0, weight=1)

        # Reload btn ở dưới
        ctk.CTkButton(
            panel, text="↻  Làm mới", command=self._reload_all,
            fg_color="transparent", hover_color="#1e1e2e",
            text_color="#505060", font=T.FONT_SMALL,
            corner_radius=6, height=28, border_width=0,
        ).grid(row=2, column=0, padx=16, pady=(4, 12), sticky="w")

        self._reload_subjects()

    def _build_file_panel(self, parent):
        """Panel giữa: 2 card loại + danh sách file."""
        panel = ctk.CTkFrame(parent, fg_color="#16161e", corner_radius=0)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(2, weight=1)

        # ── 2 card loại ──
        self._type_frame = ctk.CTkFrame(panel, fg_color="transparent")
        self._type_frame.grid(row=0, column=0, sticky="ew", padx=16, pady=(20, 0))
        self._type_frame.columnconfigure(0, weight=1)
        self._type_frame.columnconfigure(1, weight=1)

        self._render_type_placeholder()

        # ── BÀI QUIZ label ──
        ctk.CTkLabel(
            panel, text="BÀI QUIZ",
            font=(T.FONT_FAMILY, 11, "bold"),
            text_color="#505060",
        ).grid(row=1, column=0, padx=16, pady=(20, 8), sticky="w")

        # ── File list ──
        self._file_list = ctk.CTkScrollableFrame(
            panel, fg_color="transparent", corner_radius=0,
            scrollbar_button_color="#222230",
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._file_list.grid(row=2, column=0, sticky="nsew", padx=0, pady=(0, 12))
        self._file_list.columnconfigure(0, weight=1)

        self._render_file_placeholder("Chọn môn học và loại bài trước")

    def _build_config_panel(self, parent):
        """Panel phải: CẤU HÌNH."""
        panel = ctk.CTkFrame(parent, fg_color="#111118", corner_radius=0)
        panel.grid(row=0, column=2, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(10, weight=1)

        # ── CẤU HÌNH label ──
        ctk.CTkLabel(
            panel, text="CẤU HÌNH",
            font=(T.FONT_FAMILY, 11, "bold"),
            text_color="#505060",
        ).grid(row=0, column=0, padx=16, pady=(20, 12), sticky="w")

        # ── BÀI ĐANG CHỌN label ──
        ctk.CTkLabel(
            panel, text="BÀI ĐANG CHỌN",
            font=(T.FONT_FAMILY, 10, "bold"),
            text_color="#404050",
        ).grid(row=1, column=0, padx=16, pady=(0, 6), sticky="w")

        # Card bài đang chọn
        self._selected_card = ctk.CTkFrame(
            panel, fg_color="#1c1c28", corner_radius=10,
        )
        self._selected_card.grid(row=2, column=0, sticky="ew", padx=12, pady=(0, 16))
        self._selected_card.columnconfigure(0, weight=1)

        self._selected_title_lbl = ctk.CTkLabel(
            self._selected_card, text="— Chưa chọn —",
            font=T.FONT_BODY_BOLD, text_color="#505060",
            wraplength=190, justify="left", anchor="w",
        )
        self._selected_title_lbl.grid(row=0, column=0, padx=12, pady=(12, 2), sticky="w")

        self._selected_sub_lbl = ctk.CTkLabel(
            self._selected_card, text="",
            font=T.FONT_SMALL, text_color="#404050",
            anchor="w",
        )
        self._selected_sub_lbl.grid(row=1, column=0, padx=12, pady=(0, 8), sticky="w")

        self._mode_chip = ctk.CTkLabel(
            self._selected_card, text="",
            font=(T.FONT_FAMILY, 10, "bold"),
            text_color="#ffffff",
            fg_color="#3a2a70", corner_radius=4,
        )
        self._mode_chip.grid(row=2, column=0, padx=12, pady=(0, 12), sticky="w")

        # ── TÙY CHỌN ──
        ctk.CTkLabel(
            panel, text="TÙY CHỌN",
            font=(T.FONT_FAMILY, 10, "bold"),
            text_color="#404050",
        ).grid(row=3, column=0, padx=16, pady=(0, 8), sticky="w")

        self._shuffle_var = ctk.BooleanVar(value=False)
        ctk.CTkSwitch(
            panel,
            text="Xáo trộn câu hỏi",
            variable=self._shuffle_var,
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            fg_color="#2a2a3a",
            progress_color=T.BTN_PRIMARY,
            button_color="#ffffff",
            button_hover_color="#dddddd",
        ).grid(row=4, column=0, padx=16, pady=(0, 10), sticky="w")

        self._shuffle_choices_var = ctk.BooleanVar(value=False)
        ctk.CTkSwitch(
            panel,
            text="Xáo trộn đáp án",
            variable=self._shuffle_choices_var,
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            fg_color="#2a2a3a",
            progress_color=T.BTN_PRIMARY,
            button_color="#ffffff",
            button_hover_color="#dddddd",
        ).grid(row=5, column=0, padx=16, pady=(0, 16), sticky="w")

        # Spacer
        ctk.CTkFrame(panel, fg_color="transparent", height=1).grid(row=10, column=0)

        # ── Nút Bắt đầu ──
        self._start_btn = ctk.CTkButton(
            panel,
            text="▶  Bắt đầu",
            command=self._on_start_click,
            font=T.FONT_BODY_BOLD,
            fg_color="#2a2a3a",
            hover_color="#3a3a50",
            text_color="#505060",
            corner_radius=10,
            height=52,
            border_width=1,
            border_color="#3a3a4a",
        )
        self._start_btn.grid(row=11, column=0, padx=12, pady=16, sticky="ew")

    def _build_footer(self):
        footer = ctk.CTkFrame(self, fg_color="#0d0d0d", corner_radius=0, height=30)
        footer.grid(row=2, column=0, sticky="ew")
        ctk.CTkLabel(
            footer,
            text="github.com/dolong226/exam-kit",
            font=T.FONT_SMALL, text_color="#303040",
        ).pack(side="right", padx=20, pady=6)

    # ── Reload / Render ───────────────────────────────────────────────────────

    def _reload_all(self):
        self._selected_subject = None
        self._selected_type = None
        self._selected_file = None
        self._reload_subjects()
        self._render_type_placeholder()
        self._render_file_placeholder("Chọn môn học và loại bài trước")
        self._reset_selected_card()
        self._set_start_btn_disabled()

    def _reload_subjects(self):
        for w in self._subject_list.winfo_children():
            w.destroy()
        self._subject_buttons = []
        self._subject_names = []

        subjects = _scan_subjects()
        if not subjects:
            ctk.CTkLabel(
                self._subject_list,
                text="Không tìm thấy môn học.\nHãy tạo folder trong testbanks/",
                font=T.FONT_SMALL, text_color="#404050",
                justify="left",
            ).pack(padx=16, pady=20, anchor="w")
            return

        for i, name in enumerate(subjects):
            color = _AVATAR_COLORS[i % len(_AVATAR_COLORS)]
            initial = name[0].upper()

            # Đếm số file
            try:
                types = _scan_types(name)
                total_files = sum(len(_scan_files(name, t)) for t in types)
            except Exception:
                total_files = 0

            row = ctk.CTkFrame(
                self._subject_list,
                fg_color="transparent",
                corner_radius=8,
                cursor="hand2",
            )
            row.pack(fill="x", padx=8, pady=2)
            row.columnconfigure(1, weight=1)

            # Avatar
            avatar = ctk.CTkLabel(
                row, text=initial,
                font=(T.FONT_FAMILY, 12, "bold"),
                text_color="#ffffff",
                fg_color=color,
                corner_radius=6,
                width=32, height=32,
            )
            avatar.grid(row=0, column=0, padx=(10, 8), pady=8)

            name_lbl = ctk.CTkLabel(
                row, text=name,
                font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
                anchor="w",
            )
            name_lbl.grid(row=0, column=1, sticky="w")

            count_lbl = ctk.CTkLabel(
                row, text=f" {total_files} ",
                font=(T.FONT_FAMILY, 10),
                text_color="#505060",
                fg_color="#1e1e2e",
                corner_radius=4,
            )
            count_lbl.grid(row=0, column=2, padx=(0, 10))

            # Click
            def _make_click(n=name, r=row):
                def click(e=None):
                    self._select_subject(n, r)
                return click
            fn = _make_click()
            for widget in [row, avatar, name_lbl, count_lbl]:
                widget.bind("<Button-1>", fn)

            self._subject_buttons.append(row)
            self._subject_names.append(name)

    def _render_type_placeholder(self):
        for w in self._type_frame.winfo_children():
            w.destroy()
        self._type_buttons = []
        ctk.CTkLabel(
            self._type_frame,
            text="Chọn môn học trước",
            font=T.FONT_SMALL, text_color="#404050",
        ).grid(row=0, column=0, columnspan=2, padx=4, pady=8, sticky="w")

    def _render_types(self, types: List[str]):
        for w in self._type_frame.winfo_children():
            w.destroy()
        self._type_buttons = []

        if not types:
            ctk.CTkLabel(
                self._type_frame,
                text="Không có loại bài nào",
                font=T.FONT_SMALL, text_color="#404050",
            ).grid(row=0, column=0, padx=4, pady=8, sticky="w")
            return

        for col, name in enumerate(types):
            key = name.strip().lower()
            if key in _ESSAY_FOLDERS:
                icon = "✍️"
            elif key in _MC_FOLDERS:
                icon = "📝"
            else:
                icon = "📁"

            btn = ctk.CTkButton(
                self._type_frame,
                text=f"{icon}\n{name}",
                font=T.FONT_BODY_BOLD,
                text_color=T.TEXT_PRIMARY,
                fg_color="#1c1c28",
                hover_color="#252535",
                corner_radius=10,
                height=72,
                border_width=1,
                border_color="#2a2a3a",
                command=lambda n=name: self._select_type(n),
            )
            btn.grid(row=0, column=col, padx=(0, 6) if col == 0 else (6, 0), sticky="ew")
            self._type_buttons.append(btn)

    def _render_file_placeholder(self, msg: str):
        for w in self._file_list.winfo_children():
            w.destroy()
        self._file_buttons = []
        self._file_paths = []
        ctk.CTkLabel(
            self._file_list, text=msg,
            font=T.FONT_SMALL, text_color="#404050",
        ).pack(padx=16, pady=20, anchor="w")

    def _render_files(self, files: List[Path]):
        for w in self._file_list.winfo_children():
            w.destroy()
        self._file_buttons = []
        self._file_paths = list(files)

        if not files:
            ctk.CTkLabel(
                self._file_list,
                text="Không có file bài quiz nào.\nHãy thêm file .md hoặc .yaml vào folder.",
                font=T.FONT_SMALL, text_color="#404050",
            ).pack(padx=16, pady=20, anchor="w")
            return

        for i, fpath in enumerate(files):
            # Lấy thông tin số câu + mode (nếu có thể)
            try:
                from studykit.core.parser import parse_testbank
                tb = parse_testbank(fpath)
                count = len(tb.questions)
                mode = detect_mode_from_path(fpath)
                mode_str = "trắc nghiệm" if mode and "MULTIPLE" in mode.value.upper() else (
                    "tự luận" if mode else "hỗn hợp"
                )
                sub = f"{count} câu · {mode_str}"
            except Exception:
                sub = ""

            row = ctk.CTkFrame(
                self._file_list,
                fg_color="transparent",
                corner_radius=8,
                cursor="hand2",
            )
            row.pack(fill="x", padx=8, pady=2)
            row.columnconfigure(0, weight=1)

            title_lbl = ctk.CTkLabel(
                row, text=fpath.stem,
                font=T.FONT_BODY_BOLD, text_color=T.TEXT_PRIMARY,
                anchor="w",
            )
            title_lbl.grid(row=0, column=0, padx=14, pady=(10, 1), sticky="w")

            sub_lbl = ctk.CTkLabel(
                row, text=sub,
                font=T.FONT_SMALL, text_color="#505060",
                anchor="w",
            )
            sub_lbl.grid(row=1, column=0, padx=14, pady=(0, 10), sticky="w")

            def _make_click(p=fpath, idx=i, r=row):
                def click(e=None):
                    self._select_file(p, idx, r)
                return click
            fn = _make_click()
            for widget in [row, title_lbl, sub_lbl]:
                widget.bind("<Button-1>", fn)

            self._file_buttons.append(row)

    # ── Selection logic ───────────────────────────────────────────────────────

    def _select_subject(self, name: str, row_frame: ctk.CTkFrame):
        self._selected_subject = name
        self._selected_type = None
        self._selected_file = None

        # Highlight
        for b in self._subject_buttons:
            b.configure(fg_color="transparent")
        row_frame.configure(fg_color="#1e1e30")

        types = _scan_types(name)
        self._render_types(types)
        self._render_file_placeholder("Chọn loại bài trước")
        self._reset_selected_card()
        self._set_start_btn_disabled()

    def _select_type(self, name: str):
        self._selected_type = name
        self._selected_file = None

        # Highlight type buttons
        for btn in self._type_buttons:
            btn.configure(fg_color="#1c1c28", border_color="#2a2a3a", text_color=T.TEXT_PRIMARY)
        for btn in self._type_buttons:
            if name in btn.cget("text"):
                btn.configure(fg_color="#2a2050", border_color="#5a4a90", text_color="#ffffff")
                break

        files = _scan_files(self._selected_subject, name)
        self._render_files(files)
        self._reset_selected_card()
        self._set_start_btn_disabled()

    def _select_file(self, fpath: Path, idx: int, row_frame: ctk.CTkFrame):
        self._selected_file = fpath

        # Highlight file rows
        for b in self._file_buttons:
            b.configure(fg_color="transparent")
        row_frame.configure(fg_color="#1e1e30")

        self._update_selected_card(fpath)
        self._set_start_btn_active()

    def _update_selected_card(self, fpath: Path):
        try:
            from studykit.core.parser import parse_testbank
            tb = parse_testbank(fpath)
            count = len(tb.questions)
            mode = detect_mode_from_path(fpath)
            mode_str = "Trắc nghiệm" if mode and "MULTIPLE" in mode.value.upper() else (
                "Tự luận" if mode else "Hỗn hợp"
            )
            subject = self._selected_subject or ""
            sub = f"{subject} · {count} câu"
            self._selected_title_lbl.configure(text=tb.title, text_color=T.TEXT_PRIMARY)
            self._selected_sub_lbl.configure(text=sub, text_color="#606070")
            self._mode_chip.configure(text=f"  {mode_str.upper()}  ", fg_color="#3a2a70")
        except Exception:
            self._selected_title_lbl.configure(text=fpath.stem, text_color=T.TEXT_PRIMARY)
            self._selected_sub_lbl.configure(text="", text_color="#606070")
            self._mode_chip.configure(text="", fg_color="transparent")

    def _reset_selected_card(self):
        self._selected_title_lbl.configure(text="— Chưa chọn —", text_color="#505060")
        self._selected_sub_lbl.configure(text="")
        self._mode_chip.configure(text="", fg_color="transparent")

    def _set_start_btn_disabled(self):
        self._start_btn.configure(
            state="disabled",
            fg_color="#2a2a3a",
            hover_color="#2a2a3a",
            text_color="#505060",
            border_color="#3a3a4a",
        )

    def _set_start_btn_active(self):
        self._start_btn.configure(
            state="normal",
            fg_color="transparent",
            hover_color="#1e1e2e",
            text_color=T.TEXT_PRIMARY,
            border_color=T.TEXT_PRIMARY,
        )

    def _on_start_click(self):
        if not self._selected_file:
            return
        shuffle = self._shuffle_var.get()
        shuffle_choices = self._shuffle_choices_var.get()
        self._on_start(self._selected_file, shuffle, shuffle_choices)