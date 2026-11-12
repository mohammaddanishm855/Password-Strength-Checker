# 🔐 Password Strength & Security Analyzer

**A Python-powered password security assessment tool that evaluates password strength, identifies predictable patterns, and generates actionable recommendations using intelligent password analysis.**

<p align="center">

  **Python · Streamlit · zxcvbn · Security Analysis**

</p>

---

## 📌 Project Overview

The Password Strength & Security Analyzer is a cybersecurity-focused application designed to help users understand the security quality of their passwords.

Unlike traditional password validators that only check length and character combinations, this application uses the **zxcvbn password estimation algorithm** to evaluate password complexity, recognize common patterns, identify predictable sequences, and provide meaningful security feedback.

The application presents its findings through a user-friendly interface, making password security assessment easier to understand.

## 🎯 Key Objectives

- Evaluate password strength using intelligent password analysis.
- Identify predictable patterns and commonly used password structures.
- Assess password length and character diversity.
- Provide actionable recommendations to improve password security.
- Present analysis results through an interactive dashboard.

## 🚀 Core Features

### 1. Intelligent Password Strength Assessment
- Password strength estimation using zxcvbn.
- Categorization of password strength.
- Normalized strength score presentation.
- Identification of weak and predictable password structures.

### 2. Password Pattern Analysis
- Detection of common password patterns.
- Identification of sequential characters.
- Recognition of repeated character combinations.
- Analysis of predictable password structures.

### 3. Character Composition Analysis
- Password length evaluation.
- Uppercase character detection.
- Lowercase character detection.
- Numeric character detection.
- Special character detection.

### 4. Security Recommendations
- Identifies password weaknesses.
- Provides improvement suggestions.
- Encourages stronger password creation practices.
- Highlights missing security requirements.

### 5. Interactive Security Dashboard
- Clear password analysis results.
- Strength score visualization.
- Password composition breakdown.
- Security requirement indicators.
- Readable feedback and recommendations.

## 🏗️ System Architecture

```text
              USER INPUT
                  |
                  v
          PASSWORD ANALYZER
                  |
          +-------+--------+
          |                |
          v                v
    PASSWORD LENGTH    CHARACTER ANALYSIS
          |                |
          v                v
    PATTERN DETECTION   COMPOSITION CHECK
          |                |
          +-------+--------+
                  |
                  v
           ZXCVBN ANALYSIS
                  |
                  v
          STRENGTH EVALUATION
                  |
                  v
         SECURITY RECOMMENDATIONS
                  |
                  v
          STREAMLIT DASHBOARD
                  |
                  v
           ANALYSIS RESULTS
```

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and analysis logic |
| Streamlit | Interactive web interface |
| zxcvbn | Password strength estimation |
| Regular Expressions | Pattern and character analysis |
| Pytest / Python Testing | Engine validation |

## 📂 Project Structure

```text
Password-Strength-Checker/
│
├── app.py                  # Streamlit application
├── password_checker.py    # Password analysis engine
├── test_engine.py         # Engine testing
├── requirements.txt       # Project dependencies
├── Start_Project.bat      # Windows launcher
├── README.md              # Project documentation
└── .gitignore             # Git exclusions
```

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or later
- Git
- Windows / Linux

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd Password-Strength-Checker
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux:**

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Launch the Application

```bash
streamlit run app.py
```

Alternatively, Windows users can launch the application using:

```text
Start_Project.bat
```

## 🧪 Testing & Validation

The project includes a dedicated testing module to validate the password analysis engine.

Test scenarios can include:

- Weak passwords.
- Common dictionary-based passwords.
- Sequential character patterns.
- Repeated character combinations.
- Longer passwords with mixed character categories.
- Stronger, less predictable passwords.

Run the tests using:

```bash
python test_engine.py
```

## 🔒 Security Considerations

- Password strength scores are estimates, not guarantees of resistance to attacks.
- A complex-looking password can still be predictable.
- Passwords should never be reused across multiple accounts.
- Real passwords should not be entered into untrusted testing environments.
- Passwords should not be stored or logged in plaintext.

**Important:** The zxcvbn score represents an estimated password-strength category, not a probability of being hacked.

## 🔮 Future Enhancements

- Password entropy and guess-time visualization.
- Expanded dictionary and pattern analysis.
- Secure password generation.
- Additional password audit capabilities.
- Enhanced security analytics dashboard.

## 👨‍💻 Author

**Mohammad Danish**

Cybersecurity Enthusiast | SOC Analyst Aspirant

**Areas of Interest:** Security Operations, Threat Detection, Blue Team Security, Network Security and Python Automation.

---

⭐ If you find this project useful, consider giving the repository a star.

