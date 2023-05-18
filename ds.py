import streamlit as st
import pandas as pd
import numpy as np 

df = pd.read_csv("py4ai-score.csv", low_memory=False)
df['BONUS'].fillna(0, inplace = True)
for i in range(1, 11):
 df[f"S{i}"].fillna(0, inplace = True)
df['REG-MC4AI'].fillna("N", inplace = True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.write('Giới tính')
    male = st.checkbox('Nam')
    fem = st.checkbox('Nữ')
    if male:
        dfg = df[df['GENDER']=='M']
    elif fem:
        dfg = df[df['GENDER']=='F']
    elif male and fem: 
        dfg = df

with col2: 
    khoi = st.radio('Khối lớp', ('Tất cả', 'Lớp 10', 'Lớp 11', "Lớp 12"), horizontal=True)
    if khoi == 'Lớp 10':
     dfk = dfg[dfg['CLASS'].str.startswith('10')]
    elif khoi == 'Lớp 11':
     dfk = dfg[dfg['CLASS'].str.startswith('11')]
    elif khoi == 'Lớp 12':
     dfk = dfg[dfg['CLASS'].str.startswith('12')]

with col3: 
    AI_class = st.selectbox('Phòng', ('Tất cả','A114', 'A115'))
    if AI_class == 'A114':
     dfai = dfk[dfk['PYTHON-CLASS'].str.startswith('114')]
    elif AI_class == 'A115':
     dfai = dfk[dfk['PYTHON-CLASS'].str.startswith('115')]
with col4: 
    times = st.multiselect('Buổi', ['Sáng','Chiều'])
    if times == 'Sáng':
     dft = dfai[dfai['PYTHON-CLASS'].str.endswith('S')] 
    elif times == 'Chiều':
     dft = dfai[dfai['PYTHON-CLASS'].str.endswith('C')]
    else: dft = dfai
st.write(dft)
lc = st.write('Lớp chuyên')
cola, colb, colc, cold, cole = st.columns(5)
with cola:
    math = st.checkbox('Toán')
    literature = st.checkbox('Văn')
    
    
with colb:
    ly = st.checkbox('Lý')
    hoa = st.checkbox('Hóa')
with colc:
    eng = st.checkbox('Anh')
    tin = st.checkbox('Tin')
with cold:
    su_dia = st.checkbox('Sử Địa')
    tr_n = st.checkbox('Trung Nhật')
with cole:
    th_sn = st.checkbox('TH/SN')
    diff = st.checkbox('Khác')
