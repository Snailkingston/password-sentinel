import re
from app.entropy import entropy_score


def calculate_score(password, entropy, patterns, is_common):
    score = 0
    length = len(password)

    if length >= 15:
        score += 25
    elif length >= 11:
        score += 18
    elif length >= 8:
        score += 10

    types = sum([
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"[0-9]", password)),
        bool(re.search(r"[^\w]", password)),
    ])

    score += [0, 5, 12, 18, 25][types]
    score += entropy_score(entropy)
    score -= min(len(patterns) * 10, 25)

    if is_common:
        score = min(score, 20)

    return max(0, min(score, 100))


def rating_from_score(score: int) -> str:
    if score <= 20:
        return "VERY WEAK"
    if score <= 40:
        return "WEAK"
    if score <= 60:
        return "MODERATE"
    if score <= 80:
        return "STRONG"
    return "VERY STRONG"
