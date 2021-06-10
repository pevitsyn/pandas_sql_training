# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:13:37 2021
@author: Vadym

This script copies needed columns from 组织结构.csv file into a pandas dataframe
Matches first two characters of shop names with the list of first two characters of areas taken from database
If there is a match it grabs corresponding area code and put it into the database
For correct processing of chineese characters I changed the coding in 组织结构.csv to utf-8

"""

import os
import pandas as pd
import pyodbc

conn = pyodbc.connect(
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=mydatabase;'
    'UID=root;'
    'PWD=password;'
)

cursor = conn.cursor()

# Take areas names with areas codes from database
cursor.execute("SELECT name,code FROM hb_areas;")
areas = cursor.fetchall()

# Trim areas to two first characters
for row in areas:
    row[0]=row[0][0]+row[0][1]
    
os.chdir("data")
structureFile = "组织结构.csv"

# Read shops data from file
structureDF = pd.read_csv(structureFile)
structure_size=structureDF.shape[0]

i=0
while i < structure_size:
    result = structureDF.iloc[i]    
    shopid=result["SHOPID"]
    shopcode=result["SHOPCODE"]
    shopname=result["SHOPNAME"]
    shoptype=result["SHOPTYPE"]
    parentid=result["PARENTID"]
    
    default_query_string = "INSERT INTO hb_capital_shops (shopid, shopcode, shopname, shoptype, parentid, updated_at) VALUES ("+str(shopid)+","+str(shopcode)+","+"'"+shopname+"'"+"," +str(shoptype)+","+str(parentid)+",current_timestamp)"

# There is one shop name with only one character in the file so I am doind a check    
    try:
        match_string = shopname[0]+shopname[1]
    except:
        match_string=""

# If there is a match between two first characters of area and shop name put the row with area code to database. If no put record without area code        
    if match_string:        
        for ch in areas:
    
            if ch[0]==match_string:
                area_code=ch[1]
                query_string = "INSERT INTO hb_capital_shops (shopid, shopcode, shopname, shoptype, parentid, area_code, updated_at) VALUES ("+str(shopid)+","+str(shopcode)+","+"'"+shopname+"'"+"," +str(shoptype)+","+str(parentid)+","+str(area_code)+",current_timestamp)"
                #print(area_code)
                break
            else:
                query_string = default_query_string                        
    else:
        query_string = default_query_string          

    cursor.execute(query_string)
    conn.commit()

# created_at record must be set only once when the row is created so if created_at data is empty which means the record just created we put timestamp
    query_string = "SELECT created_at FROM hb_capital_shops WHERE shopid = "+str(shopid)
    cursor.execute(query_string)
    is_created = cursor.fetchone()[0]
    if not is_created:
            query_string = "UPDATE hb_capital_shops SET created_at = current_timestamp WHERE shopid ="+str(shopid)
            cursor.execute(query_string)
            conn.commit()
    i+=1       
 

    

