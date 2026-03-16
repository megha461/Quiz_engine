from fastapi import APIRouter
from ..services.student_service import submit_answer
router = APIRouter()
@router.post("/submit-answer")
def answer(data: dict):
    return submit_answer(data)
from fastapi import APIRouter
from ..services.student_service import evaluate_answers
router = APIRouter()
@router.post("/student/submit")
def submit_quiz():
    correct = ["A","B","C"]
    student = ["A","C","C"]
    return evaluate_answers(correct, student)