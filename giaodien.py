import kmeans
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st

 df = pd.read_csv("py4ai-score.csv", low_memory=False)
 df['BONUS'].fillna(0, inplace = True)
 for i in range(1, 11):
   df[f"S{i}"].fillna(0, inplace = True)
 df['REG-MC4AI'].fillna("N", inplace = True)

option = st.selectbox('Chọn mục', ('Danh sách', 'Biểu đồ', 'Phân nhóm', 'Phân loại'))
if option =='Phân nhóm':
  kmeans.kmeans()
