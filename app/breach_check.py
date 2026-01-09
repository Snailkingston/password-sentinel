import hashlib
from pathlib import Path

BREACH_PATH = Path(__file__).resolve().parents[1] / "data" / "breach_hashes.txt"

try:
    with open(BREACH_PATH, "r") as f:
        BREACH_HASHES = set(line.split(":")[0] for line in f)
except Exception:
    BREACH_HASHES = set()


def is_breached(password: str) -> bool:
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return sha1[:5] in BREACH_HASHES
