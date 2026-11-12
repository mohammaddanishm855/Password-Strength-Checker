
from password_checker import analyze_password

test_cases = [
    "12345678",
    "Password123!",
    "aaaaaaaaaaaa",
    "qwerty123",
    "River-Coffee-Planet-92"
]

for password in test_cases:
    result = analyze_password(password)

    print("\n" + "=" * 40)
    print("Test password:", password)
    print("Strength:", result["strength"])
    print("Display score:", result["score"])
    print("Estimator score:", result["estimator_score"])
    print("Detected patterns:", result["patterns"])
    print("Recommendations:", result["recommendations"])
