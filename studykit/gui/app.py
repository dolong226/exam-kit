"""
GUI App — Entry point và Navigation controller.
Quản lý việc chuyển đổi giữa HomeView → QuizView → ResultView.
"""

import customtkinter as ctk
from pathlib import Path
from typing import Optional

from core.models import QuizConfig, QuizMode
from core.parser import parse_testbank
from core.quiz_engine import QuizSession
from . import theme as T
from .home_view import HomeView
from .quiz_view import QuizView
from .result_view import ResultView


def launch_gui() -> None:
    """Hàm duy nhất được gọi từ main.py để khởi động GUI."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = ExamKitApp()
    app.mainloop()


class ExamKitApp(ctk.CTk):
    """
    Cửa sổ chính của ứng dụng.
    Hoạt động như một navigation stack đơn giản: chỉ có 1 view hiển thị tại một thời điểm.
    """

    def __init__(self):
        super().__init__()
        self.title("Exam Kit")
        self.geometry(f"{T.WINDOW_WIDTH}x{T.WINDOW_HEIGHT}")
        self.minsize(T.WINDOW_MIN_WIDTH, T.WINDOW_MIN_HEIGHT)
        self.configure(fg_color=T.BG_PRIMARY)

        # State lưu lại testbank/config để hỗ trợ "Làm lại"
        self._last_file: Optional[Path] = None
        self._last_mode: Optional[str] = None
        self._last_immediate: bool = False

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
        view = HomeView(self, on_start=self._start_quiz)
        view.grid(row=0, column=0, sticky="nsew")
        self._current_view = view

    def _start_quiz(self, file_path: Path, mode: str, show_immediately: bool):
        """Được gọi từ HomeView khi user bấm Bắt đầu."""
        # Lưu lại để hỗ trợ retry
        self._last_file = file_path
        self._last_mode = mode
        self._last_immediate = show_immediately

        # Parse testbank
        try:
            testbank = parse_testbank(file_path)
        except Exception as e:
            self._show_error(f"Lỗi nạp bộ đề:\n{e}")
            return

        # Tạo config & session
        try:
            quiz_mode = QuizMode(mode)
        except ValueError:
            self._show_error(f"Chế độ không hợp lệ: {mode}")
            return

        config = QuizConfig(mode=quiz_mode, show_explanation_immediately=show_immediately)
        session = QuizSession(testbank, config)

        if not session.questions:
            self._show_error(
                f'Không có câu hỏi nào cho chế độ "{quiz_mode.value}" trong bộ đề này.\n'
                'Hãy chọn chế độ khác hoặc thêm câu hỏi vào file testbank.'
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
        """Được gọi từ QuizView khi user hoàn thành hết câu hỏi."""
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
        """Làm lại quiz với cùng cấu hình cũ."""
        if self._last_file and self._last_mode:
            self._start_quiz(self._last_file, self._last_mode, self._last_immediate)
        else:
            self._show_home()

    def _show_error(self, message: str):
        """Hiển thị dialog lỗi."""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Lỗi")
        dialog.geometry("420x200")
        dialog.resizable(False, False)
        dialog.configure(fg_color=T.BG_SECONDARY)
        dialog.grab_set()
        dialog.focus()

        ctk.CTkLabel(
            dialog,
            text="Đã xảy ra lỗi",
            font=T.FONT_HEADING,
            text_color=T.TEXT_ERROR,
        ).pack(pady=(20, 8))

        ctk.CTkLabel(
            dialog,
            text=message,
            font=T.FONT_BODY,
            text_color=T.TEXT_PRIMARY,
            wraplength=380,
            justify="center",
        ).pack(padx=20)

        ctk.CTkButton(
            dialog,
            text="Đóng",
            command=dialog.destroy,
            fg_color=T.BTN_PRIMARY,
            hover_color=T.BTN_PRIMARY_HOVER,
            corner_radius=T.BTN_CORNER,
            width=100,
            height=T.BTN_HEIGHT_SM,
        ).pack(pady=16)