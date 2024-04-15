import sqlite3 as sq
import streamlit as st
from streamlit_option_menu import option_menu


class Database:
    def __init__(self):
        self.connection = sq.connect("menu.db")

    def get_data(self, food):

        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {food}")
        data = cursor.fetchall()
        # print(data)
        return data

    def add_data(self, data):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO veg VALUES (?,?,?,?)", data)
        self.connection.commit()
        cursor.close()

    def get_price(self, name):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT price FROM nonveg WHERE name = '{name}'")
        data = cursor.fetchall()
        return int(data[0][0][:-2])


def butt_func(item):
    if 'total_items' not in st.session_state:
        st.session_state.total_items = 0

    if item not in st.session_state:
        st.session_state[item] = 0

    st.session_state.total_items += 1
    st.session_state[item] += 1

    st.sidebar.write(st.session_state[item])
    st.sidebar.write(item)


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


d = Database()
import pandas as pd

df = pd.read_csv("new.csv")
price = tuple(df["price"])
name = tuple(df["name"])
img = tuple(df["image"])
desc = tuple(df["description"])
print(name, price, desc)

for i in range(len(df)):
    d.add_data((name[i], desc[i], img[i], str(price[i])))

