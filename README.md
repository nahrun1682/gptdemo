# 1. デモ用フロント画面

# 2. 目次

- [1. デモ用フロント画面](#1-デモ用フロント画面)
- [2. 目次](#2-目次)
- [3. 前提](#3-前提)
- [4. 使い方](#4-使い方)
- [5. プロキシ環境](#5-プロキシ環境)

# 3. 前提 

# 4. 使い方

```zsh
#gptdemo配下に移動
cd gptdemo 

#仮想環境起動
poetry install
#フロント起動
poetry run streamlit run gptdemo/01_ChatGPT@2デジ.py
```

成功すると以下が標準出力される
```zsh
/mnt/d/GPT/gptdemo % poetry run streamlit run gptdemo/01_ChatGPT@2デジ.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.18.62.148:8501

gio: http://localhost:8501: Operation not supported

```

そしたら、http://localhost:8501
へ遷移

# 5. プロキシ環境

参考：https://qiita.com/c60evaporator/items/7a757134d028a7734118

プロジェクト内のpyproject.tomlに以下の記述を追加

```zsh
[[tool.poetry.source]]
name = "proxy"
url = "http://プロキシのアドレス:ポート"
default = true
```