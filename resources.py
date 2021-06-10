# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:43:13 2021

@author: Vadym
"""

import os
import pandas as pd

os.chdir("data")

resources_file = "资源信息.csv"
resources_df = pd.read_csv(resources_file)
filtered_df = resources_df.filter(["EAST","RENT_NUM","UNITNAME","USESTATUS","WEST","NORTH","SOUTH","CHARGEMAN","OPDATE","INTDATE"], axis=1)
d1 = {'RESOURCEID': [], 'RESOURCENAME': [], 'RESOURCETYPE': [], 'RESOURCECODE': [], 'STATUS_DETAIL':[]}
df = pd.DataFrame(d1)

checklist = ('路','建','宅','基','学')

c=0
df_length = resources_df.shape[0]
while c<df_length:
    row = filtered_df.iloc[c]
    status_detail = row.to_json(force_ascii=False)
    name = resources_df.iloc[c]['RESOURCENAME']
    resuorceid = resources_df.iloc[c]['RESOURCEID']
    for word in checklist:
        if word in name:
            resourcetype = '建设用地'
            resourcecode = '2'
            break
        else:
            resourcetype = '农用地'
            resourcecode = '1'
    new_row = {'RESOURCENAME':name, 'RESOURCEID':resuorceid, 'RESOURCETYPE':resourcetype, 'RESOURCECODE':resourcecode,  'STATUS_DETAIL':status_detail}
    df = df.append(new_row, ignore_index=True)
    c+=1
print(df)
df.to_csv("resourcetypes.csv")

