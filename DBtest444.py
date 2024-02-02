import subprocess
import sqlite3

import streamlit as st
import os

# アプリのスクリプトがあるディレクトリ
app_dir = os.path.dirname(os.path.abspath(__file__))
# データベースファイルの相対パス
database_path = os.path.join(app_dir, "test-monketsu3.db")
# データベースファイルのパス
#database_path = "temp_clone_dir/path/to/database.db"

# リモートリポジトリのURL
remote_repo_url = "https://github.com/Noi0113/ver-test3.git"
# ローカルにクローンするディレクトリ
local_clone_dir = "ver-test3"


# Streamlitアプリ

# ローカルの変更をリモートリポジトリにプッシュ
def push_to_remote():
    try:
        # 変更をローカルリポジトリに追加
        subprocess.run(["git", "add", database_path])

        # 変更をコミット
        subprocess.run(["git", "commit", "-m", "Update database"], cwd=local_clone_dir)

        # ローカルの変更をリモートリポジトリにプッシュ
        subprocess.run(["git", "push", "origin", "master"], cwd=local_clone_dir)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # 入力データを取得
    input_data = st.text_input("Enter data:")

    # 入力データをデータベースに書き込む
    if st.button("Submit"):
        # データベースに接続
        conn = sqlite3.connect(database_path)
        c = conn.cursor()
        # テーブルが存在しない場合は作成
        c.execute('''CREATE TABLE IF NOT EXISTS my_table (data TEXT)''')
        # データを挿入
        c.execute("INSERT INTO my_table (data) VALUES (?)", (input_data,))
        # 変更をコミット
        conn.commit()
        # 接続を閉じる
        conn.close()
        st.success("Data inserted into database successfully!")
        # リモートリポジトリに変更をプッシュ
        if push_to_remote():
            st.success("Changes pushed to remote repository successfully!")
        else:
            st.error("Failed to push changes to remote repository!")

# Streamlitアプリを実行
if __name__ == "__main__":
    # リモートリポジトリをローカルにクローン
    subprocess.run(["git", "clone", remote_repo_url, local_clone_dir])
    main()

