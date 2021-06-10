# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:57:02 2021

@author: Vadym
"""
import pandas as pd
import os
import numpy as np
os.chdir('data')
assets_file ='资产信息.csv'
structure_file = "组织结构.csv"
assets_df = pd.read_csv(assets_file)
structure_df = pd.read_csv(structure_file)
assets_df=assets_df.filter(["ASSETID","SHOPID","ASSETSNAME","ASSETSTYPEID","UNITNAME","ADDRESS"], axis=1)
assets_df.insert(2, 'SHOPNAME', np.nan, True)
i = 0
size = assets_df.shape[0]
while i < size:
    res = assets_df.iloc[i]['SHOPID']
    r = structure_df[structure_df['SHOPID'] == res]
    # print(r)
    name = r.iloc[0]['SHOPNAME']
    print(name)
    assets_df.iloc[i,2] = name
    

    i+=1
assets_df.to_csv("assets.csv")    
print(assets_df)