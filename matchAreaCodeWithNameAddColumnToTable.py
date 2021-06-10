# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:35:05 2021

@author: Vadym
"""
import os
import pandas as pd
import pandas.io.sql
import pyodbc

os.chdir("data")

credentials_file = "hb_capital_credential_details.csv"
shops_file = "hb_capital_shops.csv"

conn = pyodbc.connect(
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=credentials;'
    'UID=root;'
    'PWD=password;'
)

cursor = conn.cursor()


det_query_string = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'hb_capital_credential_details'"
cursor.execute(det_query_string)
d_columns_list = cursor.fetchall()
details_col_list = list()
for item in d_columns_list:
    details_col_list.append(item[0])
credentials_df = pd.read_csv(credentials_file, names = details_col_list )


sps_query_string = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'hb_capital_shops'"
cursor.execute(sps_query_string)
s_columns_list = cursor.fetchall()
shops_col_list = list()
for item in s_columns_list:
    shops_col_list.append(item[0])
shops_df = pd.read_csv(shops_file, names = shops_col_list )

try:
    query_string1 = "ALTER TABLE hb_capital_credential_details DROP COLUMN name"
    cursor.execute(query_string1)
    conn.commit()
except:
    print("column does not exists")
        

query_string2 = "ALTER TABLE hb_capital_credential_details ADD name varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '名称'"
cursor.execute(query_string2)
conn.commit()


c=0
df_length = credentials_df.shape[0]
while c<df_length:
    result = credentials_df.iloc[c]['area_code']
    r = shops_df[shops_df['code'] == result]
    name = r.iloc[0]['title']
    print(r.iloc[0]['title'])
    print("")
    query = "UPDATE hb_capital_credential_details SET name ="+" '" +str(name)+"' "+ "WHERE area_code = "+"'"+result+"'"
    print(query)
    cursor.execute(query)
    conn.commit()

    c+=1












