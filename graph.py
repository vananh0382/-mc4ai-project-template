import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("py4ai-score.csv", low_memory=False)
st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')
