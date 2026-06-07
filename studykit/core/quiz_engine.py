from typing import List, Optional, Union
from .models import TestBank, QuizConfig, Question, UserResponse, QuizResult, QuizMode


class QuizSession:
    """Quản lý trạng thái và logic thuần của một phiên làm bài (Session) độc lập."""
    
    def __init__(self, testbank: TestBank, config: QuizConfig):
        self.testbank = testbank
        self.config = config
        # Lọc danh sách câu hỏi (Trắc nghiệm / Tự luận)
        self.questions: List[Question] = [
            q for q in testbank.questions if q.type == config.mode
        ]
        self.current_index = 0
        self.responses: List[UserResponse] = []

    def get_next_question(self) -> Optional[Question]:
        """Lấy câu hỏi tiếp theo để hiển thị. Trả về None nếu đã hết bộ đề."""
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def submit_answer(self, user_answer: Union[int, str]) -> UserResponse:
        """Nộp câu trả lời cho câu hỏi hiện tại, chấm điểm và chuyển sang câu kế tiếp."""
        if self.current_index >= len(self.questions):
            raise IndexError("Đã hết câu hỏi trong phiên làm bài này.")

        current_q = self.questions[self.current_index]
        is_correct = False

        # --- Logic Chấm Điểm ---
        if current_q.type == QuizMode.MULTIPLE_CHOICE:
            # So sánh index số nguyên của trắc nghiệm (A=0, B=1, C=2...)
            is_correct = int(user_answer) == int(current_q.correct_answer)
            
        elif current_q.type == QuizMode.ESSAY:
            # Tự luận đơn giản: Chuẩn hóa chuỗi (bỏ khoảng trống thừa, viết thường) để so sánh thô
            # Phần này sẽ tích hợp Agent/LLM ở các phiên bản sau
            clean_user = str(user_answer).strip().lower()
            clean_correct = str(current_q.correct_answer).strip().lower()
            is_correct = clean_user == clean_correct

        # Lưu lại phản hồi của người dùng cho câu hỏi này
        response = UserResponse(
            question_id=current_q.id,
            question_content=current_q.content,
            user_answer=str(user_answer),
            correct_answer=str(current_q.correct_answer),
            is_correct=is_correct,
            explanation=current_q.explanation
        )
        
        self.responses.append(response)
        self.current_index += 1  # Tịnh tiến sang câu hỏi tiếp theo
        return response

    def get_result(self) -> QuizResult:
        """Tính toán kết quả tổng thể sau khi hoàn thành lượt làm bài."""
        total = len(self.questions)
        correct_count = sum(1 for r in self.responses if r.is_correct)
        wrong_responses = [r for r in self.responses if not r.is_correct]
        
        return QuizResult(
            total_questions=total,
            correct_count=correct_count,
            score_string=f"{correct_count}/{total}",
            wrong_responses=wrong_responses
        )