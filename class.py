from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
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


 model = LogisticRegression()
 model.fit(X, y)
 weights = model.coef_[0]
 bias = model.intercept_[0]
 weights, bias
 w1, w2 = weights[0], weights[1]
 plt.scatter(X[y==0,0], X[y==0,1])
 plt.scatter(X[y==1,0], X[y==1,1])
 plt.legend(['S6', 'S-AVG', 'Decision Boundary'])
 plt.xlabel('S-AVG')
 plt.ylabel('S6')
 x1 = np.linspace(0,10,1000)
 x2 = -(w1*x1+bias)/w2
 plt.plot(x1,x2)
 st.pyplot(fig=None)
 

mhpf()
