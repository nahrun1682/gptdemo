import streamlit as st
import requests  # AWS Price List APIを叩くために使用します

import streamlit as st

# ストリームリットのタイトル
st.title("AWS EC2 Cost Calculator")

# カラムの設定
col1, col2 = st.columns(2)

# カラム1にインスタンスタイプのセレクトボックスを配置
with col1:
    instance_type = st.selectbox('Select EC2 Instance Type', ['t2.micro', 't2.small', 't2.medium'])

# カラム2にリージョンのセレクトボックスを配置
with col2:
    region = st.selectbox('Select AWS Region', ['us-east-1', 'us-west-1'])

# 計算ボタン
if st.button('Calculate Cost'):
    # 価格計算ロジック（サンプルのため固定値を使用）
    price_per_hour = 0.0116  # 例としてt2.microの価格を固定
    monthly_cost = 24 * 30 * price_per_hour  # 月額コストの計算

    # 結果の表示
    st.write(f"Estimated monthly cost for {instance_type} in {region}: ${monthly_cost:.2f}")

# 注意書き
st.markdown("※このアプリケーションは、簡単なデモのためのものであり、実際のコスト計算にはAWSの料金API等を利用して実装する必要があります。")
