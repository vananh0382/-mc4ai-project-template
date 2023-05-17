from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("py4ai-score.csv", low_memory=False)
df['BONUS'].fillna(0, inplace = True)
for i in range(1, 11):
 df[f"S{i}"].fillna(0, inplace = True)
df['REG-MC4AI'].fillna("N", inplace = True)

avg = []
for i in df.index:
  r = df.loc[i][4:13]
  avg.append(r.mean())
df['S-AVG'] = avg

def mhpf():
  X = df[['S6','S-AVG']].values.copy()
  y = []
  for i in range(len(df[['NAME']])):
    if X[i][0] >= 6 and X[i][1] >= 6:
      y.append(1)
    else:
      y.append(0)
  y = np.array(y)
  plt.scatter(X[y==0,0], X[y==0,1])
  plt.scatter(X[y==1,0], X[y==1,1])
  plt.legend(['S6', 'S-AVG'])
  plt.xlabel('S-AVG')
  plt.ylabel('S6')
  plt.show()
  st.pyplot(fig=None)

mhpf()
