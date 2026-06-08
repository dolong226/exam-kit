"""
GUI App — Entry point và Navigation controller.
"""

import customtkinter as ctk
from pathlib import Path
from typing import Optional

from studykit.core.models import QuizConfig, QuizMode
from studykit.core.parser import parse_testbank, detect_mode_from_path
from studykit.core.quiz_engine import QuizSession
from . import theme as T
from .home_view import HomeView
from .quiz_view import QuizView
from .result_view import ResultView


def launch_gui() -> None:
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ExamKitApp()
    app.mainloop()


class ExamKitApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Exam Kit")
        self.geometry(f"{T.WINDOW_WIDTH}x{T.WINDOW_HEIGHT}")
        self.minsize(T.WINDOW_MIN_WIDTH, T.WINDOW_MIN_HEIGHT)
        self.configure(fg_color=T.BG_PRIMARY)

        self._last_file: Optional[Path] = None
        self._last_shuffle: bool = False
        self._last_shuffle_choices: bool = False

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self._current_view: Optional[ctk.CTkFrame] = None
        self._show_home()

    # ── Navigation ───────────────────────────────────────────────────────────

    def _clear_view(self):
        if self._current_view is not None:
            self._current_view.destroy()
            self._current_view = None

    def _show_home(self):
        self._clear_view()
        # on_start signature: (file_path, shuffle, shuffle_choices)
        view = HomeView(self, on_start=self._start_quiz)
        view.grid(row=0, column=0, sticky="nsew")
        self._current_view = view

    def _start_quiz(self, file_path: Path, shuffle: bool, shuffle_choices: bool):
        """Được gọi từ HomeView khi user bấm Bắt đầu."""
        self._last_file = file_path
        self._last_shuffle = shuffle
        self._last_shuffle_choices = shuffle_choices

        # Parse testbank (shuffle nếu cần)
        try:
            testbank = parse_testbank(file_path, shuffle=shuffle, shuffle_choices=shuffle_choices)
        except Exception as e:
            self._show_error(f"Lỗi nạp bộ đề:\n{e}")
            return

        # Tự động xác định mode từ tên folder
        quiz_mode = detect_mode_from_path(file_path)
        if quiz_mode is None:
            # Fallback: đoán từ nội dung file
            has_mc = any(q.type == QuizMode.MULTIPLE_CHOICE for q in testbank.questions)
            has_essay = any(q.type == QuizMode.ESSAY for q in testbank.questions)
            if has_mc and not has_essay:
                quiz_mode = QuizMode.MULTIPLE_CHOICE
            elif has_essay and not has_mc:
                quiz_mode = QuizMode.ESSAY
            else:
                self._show_error(
                    "Không thể xác định chế độ (Trắc nghiệm/Tự luận) từ tên folder.\n"
                    "Hãy đặt file trong folder 'Trắc nghiệm' hoặc 'Tự luận'."
                )
                return

        config = QuizConfig(mode=quiz_mode, show_explanation_immediately=False)
        session = QuizSession(testbank, config)

        if not session.questions:
            self._show_error(
                f'Không có câu hỏi nào cho chế độ "{quiz_mode.value}" trong bộ đề này.\n'
                'Hãy kiểm tra lại file hoặc cấu trúc folder.'
            )
            return

        self._clear_view()
        view = QuizView(
            self,
            session=session,
            on_finish=self._show_result,
            on_back=self._show_home,
        )
        view.grid(row=0, column=0, sticky="nsew")
        self._current_view = view

    def _show_result(self, session: QuizSession):
        self._clear_view()
        view = ResultView(
            self,
            session=session,
            on_home=self._show_home,
            on_retry=self._retry_quiz,
        )
        view.grid(row=0, column=0, sticky="nsew")
        self._current_view = view

    def _retry_quiz(self):
        if self._last_file:
            self._start_quiz(self._last_file, self._last_shuffle, self._last_shuffle_choices)
        else:
            self._show_home()

    def _show_error(self, message: str):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Lỗi")
        dialog.geometry("420x200")
        dialog.resizable(False, False)
        dialog.configure(fg_color=T.BG_SECONDARY)
        dialog.grab_set()
        dialog.focus()

        ctk.CTkLabel(
            dialog, text="Đã xảy ra lỗi",
            font=T.FONT_HEADING, text_color=T.TEXT_ERROR,
        ).pack(pady=(20, 8))

        ctk.CTkLabel(
            dialog, text=message,
            font=T.FONT_BODY, text_color=T.TEXT_PRIMARY,
            wraplength=380, justify="center",
        ).pack(padx=20)

        AppButton = ctk.CTkButton
        ctk.CTkButton(
            dialog, text="Đóng", command=dialog.destroy,
            fg_color=T.BTN_PRIMARY, hover_color=T.BTN_PRIMARY_HOVER,
            corner_radius=T.BTN_CORNER, width=100, height=T.BTN_HEIGHT_SM,
        ).pack(pady=16)