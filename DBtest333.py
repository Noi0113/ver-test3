import streamlit as st
import sqlite3
from github import Github

# GitHubアクセストークンとリポジトリの情報
github_access_token = "YourAccessToken"
repository_owner = "Owner"
repository_name = "Repository"
database_file_path = "test-monketsu3.db"

# Streamlitアプリケーション
def main():
    st.title("データベース更新")

    # 入力フォーム
    data_input = st.text_input("Enter Data")

    if st.button("Update Database"):
        # SQLiteデータベースへの接続とデータの挿入
        conn = sqlite3.connect(database_file_path)
        c = conn.cursor()
        c.execute("INSERT INTO data_table (column_name) VALUES (?)", (data_input,))
        conn.commit()
        conn.close()

        # GitHubリポジトリへのアクセス
        g = Github(github_access_token)
        repo = g.get_user(repository_owner).get_repo(repository_name)

        # 更新したデータベースファイルをリポジトリに保存
        with open(database_file_path, 'rb') as file:
            content = file.read()
            repo.update_file(database_file_path, "Update database file", content, sha=None)

        st.success("Database Updated and Saved to GitHub Repository Successfully!")

if __name__ == "__main__":
    main()
