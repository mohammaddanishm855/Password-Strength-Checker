
import re
from zxcvbn import zxcvbn


# Common passwords for local pattern screening
COMMON_PASSWORDS = {
    "password", "password123", "123456",
    "12345678", "qwerty", "admin",
    "welcome", "iloveyou", "abc123",
    "letmein", "monkey", "dragon"
}

# Common keyboard sequences
KEYBOARD_PATTERNS = [
    "qwerty", "asdfgh", "zxcvbn",
    "qwertyuiop", "1234567890"
]


def analyze_characters(password):
    """Analyze password length and character composition."""

    checks = [
        {
            "name": "Minimum 8 characters",
            "passed": len(password) >= 8
        },
        {
            "name": "At least 12 characters",
            "passed": len(password) >= 12
        },
        {
            "name": "Uppercase letters",
            "passed": any(c.isupper() for c in password)
        },
        {
            "name": "Lowercase letters",
            "passed": any(c.islower() for c in password)
        },
        {
            "name": "Numbers",
            "passed": any(c.isdigit() for c in password)
        },
        {
            "name": "Special symbols",
            "passed": any(not c.isalnum() for c in password)
        }
    ]

    categories = sum([
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password)
    ])

    return {
        "length": len(password),
        "character_categories": categories,
        "checks": checks
    }


def detect_patterns(password):
    """Detect common predictable password patterns."""

    findings = []

    if password.lower() in COMMON_PASSWORDS:
        findings.append("Commonly used password")

    if re.search(r"(.)\1{2,}", password):
        findings.append("Repeated characters detected")

    # Detect ascending or descending numeric/alphabetic sequences.
    sequences = [
        "0123456789",
        "9876543210",
        "abcdefghijklmnopqrstuvwxyz",
        "zyxwvutsrqponmlkjihgfedcba"
    ]

    for sequence in sequences:
        for length in range(3, len(sequence) + 1):
            for start in range(len(sequence) - length + 1):
                pattern = sequence[start:start + length]

                if pattern in password.lower():
                    findings.append("Sequential character pattern detected")
                    break

            if "Sequential character pattern detected" in findings:
                break

        if "Sequential character pattern detected" in findings:
            break

    if any(pattern in password.lower() for pattern in KEYBOARD_PATTERNS):
        findings.append("Keyboard pattern detected")

    return findings


def evaluate_strength(password, estimator_score, patterns):
    """Classify password strength using guessability and security checks."""

    if len(password) < 8:
        return "Weak"

    if password.lower() in COMMON_PASSWORDS:
        return "Weak"

    if estimator_score <= 1:
        return "Weak"

    # Strong passwords must have sufficient length,
    # a high estimator score and no detected patterns.
    if (
        estimator_score >= 3
        and len(password) >= 12
        and not patterns
    ):
        return "Strong"

    return "Medium"


def generate_recommendations(
    password,
    patterns,
    estimator_feedback,
    strength
):
    """Generate recommendations based on analysis findings."""

    recommendations = []

    if len(password) < 12:
        recommendations.append(
            "Use a longer password or passphrase of at least 12 characters."
        )

    if not any(c.isupper() for c in password):
        recommendations.append("Consider adding uppercase letters.")

    if not any(c.islower() for c in password):
        recommendations.append("Consider adding lowercase letters.")

    if not any(c.isdigit() for c in password):
        recommendations.append("Consider adding numbers.")

    if not any(not c.isalnum() for c in password):
        recommendations.append("Consider adding special symbols.")

    if patterns:
        recommendations.append(
            "Avoid repeated characters, sequences and predictable patterns."
        )

    if estimator_feedback.get("warning"):
        recommendations.append(estimator_feedback["warning"])

    for suggestion in estimator_feedback.get("suggestions", []):
        recommendations.append(suggestion)

    if strength == "Strong" and not recommendations:
        recommendations.append(
            "Good result. Keep this password unique to one account."
        )

    # Remove duplicate recommendations while preserving order.
    return list(dict.fromkeys(recommendations))


def analyze_password(password):
    """
    Main password analysis function.

    Returns a structured security analysis without storing
    or transmitting the submitted password.
    """

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if not password:
        raise ValueError("Password cannot be empty.")

    # Layer 1: Character analysis
    character_analysis = analyze_characters(password)

    # Layer 2: Guessability estimation
    estimator_result = zxcvbn(password)

    estimator_score = estimator_result["score"]

    # Layer 3: Pattern detection
    patterns = detect_patterns(password)

    # Layer 4: Final strength classification
    strength = evaluate_strength(
        password,
        estimator_score,
        patterns
    )

    # A normalized display score, not a probability or entropy value.
    display_score = estimator_score * 25

    # Layer 5: Security recommendations
    recommendations = generate_recommendations(
        password,
        patterns,
        estimator_result.get("feedback", {}),
        strength
    )

    return {
        "strength": strength,
        "score": display_score,
        "estimator_score": estimator_score,
        "length": character_analysis["length"],
        "character_categories": character_analysis[
            "character_categories"
        ],
        "checks": character_analysis["checks"],
        "patterns": patterns,
        "recommendations": recommendations,
        "feedback": estimator_result.get("feedback", {}),
        "crack_time_estimates": estimator_result.get(
            "crack_times_display", {}
        ),
        "guesses": estimator_result.get("guesses")
    }
