#!/bin/bash

echo "Starting setup..."

echo "Loading environment variables..."
source ./.env

# 依存関係のインストール
echo "Installing dependencies..."
pip install poetry
poetry install

echo "Starting Streamlit application..."
# Streamlit アプリケーションの実行
echo $MY_STRING
echo $MY_NUMBER
echo $PORT

poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port $PORT &

echo "Starting FastAPI application..."
# FastAPIアプリケーションの起動（Gunicornを使用）
poetry run gunicorn -w 4 -k uvicorn.workers.UvicornWorker fastapi_app.main:app --bind 0.0.0.0:8000 &

echo "Startup script completed."
