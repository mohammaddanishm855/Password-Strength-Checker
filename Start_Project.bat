
@echo off
cd /d "%~dp0"
echo Starting Password Security Analyzer...
python -m streamlit run app.py
pause
