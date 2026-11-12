
import streamlit as st
from password_checker import analyze_password

st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background: #07111f;
    color: #e5eefb;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(135deg, #10243d, #0b1728);
    padding: 28px;
    border: 1px solid #1c4262;
    border-radius: 16px;
    margin-bottom: 25px;
}
.hero h1 {
    color: #35d5ff;
    margin-bottom: 8px;
}
.hero p {
    color: #b7c9dc;
}
.result-card {
    background: #10243d;
    border: 1px solid #244866;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 12px;
}
.metric {
    color: #35d5ff;
    font-size: 30px;
    font-weight: bold;
}
.small-note {
    color: #9db2c8;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="hero">
    <h1>🔐 Password Security Analyzer</h1>
    <p>
        Analyze password strength, identify predictable patterns,
        and receive security recommendations.
    </p>
</div>
""", unsafe_allow_html=True)

st.subheader("Password Analysis")

with st.form("password_analysis_form"):
    password = st.text_input(
        "Enter a password",
        type="password",
        placeholder="Enter a password to analyze"
    )

    analyze_button = st.form_submit_button(
        "Analyze Password",
        use_container_width=True
    )

if analyze_button:
    if not password:
        st.warning("Please enter a password first.")
    else:
        try:
            result = analyze_password(password)

            st.divider()
            st.subheader("Analysis Results")

            # Strength result
            strength = result["strength"]

            if strength == "Strong":
                st.success("Password Strength: STRONG")
            elif strength == "Medium":
                st.warning("Password Strength: MEDIUM")
            else:
                st.error("Password Strength: WEAK")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("zxcvbn Score", f'{result["estimator_score"]}/4')

            with col2:
                st.metric("Password Length", result["length"])

            with col3:
                st.metric(
                    "Character Categories",
                    f'{result["character_categories"]}/4'
                )

            st.caption(
                "The score is a normalized zxcvbn category score, "
                "not a probability of being hacked."
            )

            # Character checks
            st.subheader("Security Requirements")

            for check in result["checks"]:
                if check["passed"]:
                    st.success(f'✓ {check["name"]}')
                else:
                    st.error(f'✗ {check["name"]}')

            # Pattern detection
            st.subheader("Pattern Detection")

            if result["patterns"]:
                for pattern in result["patterns"]:
                    st.warning(pattern)
            else:
                st.success("No tested predictable patterns detected.")

            # Recommendations
            st.subheader("Security Recommendations")

            if result["recommendations"]:
                for recommendation in result["recommendations"]:
                    st.write(f"• {recommendation}")
            else:
                st.success("No additional recommendations.")

            # Estimator details
            st.subheader("Password Guessability")

            st.metric(
                "zxcvbn Estimator Score",
                f'{result["estimator_score"]}/4'
            )

            st.caption(
                "This estimate is model-based and should not be treated "
                "as a guarantee of real-world password security."
            )

        except Exception:
            st.error("Analysis failed. Please check the input and try again.")

st.divider()

st.markdown("""
<div style="text-align:center; color:#8298af; padding:15px;">
    Password Security Analyzer | Built with Python, Streamlit and zxcvbn
    <br>
    <span style="font-size:12px;">
        Passwords are analyzed locally by this application and are not
        intentionally stored or transmitted by the analysis code.
    </span>
</div>
""", unsafe_allow_html=True)
