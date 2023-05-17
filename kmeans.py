from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st

def kmeans():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)


  df['BONUS'].fillna(0, inplace = True)
  for i in range(1, 11):
    df[f"S{i}"].fillna(0, inplace = True)
  df['REG-MC4AI'].fillna("N", inplace = True)

  num= st.select_slider('Số nhóm', options=[1,2,3,4,5])

  X = df[['S6', 'S10', 'GPA']].to_numpy()
  kmeans = KMeans(n_clusters=num, random_state=0).fit(X)
  print(kmeans.labels_)
  x = df['S6'].values
  y = df['S10'].values
  z = df['GPA'].values

  fig = px.scatter_3d(x=x, y=y, z=z, color=kmeans.labels_)
  st.plotly_chart(fig, use_container_width=False)
  for i in range(num):
    dfi=df[kmeans.labels_==i]
    st.write('Nhóm' ,i+1, 'GPA cao nhất là',dfi['GPA'].values.max(),'thấp nhất là',dfi['GPA'].values.min(),' trung bình',round(dfi['GPA'].values.mean(),2))
    st.write(dfi.drop(columns=['GENDER','CLASS','PYTHON-CLASS','S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','BONUS','REG-MC4AI']))

