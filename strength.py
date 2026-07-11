import re

def check_strength(password):
    """
    Checks the strength of a password based on 5 rules:
    1. Minimum 8 characters
    2. At least 1 uppercase letter
    3. At least 1 lowercase letter
    4. At least 1 number
    5. At least 1 special character

    Returns a tuple:
    - strength: "Weak", "Medium", or "Strong"
    - feedback: list of suggestions to improve password
    """
    score = 0
    feedback = []

    # Rule 1 - Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters")

    # Rule 2 - Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ At least 1 uppercase letter")

    # Rule 3 - Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ At least 1 lowercase letter")

    # Rule 4 - Number
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ At least 1 number")

    # Rule 5 - Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ At least 1 special character (!@#$...)")

    # Decide strength
    if score <= 2:
        strength = "🔴 Weak"
    elif score <= 4:
        strength = "🟡 Medium"
    else:
        strength = "🟢 Strong"

    return strength, feedback