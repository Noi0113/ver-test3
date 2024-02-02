import pandas as pd
import streamlit as st
import os

# StreamlitのWebサイトで入力された情報を取得
user_input = st.text_input('Enter your data')

# 入力がある場合、それをCSVファイルに書き込む
if user_input:
    # データをDataFrameに変換
    df = pd.DataFrame([user_input], columns=['User Input'])

    # 既存のCSVファイルが存在する場合はそれを読み込み、存在しない場合は新たに作成
    if os.path.exists('user_input.csv'):
        df_existing = pd.read_csv('user_input.csv')
        df = pd.concat([df_existing, df])

    # DataFrameをCSVファイルに書き込む
    df.to_csv('user_input.csv', index=False)

    st.write('Data saved to CSV file.')
