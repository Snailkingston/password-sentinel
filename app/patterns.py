import re

KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcv"]
SEQUENCES = ["abc", "123", "abcd", "1234"]


def detect_patterns(password: str) -> list:
    found = []

    if re.search(r"(.)\1{2,}", password):
        found.append("repeated characters")

    for seq in SEQUENCES:
        if seq in password.lower():
            found.append("sequential pattern")

    for key in KEYBOARD_PATTERNS:
        if key in password.lower():
            found.append("keyboard pattern")

    substitutions = {"@": "a", "0": "o", "1": "i"}
    for k, v in substitutions.items():
        if k in password.lower() and v in password.lower():
            found.append("simple substitution")

    return list(set(found))
