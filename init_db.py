#!/usr/bin/env Python3

import sqlite3
from datetime import datetime
import random
from time import sleep


def sqlite_conn():
    try:
        connection = sqlite3.connect('meterData.db',
                                     detect_types=sqlite3.PARSE_DECLTYPES |
                                     sqlite3.PARSE_COLNAMES)
        return connection
    except Exception as e:
        print('Error:', e)


def create_db_schema():
    try:
        connection = sqlite_conn()
        print('Creating table...')
        with open('schema.sql') as f:
            connection.executescript(f.read())
        print('Schema successfully created!')
    except Exception as e:
        print('Error:', e)


def generate_random_string():
    try:
        sample_string = 'abcdefghijklmnopqrstuvwxyz'
        length = 10
        random_string = ''

        for i in range(length):
            if i % 2 == 0:
                random_string += random.choice(sample_string)

        return random_string
    except Exception as e:
        print('error:', e)


def create_fake_meter_label():
    try:
        meter_label_rows = []
        for _ in range(10):
            ('Faking label data...')
            label = generate_random_string()
            meter_label_rows.append(label)
        print('done!')
        return meter_label_rows
    except Exception as e:
        print('error:', e)


def create_fake_meter_data():
    try:
        meter_data_rows = []
        for _ in range(10):
            print('creating...', _)
            timeStamp = datetime.now()
            value = '{0:07}'.format(random.randint(1, 10000))
            meter_data_rows.append((timeStamp, value))
            sleep(10)
        return meter_data_rows
    except Exception as e:
        print('Error:', e)


def add_fake_data():
    try:
        conn = sqlite_conn()

        cursor = conn.cursor()

        meters_insert_query = 'INSERT INTO meters \
            (label) VALUES (?)'
        meter_label_row = create_fake_meter_label()

        for label_found in meter_label_row:
            cursor.execute(meters_insert_query, [label_found])

        conn.commit()
        print('Meter data inserted successfully!')

        meter_ids = cursor.execute('SELECT id FROM meters')

        meter_data_row = create_fake_meter_data()
        meter_data_insert_query = 'INSERT INTO meter_data \
            (meter_id, time_stamp, value)\
                VALUES (?, ?, ?)'
        for meter_id_found, meter_data_found in zip(meter_ids, meter_data_row):

            cursor.execute(meter_data_insert_query,
                           [meter_id_found[0],
                            meter_data_found[0],
                            meter_data_found[1]]
                           )
        conn.commit()
        conn.close()
        print('Inserted meter data successfully!')
    except Exception as e:
        print('Error:', e)


create_db_schema()
add_fake_data()
