# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:44:38 2021

@author: Vadym
"""
import pandas as pd

import pyodbc

import datetime

conn = pyodbc.connect(
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=mydatabase;'
    'UID=root;'
    'PWD=password;'
    'charset=utf8mb4;'
)


cursor = conn.cursor()

current_time=str(datetime.datetime.now())
query_string = "INSERT INTO hb_capital_shops (updated_at) VALUES (current_timestamp)"

cursor.execute(query_string)
conn.commit()
cursor.execute("SELECT * FROM hb_capital_shops;")

rows = cursor.fetchall()
for row in rows:
    print(row)




               
#conn.commit()
