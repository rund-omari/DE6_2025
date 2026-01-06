# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 14:21:14 2026

@author: SDK
"""
import pandas as pd  
import streamlit as st 
from PIL import Image
img_path = r"C:\Users\SDK\Desktop\rund\2026\DE6\mid project\dataset-cover (2).jpg"
img = Image.open(img_path)


st.header("Avocado data set ")
st.image(img)
link = "https://www.kaggle.com/datasets/neuromusic/avocado-prices"
st.text(f"data linck : {link}")

df , stat ,missing ,cols ,scaling,encoding = st.tabs(["data" ,
                                             "statistic",
                                             "missing data",
                                             "cols",
                                             "scaling",
                                             "encoding"])

with df :
    data = pd.read_csv(r"C:\Users\SDK\Desktop\rund\2026\DE6\mid project\avocado.csv")
    data.drop("Unnamed: 0",axis = 1 ,inplace = True)
    df.dataframe(data)

with stat:
    info , des = stat.tabs(["info" , "describe"]) 
    with info :
        info.text("""<class 'pandas.core.frame.DataFrame'>
        RangeIndex: 18249 entries, 0 to 18248
        Data columns (total 14 columns):
         #   Column        Non-Null Count  Dtype  
        ---  ------        --------------  -----  
         0   Unnamed: 0    18249 non-null  int64  
         1   Date          18249 non-null  object 
         2   AveragePrice  18249 non-null  float64
         3   Total Volume  18249 non-null  float64
         4   4046          18249 non-null  float64
         5   4225          18249 non-null  float64
         6   4770          18249 non-null  float64
         7   Total Bags    18249 non-null  float64
         8   Small Bags    18249 non-null  float64
         9   Large Bags    18249 non-null  float64
         10  XLarge Bags   18249 non-null  float64
         11  type          18249 non-null  object 
         12  year          18249 non-null  int64  
         13  region        18249 non-null  object 
        dtypes: float64(9), int64(2), object(3)
        memory usage: 1.9+ MB""")

    with des :
        des.subheader("numeric data")
        des.dataframe(data.describe())
        des.subheader("qat  data")
        des.dataframe(data.describe(include = "object"))

with missing :
    missing.dataframe(data.isna().sum())

with cols :
    sel_col = cols.selectbox("select column " , data.columns)
    cols.dataframe(data[sel_col].describe())
    cols.text(f"missing value : {data[sel_col].isna().sum()}")
    cols.text(f"{data[sel_col].dtype}")
    if data[sel_col].dtype == "object" :
        cols.dataframe(data[sel_col].value_counts())

#with encoding :
    