import kmeans
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st



option = st.selectbox('Chọn mục', ('Danh sách', 'Biểu đồ', 'Phân nhóm', 'Phân loại'))
if option =='Phân nhóm':
  kmeans.kmeans()
