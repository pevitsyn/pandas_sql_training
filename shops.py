# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:07:50 2021

@author: Vadym
"""
import os
import pandas as pd
import pyodbc
os.chdir("data")
structureFile = "组织结构.csv"
conn = pyodbc.connect(
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=credentials;'
    'UID=root;'
    'PWD=password;'
)

cursor = conn.cursor()

cursor.execute("SELECT level, code, name, pid FROM hb_areas;")
areas = cursor.fetchall()

for row in areas:
    row[2]=row[2][0]+row[2][1]


structureDF = pd.read_csv(structureFile)
structure_size=structureDF.shape[0]

i=0
while i < structure_size:
    result = structureDF.iloc[i]    
    shopid=result["SHOPID"]
    code=result["SHOPCODE"]
    title=result["SHOPNAME"]
    
    default_query_string = "INSERT INTO hb_capital_shops (shop_id, code, title) VALUES ("+str(shopid)+","+str(code)+","+"'"+title+"'"+")"

    try:
        match_string = title[0]+title[1]
    except:
        match_string=""

    if match_string:       
        for ch in areas:   
            if ch[2]==match_string:
                level=ch[0]
                area_code=ch[1]
                pid=ch[3]
                query_string = "INSERT INTO hb_capital_shops (shop_id, code, title, pid, level, area_code) VALUES ("+str(shopid)+","+str(code)+","+"'"+title+"'"+","+str(pid)+","+str(level)+","+str(area_code)+")"
                break
            else:
                query_string = default_query_string                       
    else:
        query_string = default_query_string          

    cursor.execute(query_string)
    conn.commit()


    i+=1       
 

    

