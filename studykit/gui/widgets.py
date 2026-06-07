"""
Các widget tái sử dụng cho toàn bộ GUI.
Tất cả đều kế thừa CustomTkinter và áp dụng theme thống nhất.
"""

import customtkinter as ctk
from typing import Callable, Optional
from . import theme as T


class AppButton(ctk.CTkButton):
    """Nút bấm chuẩn với 3 kiểu: primary / secondary / neutral."""

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
            "border_color": T.BORDER_DEFAULT,
        },
        "success": {
            "fg_color": T.BTN_SUCCESS,
            "hover_color": "#3ab890",
            "text_color": T.BTN_SUCCESS_TEXT,
            "border_width": 0,
        },
        "danger": {
            "fg_color": T.BTN_PRIMARY,
            "hover_color": T.BTN_PRIMARY_HOVER,
            "text_color": "#ffffff",
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
    """Frame dạng card với bo góc và màu nền card."""

    def __init__(self, master, color: str = T.BG_SECONDARY, **kwargs):
        super().__init__(
            master,
            fg_color=color,
            corner_radius=T.CORNER_RADIUS,
            **kwargs,
        )


class SectionLabel(ctk.CTkLabel):
    """Label tiêu đề section."""

    def __init__(self, master, text: str, **kwargs):
        super().__init__(
            master,
            text=text,
            font=T.FONT_HEADING,
            text_color=T.TEXT_ACCENT,
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
    """Thanh tiến trình có màu accent."""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            height=T.PROGRESS_HEIGHT,
            corner_radius=3,
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
            fg_color=T.BORDER_DEFAULT,
            corner_radius=0,
            **kwargs,
        )


class ScoreChip(ctk.CTkLabel):
    """Badge hiển thị điểm ở góc màn hình quiz."""

    def __init__(self, master, score_str: str = "0/0", **kwargs):
        super().__init__(
            master,
            text=f"  {score_str}  ",
            font=T.FONT_SMALL_BOLD,
            text_color=T.TEXT_SECONDARY,
            fg_color=T.BG_CARD,
            corner_radius=6,
            **kwargs,
        )

    def update_score(self, correct: int, total: int):
        self.configure(text=f"  ✓ {correct}/{total}  ")


class ExplanationBox(ctk.CTkTextbox):
    """Hộp hiển thị giải thích (read-only)."""

    def __init__(self, master, text: str, **kwargs):
        super().__init__(
            master,
            font=T.FONT_MONO,
            fg_color=T.BG_PRIMARY,
            text_color=T.TEXT_PRIMARY,
            border_color=T.BORDER_DEFAULT,
            border_width=1,
            corner_radius=8,
            wrap="word",
            state="normal",
            **kwargs,
        )
        self.insert("0.0", text)
        self.configure(state="disabled")


class ChoiceButton(ctk.CTkButton):
    """
    Nút phương án trắc nghiệm.
    Có 4 trạng thái: default / selected / correct / wrong.
    """

    def __init__(self, master, letter: str, text: str, command: Callable, **kwargs):
        self.letter = letter
        self._state = "default"
        super().__init__(
            master,
            text=f"  {letter}.  {text}",
            command=command,
            height=T.CHOICE_BTN_HEIGHT,
            corner_radius=T.BTN_CORNER,
            font=T.FONT_CHOICE,
            anchor="w",
            fg_color=T.BTN_CHOICE_DEFAULT,
            hover_color=T.BTN_CHOICE_HOVER,
            text_color=T.TEXT_PRIMARY,
            border_width=1,
            border_color=T.BTN_CHOICE_DEFAULT_BORDER,
            **kwargs,
        )

    def set_state(self, state: str):
        """state: 'default' | 'selected' | 'correct' | 'wrong'"""
        self._state = state
        styles = {
            "default": {
                "fg_color": T.BTN_CHOICE_DEFAULT,
                "border_color": T.BTN_CHOICE_DEFAULT_BORDER,
                "text_color": T.TEXT_PRIMARY,
                "hover_color": T.BTN_CHOICE_HOVER,
            },
            "selected": {
                "fg_color": T.BTN_CHOICE_SELECTED,
                "border_color": T.BORDER_ACCENT,
                "text_color": "#ffffff",
                "hover_color": T.BTN_CHOICE_SELECTED,
            },
            "correct": {
                "fg_color": T.BTN_CHOICE_CORRECT,
                "border_color": T.BTN_CHOICE_CORRECT_BORDER,
                "text_color": T.TEXT_SUCCESS,
                "hover_color": T.BTN_CHOICE_CORRECT,
            },
            "wrong": {
                "fg_color": T.BTN_CHOICE_WRONG,
                "border_color": T.BTN_CHOICE_WRONG_BORDER,
                "text_color": T.TEXT_ERROR,
                "hover_color": T.BTN_CHOICE_WRONG,
            },
        }
        s = styles.get(state, styles["default"])
        self.configure(**s)