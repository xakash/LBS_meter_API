#!/usr/bin/env Python3

import sqlite3


def get_db_connection():
    try:
        conn = sqlite3.connect('meterData.db')
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print('Error:', e)
        return e
