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
from .widgets import AppButton, Card, SectionLabel, Divider, SubjectAvatar

TESTBANKS_DIR = Path(__file__).parent.parent.parent / "testbanks"

_ESSAY_FOLDERS = {"tự luận", "tu luan", "essay"}
_MC_FOLDERS    = {"trắc nghiệm", "trac nghiem", "multiple_choice", "multiplechoice"}


def _is_supported_file(p: Path) -> bool:
    return p.is_file() and p.suffix.lower() in (".yaml", ".yml", ".md", ".markdown")


def _scan_subjects() -> List[str]:
    if not TESTBANKS_DIR.exists():
        return []
    return sorted(d.name for d in TESTBANKS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))


def _scan_types(subject: str) -> List[str]:
    d = TESTBANKS_DIR / subject
    if not d.exists():
        return []
    return sorted(x.name for x in d.iterdir() if x.is_dir() and not x.name.startswith("."))


def _scan_files(subject: str, type_name: str) -> List[Path]:
    folder = TESTBANKS_DIR / subject / type_name
    if not folder.exists():
        return []
    return sorted(p for p in folder.iterdir() if _is_supported_file(p))


def _type_display(name: str) -> tuple[str, str]:
    """Trả về (label hiển thị, badge text) cho folder loại bài."""
    key = name.strip().lower()
    if key in _ESSAY_FOLDERS:
        return ("Tự luận", T.TAG_ESSAY_TEXT)
    elif key in _MC_FOLDERS:
        return ("Trắc nghiệm", T.TAG_MC_TEXT)
    return (name, T.TEXT_SECONDARY)


class HomeView(ctk.CTkFrame):
    def __init__(self, master, on_start: Callable[[Path, bool, bool], None]):
        super().__init__(master, fg_color=T.BG_PRIMARY, corner_radius=0)
        self._on_start = on_start
        self._selected_file:    Optional[Path] = None
        self._selected_subject: Optional[str]  = None
        self._selected_type:    Optional[str]  = None

        self._subject_rows:  List[ctk.CTkFrame] = []
        self._subject_names: List[str]          = []
        self._type_btns:     List[ctk.CTkFrame] = []
        self._file_rows:     List[ctk.CTkFrame] = []
        self._file_paths:    List[Path]         = []

        self._shuffle_var         = ctk.BooleanVar(value=False)
        self._shuffle_choices_var = ctk.BooleanVar(value=False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self._build_topbar()
        self._build_body()
        self._build_statusbar()

    # ── Topbar ────────────────────────────────────────────────────────────────

    def _build_topbar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=52)
        bar.grid(row=0, column=0, sticky="ew")
        bar.columnconfigure(1, weight=1)
        bar.grid_propagate(False)

        ctk.CTkLabel(
            bar, text="exam kit",
            font=T.FONT_HEADING, text_color=T.TEXT_PRIMARY,
        ).grid(row=0, column=0, padx=20, pady=14, sticky="w")

        ctk.CTkLabel(
            bar, text="Chọn môn → loại bài → bộ đề rồi bắt đầu",
            font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY,
        ).grid(row=0, column=1, pady=14, sticky="w")

        # Nút reload nhỏ bên phải
        ctk.CTkButton(
            bar, text="↻", command=self._reload_all,
            fg_color="transparent", hover_color=T.BG_HOVER,
            text_color=T.TEXT_TERTIARY, font=T.FONT_BODY,
            width=32, height=32, corner_radius=6, border_width=0,
        ).grid(row=0, column=2, padx=(0, 16), pady=10)

    # ── Body 3 cột ────────────────────────────────────────────────────────────

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=T.BG_PRIMARY, corner_radius=0)
        body.grid(row=1, column=0, sticky="nsew")
        body.columnconfigure(0, weight=2, minsize=180)
        body.columnconfigure(1, weight=1, minsize=1)   # divider
        body.columnconfigure(2, weight=3, minsize=220)
        body.columnconfigure(3, weight=1, minsize=1)   # divider
        body.columnconfigure(4, weight=2, minsize=180)
        body.rowconfigure(0, weight=1)

        self._build_subject_panel(body, col=0)

        # Vertical divider 1
        ctk.CTkFrame(body, width=1, fg_color=T.BORDER_SUBTLE, corner_radius=0
                     ).grid(row=0, column=1, sticky="ns")

        self._build_file_panel(body, col=2)

        # Vertical divider 2
        ctk.CTkFrame(body, width=1, fg_color=T.BORDER_SUBTLE, corner_radius=0
                     ).grid(row=0, column=3, sticky="ns")

        self._build_config_panel(body, col=4)

    # ── Panel trái: Môn học ───────────────────────────────────────────────────

    def _build_subject_panel(self, parent, col: int):
        panel = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
        panel.grid(row=0, column=col, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)

        SectionLabel(panel, text="Môn học").grid(
            row=0, column=0, padx=16, pady=(18, 10), sticky="w"
        )

        self._subject_scroll = ctk.CTkScrollableFrame(
            panel, fg_color="transparent", corner_radius=0,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._subject_scroll.grid(row=1, column=0, sticky="nsew")
        self._subject_scroll.columnconfigure(0, weight=1)

        self._reload_subjects()

    # ── Panel giữa: Loại + File ───────────────────────────────────────────────

    def _build_file_panel(self, parent, col: int):
        panel = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
        panel.grid(row=0, column=col, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(3, weight=1)

        # Loại bài
        SectionLabel(panel, text="Loại bài").grid(
            row=0, column=0, padx=16, pady=(18, 10), sticky="w"
        )

        self._type_frame = ctk.CTkFrame(panel, fg_color="transparent")
        self._type_frame.grid(row=1, column=0, sticky="ew", padx=14, pady=(0, 14))
        self._type_frame.columnconfigure(0, weight=1)
        self._type_frame.columnconfigure(1, weight=1)
        self._render_type_placeholder()

        Divider(panel).grid(row=2, column=0, sticky="ew", padx=0)

        # Bộ đề
        SectionLabel(panel, text="Bộ đề").grid(
            row=2, column=0, padx=16, pady=(14, 10), sticky="w"
        )

        self._file_scroll = ctk.CTkScrollableFrame(
            panel, fg_color="transparent", corner_radius=0,
            scrollbar_button_color=T.BG_CARD,
            scrollbar_button_hover_color=T.BTN_PRIMARY,
        )
        self._file_scroll.grid(row=3, column=0, sticky="nsew")
        self._file_scroll.columnconfigure(0, weight=1)

        self._render_file_placeholder("Chọn môn học và loại bài trước")

    # ── Panel phải: Cấu hình + Start ─────────────────────────────────────────

    def _build_config_panel(self, parent, col: int):
        panel = ctk.CTkFrame(parent, fg_color="transparent", corner_radius=0)
        panel.grid(row=0, column=col, sticky="nsew")
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(8, weight=1)

        SectionLabel(panel, text="Đang chọn").grid(
            row=0, column=0, padx=16, pady=(18, 10), sticky="w"
        )

        # Card bài đang chọn
        self._info_card = ctk.CTkFrame(
            panel, fg_color=T.BG_CARD, corner_radius=T.CORNER_RADIUS,
        )
        self._info_card.grid(row=1, column=0, sticky="ew", padx=14, pady=(0, 16))
        self._info_card.columnconfigure(0, weight=1)

        self._info_title_lbl = ctk.CTkLabel(
            self._info_card, text="Chưa chọn",
            font=T.FONT_BODY_BOLD, text_color=T.TEXT_TERTIARY,
            wraplength=170, justify="left", anchor="w",
        )
        self._info_title_lbl.grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")

        self._info_sub_lbl = ctk.CTkLabel(
            self._info_card, text="",
            font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
            anchor="w",
        )
        self._info_sub_lbl.grid(row=1, column=0, padx=12, pady=(0, 4), sticky="w")

        self._info_badge = ctk.CTkLabel(
            self._info_card, text="",
            font=T.FONT_TINY_BOLD,
            fg_color="transparent", text_color=T.TEXT_TERTIARY,
            corner_radius=4,
        )
        self._info_badge.grid(row=2, column=0, padx=12, pady=(0, 12), sticky="w")

        Divider(panel).grid(row=2, column=0, sticky="ew", padx=0)

        SectionLabel(panel, text="Tùy chọn").grid(
            row=3, column=0, padx=16, pady=(14, 10), sticky="w"
        )

        # Toggle: xáo trộn câu
        self._build_toggle_row(panel, row=4, label="Xáo trộn câu hỏi", var=self._shuffle_var)
        # Toggle: xáo trộn đáp án
        self._build_toggle_row(panel, row=5, label="Xáo trộn đáp án", var=self._shuffle_choices_var)

        # Spacer
        ctk.CTkFrame(panel, fg_color="transparent", height=1).grid(row=8, column=0)

        # Nút bắt đầu
        self._start_btn = ctk.CTkButton(
            panel,
            text="Bắt đầu làm bài",
            command=self._on_start_click,
            font=T.FONT_BODY_BOLD,
            fg_color=T.BG_CARD,
            hover_color=T.BG_HOVER,
            text_color=T.TEXT_TERTIARY,
            corner_radius=T.BTN_CORNER,
            height=44,
            border_width=1,
            border_color=T.BORDER_SUBTLE,
            state="disabled",
        )
        self._start_btn.grid(row=9, column=0, padx=14, pady=(0, 16), sticky="ew")

    def _build_toggle_row(self, parent, row: int, label: str, var: ctk.BooleanVar):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=0, sticky="ew", padx=14, pady=3)
        frame.columnconfigure(0, weight=1)

        ctk.CTkLabel(
            frame, text=label,
            font=T.FONT_SMALL, text_color=T.TEXT_SECONDARY,
        ).grid(row=0, column=0, sticky="w")

        ctk.CTkSwitch(
            frame, text="", variable=var,
            width=40, height=20,
            fg_color=T.BORDER_DEFAULT,
            progress_color=T.BTN_PRIMARY,
            button_color="#ffffff",
            button_hover_color="#dddddd",
        ).grid(row=0, column=1)

    # ── Status bar ────────────────────────────────────────────────────────────

    def _build_statusbar(self):
        bar = ctk.CTkFrame(self, fg_color=T.BG_SECONDARY, corner_radius=0, height=28)
        bar.grid(row=2, column=0, sticky="ew")
        ctk.CTkLabel(
            bar, text="github.com/dolong226/exam-kit",
            font=T.FONT_TINY, text_color=T.TEXT_TERTIARY,
        ).pack(side="right", padx=16, pady=5)

    # ── Render helpers ────────────────────────────────────────────────────────

    def _reload_subjects(self):
        for w in self._subject_scroll.winfo_children():
            w.destroy()
        self._subject_rows  = []
        self._subject_names = []

        subjects = _scan_subjects()
        if not subjects:
            ctk.CTkLabel(
                self._subject_scroll,
                text="Không tìm thấy môn học.\nHãy tạo folder trong testbanks/",
                font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY,
                justify="left",
            ).pack(padx=16, pady=20, anchor="w")
            return

        for i, name in enumerate(subjects):
            color_pair = T.AVATAR_COLORS[i % len(T.AVATAR_COLORS)]
            try:
                types = _scan_types(name)
                total = sum(len(_scan_files(name, t)) for t in types)
            except Exception:
                total = 0

            row = ctk.CTkFrame(
                self._subject_scroll,
                fg_color="transparent", corner_radius=8, cursor="hand2",
            )
            row.pack(fill="x", padx=8, pady=2)
            row.columnconfigure(1, weight=1)

            avatar = SubjectAvatar(row, initial=name[0], color_pair=color_pair)
            avatar.grid(row=0, column=0, padx=(10, 8), pady=8)

            name_lbl = ctk.CTkLabel(
                row, text=name,
                font=T.FONT_SMALL, text_color=T.TEXT_PRIMARY, anchor="w",
            )
            name_lbl.grid(row=0, column=1, sticky="w")

            count_lbl = ctk.CTkLabel(
                row, text=f" {total} ",
                font=T.FONT_TINY,
                text_color=T.TEXT_TERTIARY,
                fg_color=T.BG_CARD, corner_radius=4,
            )
            count_lbl.grid(row=0, column=2, padx=(0, 10))

            def _mk(n=name, r=row):
                def _click(_=None): self._select_subject(n, r)
                return _click
            fn = _mk()
            for w in (row, avatar, name_lbl, count_lbl):
                w.bind("<Button-1>", fn)

            self._subject_rows.append(row)
            self._subject_names.append(name)

    def _render_type_placeholder(self):
        for w in self._type_frame.winfo_children():
            w.destroy()
        self._type_btns = []
        ctk.CTkLabel(
            self._type_frame, text="Chọn môn học trước",
            font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY,
        ).grid(row=0, column=0, columnspan=2, padx=4, pady=4, sticky="w")

    def _render_types(self, types: List[str]):
        for w in self._type_frame.winfo_children():
            w.destroy()
        self._type_btns = []

        if not types:
            ctk.CTkLabel(
                self._type_frame, text="Không có loại bài nào",
                font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY,
            ).grid(row=0, column=0, padx=4, pady=4, sticky="w")
            return

        for col, name in enumerate(types):
            label, _ = _type_display(name)

            btn = ctk.CTkButton(
                self._type_frame,
                text=label,
                font=T.FONT_SMALL_BOLD,
                text_color=T.TEXT_SECONDARY,
                fg_color=T.BG_CARD,
                hover_color=T.BG_HOVER,
                corner_radius=T.BTN_CORNER,
                height=36,
                border_width=1,
                border_color=T.BORDER_SUBTLE,
                command=lambda n=name: self._select_type(n),
            )
            pad = (0, 6) if col == 0 else (6, 0)
            btn.grid(row=0, column=col, padx=pad, sticky="ew")
            self._type_btns.append(btn)

    def _render_file_placeholder(self, msg: str):
        for w in self._file_scroll.winfo_children():
            w.destroy()
        self._file_rows  = []
        self._file_paths = []
        ctk.CTkLabel(
            self._file_scroll, text=msg,
            font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY,
        ).pack(padx=16, pady=20, anchor="w")

    def _render_files(self, files: List[Path]):
        for w in self._file_scroll.winfo_children():
            w.destroy()
        self._file_rows  = []
        self._file_paths = list(files)

        if not files:
            ctk.CTkLabel(
                self._file_scroll,
                text="Không có file nào.\nHãy thêm file .md / .yaml vào folder.",
                font=T.FONT_SMALL, text_color=T.TEXT_TERTIARY,
            ).pack(padx=16, pady=20, anchor="w")
            return

        for i, fpath in enumerate(files):
            try:
                from studykit.core.parser import parse_testbank
                tb    = parse_testbank(fpath)
                count = len(tb.questions)
                mode  = detect_mode_from_path(fpath)
                mode_str = (
                    "trắc nghiệm" if mode and "MULTIPLE" in mode.value.upper()
                    else ("tự luận" if mode else "hỗn hợp")
                )
                sub = f"{count} câu · {mode_str}"
                title = tb.title
            except Exception:
                sub   = ""
                title = fpath.stem

            row = ctk.CTkFrame(
                self._file_scroll,
                fg_color="transparent", corner_radius=8, cursor="hand2",
            )
            row.pack(fill="x", padx=8, pady=2)
            row.columnconfigure(0, weight=1)

            title_lbl = ctk.CTkLabel(
                row, text=title,
                font=T.FONT_SMALL_BOLD, text_color=T.TEXT_PRIMARY, anchor="w",
            )
            title_lbl.grid(row=0, column=0, padx=12, pady=(9, 1), sticky="w")

            sub_lbl = ctk.CTkLabel(
                row, text=sub,
                font=T.FONT_TINY, text_color=T.TEXT_TERTIARY, anchor="w",
            )
            sub_lbl.grid(row=1, column=0, padx=12, pady=(0, 9), sticky="w")

            def _mk(p=fpath, idx=i, r=row):
                def _click(_=None): self._select_file(p, idx, r)
                return _click
            fn = _mk()
            for w in (row, title_lbl, sub_lbl):
                w.bind("<Button-1>", fn)

            self._file_rows.append(row)

    # ── Selection logic ───────────────────────────────────────────────────────

    def _select_subject(self, name: str, row_frame: ctk.CTkFrame):
        self._selected_subject = name
        self._selected_type    = None
        self._selected_file    = None

        for r in self._subject_rows:
            r.configure(fg_color="transparent")
        row_frame.configure(fg_color=T.BG_SELECTED)

        self._render_types(_scan_types(name))
        self._render_file_placeholder("Chọn loại bài trước")
        self._reset_info_card()
        self._set_start_disabled()

    def _select_type(self, name: str):
        self._selected_type  = name
        self._selected_file  = None

        for btn in self._type_btns:
            btn.configure(
                fg_color=T.BG_CARD,
                border_color=T.BORDER_SUBTLE,
                text_color=T.TEXT_SECONDARY,
            )
        for btn in self._type_btns:
            label, _ = _type_display(name)
            if btn.cget("text") == label:
                btn.configure(
                    fg_color=T.BG_SELECTED,
                    border_color=T.BTN_PRIMARY,
                    text_color=T.TEXT_ACCENT,
                )
                break

        self._render_files(_scan_files(self._selected_subject, name))
        self._reset_info_card()
        self._set_start_disabled()

    def _select_file(self, fpath: Path, idx: int, row_frame: ctk.CTkFrame):
        self._selected_file = fpath

        for r in self._file_rows:
            r.configure(fg_color="transparent")
        row_frame.configure(fg_color=T.BG_SELECTED)

        self._update_info_card(fpath)
        self._set_start_active()

    # ── Info card ─────────────────────────────────────────────────────────────

    def _update_info_card(self, fpath: Path):
        try:
            from studykit.core.parser import parse_testbank
            tb    = parse_testbank(fpath)
            count = len(tb.questions)
            mode  = detect_mode_from_path(fpath)
            is_essay = mode and "ESSAY" in mode.value.upper()
            mode_label = "Tự luận" if is_essay else "Trắc nghiệm"
            badge_bg   = T.TAG_ESSAY_BG   if is_essay else T.TAG_MC_BG
            badge_fg   = T.TAG_ESSAY_TEXT if is_essay else T.TAG_MC_TEXT
            sub = f"{self._selected_subject or ''} · {count} câu"
            self._info_title_lbl.configure(text=tb.title, text_color=T.TEXT_PRIMARY)
            self._info_sub_lbl.configure(text=sub, text_color=T.TEXT_TERTIARY)
            self._info_badge.configure(
                text=f"  {mode_label.upper()}  ",
                fg_color=badge_bg, text_color=badge_fg,
            )
        except Exception:
            self._info_title_lbl.configure(text=fpath.stem, text_color=T.TEXT_PRIMARY)
            self._info_sub_lbl.configure(text="", text_color=T.TEXT_TERTIARY)
            self._info_badge.configure(text="", fg_color="transparent")

    def _reset_info_card(self):
        self._info_title_lbl.configure(text="Chưa chọn", text_color=T.TEXT_TERTIARY)
        self._info_sub_lbl.configure(text="")
        self._info_badge.configure(text="", fg_color="transparent")

    # ── Start button states ───────────────────────────────────────────────────

    def _set_start_disabled(self):
        self._start_btn.configure(
            fg_color=T.BG_CARD,
            hover_color=T.BG_CARD,
            text_color=T.TEXT_TERTIARY,
            border_color=T.BORDER_SUBTLE,
        )
        self._start_btn.configure(state="disabled")

    def _set_start_active(self):
        # Phải set state="normal" TRƯỚC rồi mới set màu,
        # vì CTK bỏ qua fg_color khi widget đang disabled.
        self._start_btn.configure(state="normal")
        self._start_btn.configure(
            fg_color=T.BTN_PRIMARY,
            hover_color=T.BTN_PRIMARY_HOVER,
            text_color=T.BTN_PRIMARY_TEXT,
            border_color="transparent",
        )

    def _reload_all(self):
        self._selected_subject = None
        self._selected_type    = None
        self._selected_file    = None
        self._reload_subjects()
        self._render_type_placeholder()
        self._render_file_placeholder("Chọn môn học và loại bài trước")
        self._reset_info_card()
        self._set_start_disabled()

    def _on_start_click(self):
        if not self._selected_file:
            return
        self._on_start(
            self._selected_file,
            self._shuffle_var.get(),
            self._shuffle_choices_var.get(),
        )