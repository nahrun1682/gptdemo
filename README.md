# 1. デモ用フロント画面

# 2. 目次

- [1. デモ用フロント画面](#1-デモ用フロント画面)
- [2. 目次](#2-目次)
- [3. 前提](#3-前提)
- [4. 使い方](#4-使い方)
- [5. プロキシ環境](#5-プロキシ環境)
- [6. Poetryコマンド](#6-poetryコマンド)

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

参考：[プロキシ環境でのPython環境構築まとめ](https://qiita.com/c60evaporator/items/7a757134d028a7734118)

プロジェクト内のpyproject.tomlに以下の記述を追加

```zsh
[[tool.poetry.source]]
name = "proxy"
url = "http://プロキシのアドレス:ポート"
default = true
```

# 6. Poetryコマンド

参考:[Poetryをサクッと使い始めてみる](https://qiita.com/ksato9700/items/b893cf1db83605898d8a)
インストールされているパッケージのアップグレード（バージョンアップ）を行いたい時には poetry updateを使う。

```zsh
poetry update --dry-run
#とするとアップグレードされるパッケージがわかるので、それを確認した上で
poetry update
```
すると実際にアップグレードが行われます。なお、poetry updateした時に変更されるのはpoetry.lockだけで pyproject.tomlはそのままです。新しいバージョンの新機能を使うなどの場合はpyproject.tomlを手動で修正してして依存するバージョンを変える必要があります。