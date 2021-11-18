# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:22:28 2020

@author: admin
"""



# make sure that excels are not having error while opening
# if error is there open the file and sve as xls format with same name(replace file )
# copy paste this code file in the folder where combined files are present

#file1 = 'BLR ECE IV SEM1.xls'
#df1 = pd.read_excel(file1)
import os
import pandas as pd
cwd = os.path.abspath('') 
files = os.listdir(cwd) 

df = pd.DataFrame()
for file in files:
     if file.endswith('.xls'):
         df = df.append(pd.read_excel(file), ignore_index=True) 
#df.head()

writer1 = pd.ExcelWriter('D:/excelCombine/combinedFile.xls')
df.to_excel(writer1, index=False) # index false to drop first index colum that adds with dataframe in the output
# save the excel
writer1.save()