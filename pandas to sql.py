# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:35:05 2021

@author: Vadym
"""

import pandas as pd
import pandas.io.sql
import pyodbc
#conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + '; UID = ' + UID + '; PWD = ' + UID + 'Trusted_Connection=yes')

conn = pyodbc.connect(
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=mydatabase;'
    'UID=root;'
    'PWD=password;'
)

sql_query_string = "SELECT * FROM hb_areas"
df= pandas.io.sql.read_sql(sql_query_string, conn)
#print(df)
query_string = "CREATE TABLE test_table (idx)"
cursor = conn.cursor()
cursor.execute(query_string)
copy = cursor.fetchall()
print(copy)
#conn.commit()

df.to_sql("test_table", conn)
