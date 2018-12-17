# -*- coding: utf-8 -*-

# import necessary libraries

import pandas as pd
from slugify import slugify

# read input data
fn = "Keywords.xlsx"
df = pd.read_excel(fn)

# create extra columns
df['english_urls'] = ""
df['deutsch_urls'] = ""
df['japan_urls'] = ""
df['arabic_urls'] = ""

# make urls iteratively
for index in range(len(df)):
    df['english_urls'][index] = 'https://www.example.com/'+slugify( df['English'][index]) + "/"
    df['deutsch_urls'][index] = 'https://www.example.com/'+slugify( df['deutsch'][index]) + "/"
    df['japan_urls'][index] = 'https://www.example.com/'+slugify( df['japan'][index]) + "/"
    df['arabic_urls'][index] = 'https://www.example.com/'+slugify( df['arabic'][index]) + "/"

# make comportable orfer of columns
df = df[['English','english_urls','deutsch','deutsch_urls','japan','japan_urls','arabic','arabic_urls']]

# save rusults
writer = pd.ExcelWriter(fn)
df.to_excel(writer, 'Sheet1',index = False)
writer.save()
