# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 17:21:24 2021

@author: Vadym
"""

import pandas as pd

d1 = {'Name': ['Pankaj', 'Meghna'], 'ID': [1, 2], 'Role': ['CEO', 'CTO']}

df = pd.DataFrame(d1)
print('DataFrame:\n', df)
df.to_csv("csvfile.csv")

# default CSV
csv_data = df.to_csv()
print('\nCSV String:\n', csv_data)

pd.read_csv("csvfile.csv")
