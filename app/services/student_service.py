from ..utils.difficulty import adjust_difficulty
def submit_answer(data):

    selected = data["selected_answer"]

    correct_answer = "3"

    is_correct = selected == correct_answer

    new_difficulty = adjust_difficulty("easy", is_correct)

    return {
        "correct": is_correct,
        "next_difficulty": new_difficulty
    }
def evaluate_answers(correct_answers, student_answers):

    score = 0

    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            score += 1

    return {
        "score": score,
        "total": len(correct_answers)
    }