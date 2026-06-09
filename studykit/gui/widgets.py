"""
Các widget tái sử dụng cho toàn bộ GUI.
Thiết kế mới: tối giản, typography rõ ràng, ChoiceButton tự expand theo text.
"""

import customtkinter as ctk
from typing import Callable, Optional
from . import theme as T


class AppButton(ctk.CTkButton):
    """Nút bấm chuẩn với các style: primary / secondary / neutral / success / danger."""

    STYLES = {
        "primary": {
            "fg_color": T.BTN_PRIMARY,
            "hover_color": T.BTN_PRIMARY_HOVER,
            "text_color": T.BTN_PRIMARY_TEXT,
            "border_width": 0,
        },
        "secondary": {
            "fg_color": T.BTN_SECONDARY,
            "hover_color": T.BTN_SECONDARY_HOVER,
            "text_color": T.BTN_SECONDARY_TEXT,
            "border_width": 1,
            "border_color": T.BORDER_DEFAULT,
        },
        "neutral": {
            "fg_color": T.BTN_NEUTRAL,
            "hover_color": T.BTN_NEUTRAL_HOVER,
            "text_color": T.BTN_NEUTRAL_TEXT,
            "border_width": 1,
            "border_color": T.BORDER_SUBTLE,
        },
        "success": {
            "fg_color": T.BTN_SUCCESS,
            "hover_color": "#1f3d2e",
            "text_color": T.BTN_SUCCESS_TEXT,
            "border_width": 0,
        },
        "danger": {
            "fg_color": T.BTN_DANGER,
            "hover_color": T.BTN_DANGER_HOVER,
            "text_color": T.BTN_DANGER_TEXT,
            "border_width": 0,
        },
    }

    def __init__(
        self,
        master,
        text: str,
        command: Optional[Callable] = None,
        style: str = "primary",
        width: int = 140,
        height: int = T.BTN_HEIGHT,
        font=None,
        **kwargs,
    ):
        s = self.STYLES.get(style, self.STYLES["primary"])
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=height,
            corner_radius=T.BTN_CORNER,
            font=font or T.FONT_BODY_BOLD,
            **s,
            **kwargs,
        )


class Card(ctk.CTkFrame):
    """Frame dạng card với bo góc nhất quán."""

    def __init__(self, master, color: str = T.BG_CARD, **kwargs):
        super().__init__(
            master,
            fg_color=color,
            corner_radius=T.CORNER_RADIUS,
            **kwargs,
        )


class SectionLabel(ctk.CTkLabel):
    """Label tiêu đề section — dạng uppercase nhỏ."""

    def __init__(self, master, text: str, **kwargs):
        super().__init__(
            master,
            text=text.upper(),
            font=T.FONT_TINY_BOLD,
            text_color=T.TEXT_TERTIARY,
            **kwargs,
        )


class BodyLabel(ctk.CTkLabel):
    """Label nội dung thông thường."""

    def __init__(self, master, text: str, secondary: bool = False, **kwargs):
        super().__init__(
            master,
            text=text,
            font=T.FONT_BODY,
            text_color=T.TEXT_SECONDARY if secondary else T.TEXT_PRIMARY,
            **kwargs,
        )


class ProgressBar(ctk.CTkProgressBar):
    """Thanh tiến trình mỏng."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            height=T.PROGRESS_HEIGHT,
            corner_radius=2,
            fg_color=T.BG_CARD,
            progress_color=T.BTN_PRIMARY,
            **kwargs,
        )


class Divider(ctk.CTkFrame):
    """Đường kẻ ngang phân cách."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            height=1,
            fg_color=T.BORDER_SUBTLE,
            corner_radius=0,
            **kwargs,
        )


class ScoreChip(ctk.CTkLabel):
    """Badge hiển thị điểm đúng ở topbar."""

    def __init__(self, master, score_str: str = "0/0", **kwargs):
        super().__init__(
            master,
            text=f"  {score_str}  ",
            font=T.FONT_TINY_BOLD,
            text_color=T.TEXT_SECONDARY,
            fg_color=T.BG_CARD,
            corner_radius=6,
            **kwargs,
        )

    def update_score(self, correct: int, total: int):
        self.configure(
            text=f"  ✓ {correct}/{total}  ",
            text_color=T.TEXT_SUCCESS if correct > 0 else T.TEXT_SECONDARY,
        )


class ModeTag(ctk.CTkLabel):
    """Tag nhỏ hiển thị chế độ: TRẮC NGHIỆM / TỰ LUẬN."""

    def __init__(self, master, mode: str = "mc", **kwargs):
        is_essay = mode.lower() in ("essay", "tự luận", "tu luan")
        bg = T.TAG_ESSAY_BG if is_essay else T.TAG_MC_BG
        fg = T.TAG_ESSAY_TEXT if is_essay else T.TAG_MC_TEXT
        label = "TỰ LUẬN" if is_essay else "TRẮC NGHIỆM"
        super().__init__(
            master,
            text=f"  {label}  ",
            font=T.FONT_TINY_BOLD,
            text_color=fg,
            fg_color=bg,
            corner_radius=4,
            **kwargs,
        )


class ExplanationBox(ctk.CTkTextbox):
    """Hộp giải thích read-only."""

    def __init__(self, master, text: str, **kwargs):
        super().__init__(
            master,
            font=T.FONT_MONO,
            fg_color=T.BG_SECONDARY,
            text_color=T.TEXT_SECONDARY,
            border_color=T.BORDER_SUBTLE,
            border_width=1,
            corner_radius=8,
            wrap="word",
            state="normal",
            **kwargs,
        )
        self.insert("0.0", text)
        self.configure(state="disabled")


class FeedbackBanner(ctk.CTkFrame):
    """
    Banner feedback sau khi trả lời MC.
    Dùng border-left accent thay vì màu nền đặc.
    """

    def __init__(self, master, is_correct: bool, **kwargs):
        accent = T.BORDER_SUCCESS if is_correct else T.BORDER_ERROR
        super().__init__(
            master,
            fg_color=T.BG_SECONDARY,
            corner_radius=8,
            border_width=0,
            **kwargs,
        )
        # Thanh accent dọc bên trái
        ctk.CTkFrame(
            self,
            width=3, fg_color=accent, corner_radius=0,
        ).pack(side="left", fill="y", padx=(0, 0))


class ChoiceButton(ctk.CTkFrame):
    """
    Nút phương án trắc nghiệm — tự expand chiều cao khi text dài.

    Dùng CTkFrame thay vì CTkButton để kiểm soát layout:
    - Letter badge cố định bên trái
    - Text wrap xuống dòng tự nhiên bên phải
    """

    def __init__(self, master, letter: str, text: str, command: Callable, **kwargs):
        self.letter = letter
        self._command = command
        self._state_name = "default"

        super().__init__(
            master,
            fg_color=T.BTN_CHOICE_DEFAULT,
            corner_radius=T.BTN_CORNER,
            border_width=1,
            border_color=T.BTN_CHOICE_DEFAULT_BORDER,
            cursor="hand2",
            **kwargs,
        )
        self.columnconfigure(1, weight=1)

        # Letter badge
        self._letter_lbl = ctk.CTkLabel(
            self,
            text=letter,
            font=T.FONT_TINY_BOLD,
            width=26, height=26,
            fg_color=T.BG_HOVER,
            corner_radius=6,
            text_color=T.TEXT_SECONDARY,
        )
        self._letter_lbl.grid(row=0, column=0, padx=(12, 10), pady=12, sticky="n")

        # Text — wraplength sẽ được set khi widget configure
        self._text_lbl = ctk.CTkLabel(
            self,
            text=text,
            font=T.FONT_CHOICE,
            text_color=T.TEXT_PRIMARY,
            anchor="w",
            justify="left",
            wraplength=580,
        )
        self._text_lbl.grid(row=0, column=1, padx=(0, 12), pady=12, sticky="ew")

        # Bind click trên toàn frame + các con
        for w in (self, self._letter_lbl, self._text_lbl):
            w.bind("<Button-1>", self._on_click)
            w.bind("<Enter>", self._on_enter)
            w.bind("<Leave>", self._on_leave)

    def _on_click(self, _=None):
        if str(self.cget("cursor")) != "hand2":
            return
        self._command()

    def _on_enter(self, _=None):
        if self._state_name == "default":
            self.configure(fg_color=T.BTN_CHOICE_HOVER)

    def _on_leave(self, _=None):
        if self._state_name == "default":
            self.configure(fg_color=T.BTN_CHOICE_DEFAULT)

    def configure(self, **kwargs):
        super().configure(**kwargs)

    def set_state(self, state: str):
        """state: 'default' | 'correct' | 'wrong'"""
        self._state_name = state
        styles = {
            "default": {
                "frame_fg":    T.BTN_CHOICE_DEFAULT,
                "frame_bd":    T.BTN_CHOICE_DEFAULT_BORDER,
                "badge_fg":    T.BG_HOVER,
                "badge_text":  T.TEXT_SECONDARY,
                "text_color":  T.TEXT_PRIMARY,
                "cursor":      "hand2",
            },
            "correct": {
                "frame_fg":    T.BTN_CHOICE_CORRECT,
                "frame_bd":    T.BTN_CHOICE_CORRECT_BORDER,
                "badge_fg":    T.BTN_CHOICE_CORRECT_BORDER,
                "badge_text":  "#ffffff",
                "text_color":  T.TEXT_SUCCESS,
                "cursor":      "arrow",
            },
            "wrong": {
                "frame_fg":    T.BTN_CHOICE_WRONG,
                "frame_bd":    T.BTN_CHOICE_WRONG_BORDER,
                "badge_fg":    T.BTN_CHOICE_WRONG_BORDER,
                "badge_text":  "#ffffff",
                "text_color":  T.TEXT_ERROR,
                "cursor":      "arrow",
            },
        }
        s = styles.get(state, styles["default"])
        super().configure(
            fg_color=s["frame_fg"],
            border_color=s["frame_bd"],
            cursor=s["cursor"],
        )
        self._letter_lbl.configure(
            fg_color=s["badge_fg"],
            text_color=s["badge_text"],
        )
        self._text_lbl.configure(text_color=s["text_color"])

    def disable(self):
        """Vô hiệu hoá tương tác sau khi đã trả lời."""
        super().configure(cursor="arrow")
        for w in (self._letter_lbl, self._text_lbl):
            w.configure(cursor="arrow")


class SubjectAvatar(ctk.CTkLabel):
    """Avatar chữ cái đầu cho môn học."""

    def __init__(self, master, initial: str, color_pair: tuple, **kwargs):
        bg, fg = color_pair
        super().__init__(
            master,
            text=initial.upper(),
            font=T.FONT_TINY_BOLD,
            fg_color=bg,
            text_color=fg,
            corner_radius=6,
            width=28,
            height=28,
            **kwargs,
        )