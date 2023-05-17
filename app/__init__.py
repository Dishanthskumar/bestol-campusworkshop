"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi81p5269vf5qbd5tpg-a.oregon-postgres.render.com",
        database="todo_yydj",
        user="root",
        password="vHWXAMRfkwumXlvzdVeKDISYaDWu4O1Z")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
