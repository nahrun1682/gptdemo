#!/bin/bash

# 依存関係のインストール
pip install poetry
poetry install

# Streamlit アプリケーションの実行
poetry run streamlit run gptdemo/01_ChatGPT_DEMO.py --server.port 80
