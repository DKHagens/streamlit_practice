import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd

iris = sns.load_dataset('iris')
df = pd.DataFrame(iris)
st.dataframe(df)

st.divider()

colors = st.multiselect('품종을 지정해주세요',
                        options = ['setosa','versicolor', 'virginica'],
                        default=['setosa'])

st.dataframe(iris[iris.species.isin(colors)])

columns = st.radio('컬럼을 선택하세요',
                   ['sepal_length','sepal_width',
                    'petal_length','petal_width'])
fig, ax = plt.subplots()
ax.hist(iris[columns])
st.pyplot(fig)

st.markdown(f'히스토그램 {columns}')
data = pd.read_excel('data/kor_news_240326.xlsx')

# ssort = st.radio('분류를 선택하세요',
#                    ['sepal_length','sepal_width',
#                     'petal_length','petal_width'])

from konlpy.tag import Okt, Kkma
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from collections import Counter

# def select_top_keywords()
# data = pd.read_excel('data/kor_news_240326.xlsx')
#
# categories = data.대분류.unique()
# cate = st.selectbox('분야를 선택하세요', categories)
# select_top_keywords(news, '제목', cate, 20)

import folium
import json
import os


with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
    geo_gg = json.loads(f.read())

def mapp(year):
    with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
        geo_gg = json.loads(f.read())
    map = folium.Map(location=[37.566535, 126.9779691999996], zoom_start=8)
    folium.GeoJson(geo_gg).add_to(map)
    folium.Choropleth(geo_data = geo_gg,
                  data = geo_gg[year],
                  columns = [geo_gg.index, geo_gg[year]],
                  key_on= 'feature.properties.name').add_to(map)
    st.folium(map, width=600, height=400)

tab1, tab2, tab3= st.tabs(['2007','2015','2017'])

with tab1:
    st.subheader('2007')
    mapp(2007)
with tab2:
    st.subheader('2015')
    mapp(2015)
with tab3:
    st.subheader('2017')
    mapp(2017)

#파일의 모듈화