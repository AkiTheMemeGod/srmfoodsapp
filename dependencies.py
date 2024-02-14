import sqlite3 as sq
import streamlit as st


class Database:
    def __init__(self):
        self.connection = sq.connect("menu.db")

    def get_data(self, food):

        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {food}")
        data = cursor.fetchall()[0][4]
        print(data)


db = Database()
db.get_data("nonveg")

