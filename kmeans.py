from sklearn.cluster import KMeans
import pandas as pd
import numpy as np 
import plotly.express as px
df = pd.read_csv("py4ai-score.csv", low_memory=False)


df['BONUS'].fillna(0, inplace = True)
for i in range(1, 11):
  df[f"S{i}"].fillna(0, inplace = True)
df['REG-MC4AI'].fillna("N", inplace = True)

X = df[['S6', 'S10', 'GPA']].to_numpy()
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
print(kmeans.labels_)
x = df['S6'].values
y = df['S10'].values
z = df['GPA'].values

fig = px.scatter_3d(x=x, y=y, z=z, color=kmeans.labels_)
st.plotly_chart(fig, use_container_width=False)

print(df[kmeans.labels_==0])
print(df[kmeans.labels_==1])
print(df[kmeans.labels_==2])
