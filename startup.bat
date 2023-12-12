@echo off

REM Install dependencies using Poetry
poetry install

REM Run the front-end using Streamlit
start cmd /k "poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py"