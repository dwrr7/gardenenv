import sqlite3
from flask import g

DATABASE = "./data.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row # hasil dari query dari SQlite kembali ke py
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
