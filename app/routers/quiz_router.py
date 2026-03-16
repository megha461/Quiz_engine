from fastapi import APIRouter
from ..services.quiz_service import get_quiz

router = APIRouter()

@router.get("/quiz")

def quiz(topic: str, difficulty: str):

    return get_quiz(topic, difficulty)
from fastapi import APIRouter
from ..services.quiz_service import generate_quiz

router = APIRouter()

@router.get("/quiz")
def get_quiz(topic: str, difficulty: str):
    return generate_quiz(topic, difficulty)