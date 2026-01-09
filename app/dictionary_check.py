from pathlib import Path

DICT_PATH = Path(__file__).resolve().parents[1] / "data" / "common_passwords.txt"

try:
    with open(DICT_PATH, "r", encoding="utf-8") as f:
        COMMON_PASSWORDS = set(p.strip() for p in f)
except Exception:
    COMMON_PASSWORDS = set()


def is_common_password(password: str) -> bool:
    return password in COMMON_PASSWORDS
