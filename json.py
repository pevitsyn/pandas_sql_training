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
#print(resources_df)
filtered_df = resources_df.filter(["EAST","RENT_NUM","UNITNAME","USESTATUS","WEST","NORTH","SOUTH","CHARGEMAN","OPDATE","INTDATE"], axis=1)
#print(filtered_df)
row = filtered_df.iloc[0]

print(row)

row1 = row.to_json(force_ascii=False)

print(row1)
print("")
s='{"EAST":"0","RENT_NUM":0.0,"UNITNAME":"\u4ea9","USESTATUS":1,"WEST":"0","NORTH":"0","SOUTH":"0","CHARGEMAN":"\u6768\u7ea2\u5149","OPDATE":"2011-01-24","INTDATE":"2009-10-24"}'
print(s)
a='\u4ea9'
print(a)
# str1 = '\\\\u4ea9'
# print(str1.encode('utf-8'))


