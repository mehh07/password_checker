import math
import string
import re

# Load common dictionary words
with open("common_text.txt", "r") as f:
    COMMON_WORDS = set(word.strip().lower() for word in f)


def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    if pool == 0 or len(password) == 0:
        return 0
    entropy = len(password) * math.log2(pool)
    return entropy


def has_sequence(password):
    sequences = ['1234', 'abcd', 'qwerty', 'password', '1111']
    password_lower = password.lower()
    return any(seq in password_lower for seq in sequences)


def evaluate_password(password):
    score = 0
    reasons = []

    length = len(password)
    entropy = calculate_entropy(password)

    # Length
    if length >= 12:
        score += 2
        reasons.append("Long password (12+ characters)")
    elif length >= 8:
        score += 1
        reasons.append("Moderate length")
    else:
        reasons.append("Too short (less than 8 characters)")

    # Digits
    if any(c.isdigit() for c in password):
        score += 1
        reasons.append("Contains digits")

    # Specials
    if any(c in string.punctuation for c in password):
        score += 1
        reasons.append("Contains special characters")

    # Upper/Lower
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1
        reasons.append("Contains both uppercase and lowercase letters")

    # Entropy
    if entropy >= 40:
        score += 2
        reasons.append(f"High entropy ({round(entropy, 2)} bits)")
    elif entropy >= 28:
        score += 1
        reasons.append(f"Moderate entropy ({round(entropy, 2)} bits)")
    else:
        reasons.append(f"Low entropy ({round(entropy, 2)} bits)")

    # Dictionary words
    lowered = password.lower()
    for word in COMMON_WORDS:
        if word in lowered and len(word) > 3:
            score -= 1
            reasons.append(f"Contains common word: '{word}'")
            break

    # Sequence
    if has_sequence(password):
        score -= 2
        reasons.append("Contains easy-to-guess pattern or sequence")

    # Final rating
    if score >= 6:
        rating = "Strong"
    elif score >= 3:
        rating = "Moderate"
    else:
        rating = "Weak"

    return {"rating": rating, "reasons": reasons}
