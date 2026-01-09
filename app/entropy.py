import math
import re


def calculate_entropy(password: str) -> float:
    if not password:
        return 0.0

    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^\w]", password):
        charset += 32

    return math.log2(charset ** len(password)) if charset else 0.0


def entropy_score(entropy: float) -> int:
    if entropy < 40:
        return 5
    if entropy < 60:
        return 12
    if entropy < 80:
        return 18
    return 25
