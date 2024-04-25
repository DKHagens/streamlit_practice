from konlpy.tag import Okt, Kkma
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from collections import Counter
import streamlit as st
import seaborn as sns

file_path='data/kor_news_240326.xlsx'

data = pd.read_excel('data/kor_news_240326.xlsx')
st.dataframe(data,
                column_config={
                    'URL' : st.column_config.LinkColumn(
                        display_text= '뉴스 기사로 이동',
                   )
               })

font_name= font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)
font_path='c:/Windows/Fonts/malgun.ttf'

data['분류리스트']=data.분류.str.split('>')

data['대분류'] = data.분류리스트.str[0]
data['중분류'] = data.분류리스트.str[1]
data['소분류'] = data.분류리스트.str[2]

Sort_cnt = data.대분류.value_counts()
st.bar_chart(Sort_cnt)

title_str = str(list(data.제목))
def text_p_proc(str):
    okt = Okt()
    const = okt.nouns(str)
    const = [token for token in const if len(token)>1]
    return const

title_const= text_p_proc(title_str)

def Counter_const(const):
    cnt_const = Counter(const)
    df_cnt_const = pd.DataFrame(pd.Series(cnt_const), columns=['Freq'])
    s_const = df_cnt_const.sort_values(by='Freq', ascending=False)
    return s_const

s_title_const = Counter_const(title_const)
top20 = s_title_const.iloc[:20]

st.bar_chart(top20)

fig, ax = plt.subplots()
ax.bar(data=top20, x=top20.index, height='Freq')
plt.xticks(rotation=40)
st.pyplot(fig)


fig = plt.figure(figsize=(7,5))
df = top20.iloc[:20]
sns.barplot(data=df, x='Freq', y=df.index)
plt.title('Top20 단어 빈도그래프')
st.pyplot(fig)
