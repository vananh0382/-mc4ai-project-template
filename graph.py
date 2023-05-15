import streamlit as st
import re
import pandas as pd
import plotly.express as px

df = pd.read_csv("py4ai-score.csv", low_memory=False)
st.title('BẢNG ĐIỂM LỚP PY4AI 09/2022')

def sohs():
    def xulyfile():
        df['S1'].fillna(0, inplace=True)
        df['S2'].fillna(0, inplace=True)
        df['S3'].fillna(0, inplace=True)
        df['S4'].fillna(0, inplace=True)
        df['S5'].fillna(0, inplace=True)
        df['S6'].fillna(0, inplace=True)
        df['S7'].fillna(0, inplace=True)
        df['S8'].fillna(0, inplace=True)
        df['S9'].fillna(0, inplace=True)
        df['S10'].fillna(0, inplace=True)
        df['BONUS'].fillna(0, inplace=True)
        df['REG-MC4AI'].fillna('N', inplace=True)

    st.write('BIỂU ĐỒ MÔ TẢ SỐ LƯỢNG HỌC SINH NAM VÀ NỮ')
    px.pie(df, names = 'GENDER')
    st.write('Kết luận: ')

    def khoi():
        if df['CLASS'].str.startswith('10'):
            return 'Khối 10'
        else:
            return 'Khối 11 và 12'
    df['KHỐI'] = df.apply(khoi, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH KHỐI 10 VÀ HỌC SINH HAI KHỐI CÒN LẠI')
    px.pie(df, names = 'KHỐI')
    st.write('Kết luận: ')

    def cg():
        if re.search('..CV.', df['CLASS']):
            return 'Chuyên Văn'
        elif re.search('..CT.$', df['CLASS']):
            return 'Chuyên Toán'
        elif re.search('..CL.', df['CLASS']):
            return 'Chuyên Lý'
        elif re.search('..CH.', df['CLASS']):
            return 'Chuyên Hoá'
        elif re.search('..CA.', df['CLASS']):
            return 'Chuyên Anh'
        elif re.search('..CTIN', df['CLASS']):
            return 'Chuyên Tin'
        elif re.search('..CTRN', df['CLASS']):
            return 'Chuyên Trung Nhật'
        elif re.search('..CSD', df['CLASS']):
            return 'Chuyên Sử Địa'
        elif re.search('..TH.', df['CLASS']) or re.search('..SN', df['CLASS']):
            return 'Tích Hợp/Song Ngữ'
        else:
            return 'Khác'
    df['CLASS GROUP'] = df.apply(cg, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH Ở CÁC LỚP CHUYÊN')
    px.pie(df, names = 'CLASS GROUP')
    st.write('Kết luận: ')

    def ca():
        if df['PYTHON-CLASS'].str.endswith('S'):
            return 'SÁNG'
        else:
            return 'CHIỀU'
    df['CA HỌC'] = df.apply(ca, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH CHỌN CA HỌC')
    px.pie(df, names = 'CA HỌC')
    st.write('Kết luận: ')
    
    def pf():
        if df['GPA'] >= 6:
            return 'Pass'
        else:
            return 'Fail'
    df['Pass/Fail'] = df.apply(pf, axis=1)
    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH ĐẬU LÊN LỚP MC')
    px.pie(df, names = 'PASS/FAIL')
    st.write('Kết luận: ')

    st.write('BIỂU ĐỒ MÔ TẢ SỐ HỌC SINH ĐĂNG KÍ HỌC TIẾP LỚP MC4AI')
    px.pie(df, names = 'REG-MC4AI')
    st.write('Kết luận: ')
