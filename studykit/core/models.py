from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field


class QuizMode(str, Enum):
    """Chế độ học tập/làm bài."""
    MULTIPLE_CHOICE = "multiple_choice"  # Trắc nghiệm
    ESSAY = "essay"                      # Tự luận


class Question(BaseModel):
    """Định nghĩa cấu trúc của một câu hỏi lẻ."""
    id: str = Field(..., description="ID duy nhất của câu hỏi (dùng để tracking)")
    type: QuizMode = Field(default=QuizMode.MULTIPLE_CHOICE, description="Loại câu hỏi")
    content: str = Field(..., description="Nội dung/đề bài câu hỏi")
    
    # Chỉ dùng cho trắc nghiệm (MULTIPLE_CHOICE)
    choices: Optional[List[str]] = Field(
        default=None, 
        description="Danh sách các phương án lựa chọn (A, B, C, D...)"
    )
    
    # Lưu index của câu trả lời đúng (0, 1, 2, 3...) đối với trắc  nghiệm
    #Lưu nội dung/đáp án mẫu để so sánh hoặc đưa cho LLM chấm đối với tự luận
    correct_answer: Union[int, str] = Field(
        ..., 
        description="Đáp án đúng (Index số nguyên với trắc nghiệm, hoặc text mẫu với tự luận)"
    )
    
    explanation: Optional[str] = Field(
        default=None, 
        description="Giải thích chi tiết lý do chọn đáp án này hoặc hướng dẫn giải"
    )


class TestBank(BaseModel):
    """Cấu trúc của cả một file test bank được import vào."""
    title: str = Field(default="Bộ câu hỏi học tập", description="Tiêu đề của bộ đề")
    description: Optional[str] = Field(default=None, description="Mô tả ngắn gọn về bộ đề")
    questions: List[Question] = Field(
        default_factory=list, 
        description="Danh sách các câu hỏi thuộc test bank này"
    )


class QuizConfig(BaseModel):
    """Cấu hình cho một phiên (session) làm quiz."""
    mode: QuizMode = Field(..., description="Chế độ muốn làm: trắc nghiệm hoặc tự luận")
    show_explanation_immediately: bool = Field(
        default=False, 
        description="True: Hiện ngay đáp án/giải thích sau khi chọn. False: Đợi làm xong hết mới hiện"
    )


class UserResponse(BaseModel):
    """Lưu trữ câu trả lời chi tiết của người dùng cho từng câu hỏi."""
    question_id: str = Field(..., description="Liên kết với ID của câu hỏi")
    question_content: str = Field(..., description="Lưu lại nội dung câu hỏi để tiện hiển thị/xuất file")
    user_answer: str = Field(..., description="Câu trả lời của user (Index lựa chọn hoặc text tự luận)")
    correct_answer: str = Field(..., description="Đáp án đúng để đối chiếu")
    is_correct: bool = Field(..., description="Đúng hay Sai")
    explanation: Optional[str] = Field(default=None, description="Giải thích đi kèm của câu hỏi đó")
    ai_feedback: Optional[str] = Field(
        default=None, 
        description="Nhận xét chi tiết từ Agent/LLM (chỉ dùng cho phần tự luận)"
    )


class QuizResult(BaseModel):
    """Kết quả tổng thể sau khi hoàn thành phiên làm bài."""
    total_questions: int = Field(..., description="Tổng số câu hỏi đã làm")
    correct_count: int = Field(..., description="Số câu trả lời đúng")
    score_string: str = Field(
        ..., 
        description="Chuỗi hiển thị điểm định dạng (Ví dụ: '21/30')"
    )
    wrong_responses: List[UserResponse] = Field(
        default_factory=list, 
        description="Danh sách các câu làm sai (dùng để xuất file CLI hoặc hiển thị lên GUI)"
    )