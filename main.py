import kmeans
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st

import class
import graph
import kmeans

df = pd.read_csv("score.csv", low_memory=False)
st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')

tab1, tab2, tab3, tab4 = st.tabs(['Danh sách', 'Biểu đồ', 'Phân nhóm', 'Phân loại'])
with tab1:
  
with tab2:
  graph()
with tab3:
  kmeans.kmeans()
with tab4:
  class()
