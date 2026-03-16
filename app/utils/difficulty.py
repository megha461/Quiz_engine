levels = ["easy", "medium", "hard"]


def adjust_difficulty(current, correct):

    index = levels.index(current)

    if correct and index < 2:
        return levels[index + 1]

    if not correct and index > 0:
        return levels[index - 1]

    return current