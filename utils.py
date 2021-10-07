from flask import g
import sqlite3


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("test.db")
    return db


def query_db(query, args=(), one=False):
    conn = get_db()
    cur = conn.cursor()
    conn.row_factory = sql.Row

    cur.execute(query, args)
    ds = cur.fetchall()
    cur.close()
    conn.close()
    return ds


def insert(table, data):
    try:
        conn = get_db()
        cur = conn.cursor()
        query = "insert into {table} values {data}".format(
            table=table, data=data)
        cur.execute(query)
        con.commit()
    except:
        conn.rollback()
    finally:
        cur.close()
        conn.close()
