from app.entropy import calculate_entropy, entropy_score
from app.patterns import detect_patterns
from app.dictionary_check import is_common_password
from app.breach_check import is_breached
from app.scoring import calculate_score, rating_from_score


def analyze_password(password: str) -> dict:
    details = []
    recommendations = []

    if is_breached(password):
        return {
            "score": 0,
            "rating": "VERY WEAK",
            "details": ["Breach exposure: FOUND"],
            "recommendations": ["Change this password immediately"]
        }

    common = is_common_password(password.lower())
    patterns = detect_patterns(password)

    entropy = calculate_entropy(password)
    score = calculate_score(password, entropy, patterns, common)
    rating = rating_from_score(score)

    details.append(f"Length: {len(password)} characters")
    details.append(f"Entropy: {round(entropy, 2)} bits")
    details.append(f"Patterns detected: {len(patterns)}")
    details.append(f"Common password: {'Yes' if common else 'No'}")
    details.append("Breach exposure: Not found")

    if len(password) < 16:
        recommendations.append("Increase length to at least 16 characters")

    if patterns:
        recommendations.append("Avoid predictable patterns and sequences")

    return {
        "score": score,
        "rating": rating,
        "details": details,
        "recommendations": recommendations
    }
