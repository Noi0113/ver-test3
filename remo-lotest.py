import sqlite3
import streamlit as st

# StreamlitのWebサイトで入力された情報を取得
input_data = st.text_input('Enter your data')

# データベースファイルに書き込み
conn = sqlite3.connect('local_database.db')
c = conn.cursor()

# ここでは例としてテーブル名を 'TABLE_NAME'、カラム名を 'COLUMN_NAME' としています。
# 実際には適切なテーブル名とカラム名を指定してください。
c.execute("INSERT INTO TABLE_NAME (COLUMN_NAME) VALUES (?)", (input_data,))

conn.commit()
conn.close()
