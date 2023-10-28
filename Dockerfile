# Pythonイメージのベースとなるイメージを指定
FROM python:3.11

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係ファイルをコンテナにコピー
COPY poetry.lock pyproject.toml /app/

# Poetryをインストールし、依存関係をインストール
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

# アプリのソースコードをコンテナにコピー
COPY . /app

# アプリを実行するコマンド
CMD ["poetry", "run", "streamlit", "run", "--server.address", "0.0.0.0", "--server.port", "8501", "gptdemo/01_ChatGPT_DEMO.py"]
