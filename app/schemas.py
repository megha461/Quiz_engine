from pydantic import BaseModel
from typing import List


class QuizQuestion(BaseModel):

    question: str
    options: List[str]
    difficulty: str


class AnswerSubmission(BaseModel):

    student_id: str
    question_id: int
    selected_answer: str