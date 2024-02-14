import sqlite3 as sq
import streamlit as st


class Database:
    def __init__(self):
        self.connection = sq.connect("menu.db")

    def get_data(self, food):

        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {food}")
        data = cursor.fetchall()
        # print(data)
        return data


def custom_title(pos, size, color, title, align="center"):
    if pos == "side":
        st.sidebar.markdown(f"""
                        <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="{align}">{title}</h1>
                        """,
                            unsafe_allow_html=True)

    else:
        st.markdown(f"""
                <h1 style="font-family:monospace; color:{color}; font-size: {size}px;", align="{align}">{title}</h1>
""",
                    unsafe_allow_html=True)

