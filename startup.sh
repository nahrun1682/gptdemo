#!/bin/bash

# 依存関係のインストール
pip install poetry
poetry install

# FastAPIアプリケーションの起動（Gunicornを使用）
poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_app.main:app --bind 0.0.0.0:8000 &

# Streamlit アプリケーションの実行
poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port 80 &
