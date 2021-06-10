

import os
import pandas as pd
from os import listdir
from os.path import isfile, join
os.chdir("data")
files = [f for f in listdir("files") if isfile(join("files", f))]
neededColumnsList = ["SHOPID","SHOPCODE","SHOPNAME","SHOPTYPE","PARENTID","ISUSED","MEMO","ONLYSHOP"]
resultDataframe = pd.DataFrame(columns = neededColumnsList)
#print(files)


# for file in files:
#     documentColumnsList = pd.read_csv(file, nrows=1).columns.tolist()
#     #print(documentColumnsList)

#     toExtractColumnsList = []
    
#     for i in documentColumnsList:
#         if i in neededColumnsList:
#             toExtractColumnsList.append(i)
#     print(file)
#     print(toExtractColumnsList)
    
            #df = pd.read_csv(i, usecols=toExtractColumnsList)


#print(df)


allColumnsList = []

for file in files:
    documentColumnsList = pd.read_csv(file, nrows=1).columns.tolist()    
    for i in documentColumnsList:
        if i not in allColumnsList:
            allColumnsList.append(i)
#print(allColumnsList)
            
count = {}            
for file in files:
    documentColumnsList = pd.read_csv(file, nrows=1).columns.tolist()
    for i in documentColumnsList:
        if i not in count:
            count[i] = 0
        else:
            count[i] += 1
print(count)

# documentColumnsList = pd.read_csv('会计科目表.csv', nrows=1).columns.tolist()
# #print(documentColumnsList)

# toExtractColumnsList = []

# for i in documentColumnsList:
#     if i in neededColumnsList:
#         toExtractColumnsList.append(i)

# #print(toExtractColumnsList)

# df = pd.read_csv('会计科目表.csv', usecols=toExtractColumnsList)

# #print(df["PARENTID"])

