def get_quiz(topic, difficulty):

    questions = [
        {
            "question": "How many sides does a triangle have?",
            "options": ["2", "3", "4", "5"],
            "difficulty": difficulty
        },
        {
            "question": "Plants need sunlight to grow.",
            "options": ["True", "False"],
            "difficulty": difficulty
        }
    ]

    return {
        "topic": topic,
        "difficulty": difficulty,
        "questions": questions
    }
import random

def generate_quiz(topic: str, difficulty: str):

    easy_questions = [
        f"What is {topic}?",
        f"Define {topic}.",
        f"Why is {topic} important?"
    ]

    medium_questions = [
        f"Explain how {topic} works.",
        f"What are the main components of {topic}?",
        f"Give an example of {topic}."
    ]

    hard_questions = [
        f"Explain advanced concepts of {topic}.",
        f"What are limitations of {topic}?",
        f"Compare {topic} with another related concept."
    ]

    if difficulty == "easy":
        questions = random.sample(easy_questions, 3)

    elif difficulty == "medium":
        questions = random.sample(medium_questions, 3)

    else:
        questions = random.sample(hard_questions, 3)

    return {
        "topic": topic,
        "difficulty": difficulty,
        "questions": questions
    }