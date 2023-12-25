import streamlit as st
import requests  # AWS Price List APIを叩くために使用します

# ストリームリットのタイトル
st.title("AWS EC2 Cost Calculator")

# ユーザー入力のためのセレクトボックスを設定
instance_type = st.selectbox('Select EC2 Instance Type', ['t2.micro', 't2.small', 't2.medium'])
region = st.selectbox('Select AWS Region', ['us-east-1', 'us-west-1'])

# 計算ボタン
if st.button('Calculate Cost'):
    # 実際には、AWS Pricing APIを呼び出して料金を取得する必要があります。
    # ここでは、サンプルとして固定値を返すようにしています。
    # AWS Price List APIから価格情報を取得する実装が必要です。
    price_per_hour = 0.0116  # 例としてt2.microの価格を固定

    # 簡易的なコスト計算
    monthly_cost = 24 * 30 * price_per_hour

    # 結果を表示
    st.write(f"Estimated monthly cost for {instance_type} in {region}: ${monthly_cost:.2f}")

# 注意書き
st.markdown("※このアプリケーションは、簡単なデモのためのものであり、実際のコスト計算にはAWSの料金API等を利用して実装する必要があります。")
