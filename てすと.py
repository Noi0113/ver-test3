import subprocess
import sqlite3
import streamlit as st

# リポジトリのURLとクローン先のディレクトリパスを指定します。
repo_url = "https://github.com/Noi0113/ver-test3.git"
clone_dir = "/path/to/clone/directory"

# git cloneコマンドを実行します。
subprocess.check_call(["git", "clone", repo_url, clone_dir], check=True)




# StreamlitのWebサイトで入力された情報を取得します。
input_data = st.text_input('Enter your data')

# データベースファイルに書き込みます。
conn = sqlite3.connect(f'{clone_dir}/test-monketsu3.db')
c = conn.cursor()

# ここでは例としてテーブル名を 'TABLE_NAME'、カラム名を 'COLUMN_NAME' としています。
# 実際には適切なテーブル名とカラム名を指定してください。
c.execute("INSERT INTO TestTable3 (univ) VALUES (?)", (input_data,))

conn.commit()
conn.close()



# リポジトリのディレクトリに移動します。
subprocess.check_call(["cd", clone_dir], check=True)

# git addコマンドを実行します。
subprocess.check_call(["git", "add", "."], check=True)

# git commitコマンドを実行します。
commit_message = "Update database"
subprocess.check_call(["git", "commit", "-m", commit_message], check=True)

#何者か
subprocess.check_call(["git", "config", "--global", "user.name", "Noi0113"])
subprocess.check_call(["git", "config", "--global", "user.email", "s2110524@u.tsukuba.ac.jp"])

# git pushコマンドを実行します。
subprocess.check_call(["git", "push","origin","main"], check=True)

