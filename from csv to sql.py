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
credentials_file = "hb_capital_credentials.csv"
conn = pyodbc.connect(
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=credentials;'
    'UID=root;'
    'PWD=password;'
)
cursor = conn.cursor()

def isNaN(num):
    return num!= num

query_string = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'hb_capital_credentials'"
cursor.execute(query_string)
columns_list = cursor.fetchall()
items = list()
for item in columns_list:
    items.append(item[0])

credentials_df = pd.read_csv(credentials_file, names = items )




query_string1 = "INSERT INTO hb_capital_credentials ("
query_string2 = ""
execute_query_string =""
c=0

df_length = credentials_df.shape[0]
while c<df_length:
    result = credentials_df.iloc[c]
    
    i=0
    items_length = len(items)
    while i<items_length:
        value = result[items[i]]
        if i == items_length-1:
            query_string1 = query_string1+items[i]+") VALUES ( "
            if isNaN(value):
                query_string2 = query_string2+"null"+")"
            else:
                query_string2 = query_string2+"'"+str(value)+"'"+")"
        else:
            query_string1 = query_string1+items[i]+", "
            if isNaN(value):
                query_string2 = query_string2+"null"+", "
            else:
                query_string2 = query_string2+"'"+str(value)+"'"+", "
        i+=1
    final_query_string = query_string1+""+query_string2
    execute_query_string = execute_query_string + final_query_string + "; "
    query_string1 = "INSERT INTO hb_capital_credentials ("
    query_string2 = ""
    final_query_string = ""    
    c+=1

print(execute_query_string)
cursor.execute(execute_query_string)
conn.commit()










