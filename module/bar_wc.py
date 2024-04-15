# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:14:33 2024

@author: jcp
"""

# 막대그래프, 가로 막대그래프 함수 모듈 :
    # bar_wordcount(df, 저장할 파일 이름)
    # barh_wordcount(df, 저장할 파일 이름)
from . import add_font as af
# %%
def bar_wordcount(df, filename):
    try:
        import matplotlib.pyplot as plt
        
        af.reg()
        make_bar(df['word'], df['count'])
        plt.title('단어별 빈도수')
        plt.savefig(filename + '_bar')
        plt.show()
    except Exception as e:
        print(e)

# %%
def make_bar(x_col, y_col):
    try:
        import matplotlib.pyplot as plt
        plt.rc('font', family='NaNumBarunGothic')
        plt.rcParams['figure.dpi'] = 140
        
        bar = plt.bar(x_col, y_col, width=0.6)
        
        plt.xticks(rotation=55)
        # 막대 위 값 표시
        for rect in bar:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1d' % height, ha='center', va='bottom', size = 6, color='r')        
    except Exception as e:
        print(e)
# %%
def barh_wordcount(df, filename):
    try:
        import matplotlib.pyplot as plt
        af.reg()
        df = df.sort_values(by=['count'], ascending=True) 

        make_barh(df['word'], df['count'])
        plt.title('단어별 빈도수')
        plt.savefig(filename + '_barh')
        plt.show()
    except Exception as e:
        print(e)

# %%
def make_barh(x_col, y_col):
    try:
        import matplotlib.pyplot as plt
        plt.rc('font', family='NanumBarunGothic')
        plt.rcParams['figure.dpi'] = 140
        
        barh = plt.barh(x_col, y_col, height=0.6)
        
        plt.yticks(fontsize=8)
        # for rect in barh:
            # width = rect.get_width()
            # plt.text(width + 1.5, rect.get_y() - 0.15, '%.1d' % width, ha='center', va='bottom', size = 7, color='g')
    except Exception as e:
        print(e)
    
# %%
if __name__ == "__main__":
    
    import pandas as pd # 데이터 프레임 라이브러리
       
    af.reg()

    df = pd.read_csv('한산_댓글모음.csv')
    df

    df['Review'] = df['Review'].str.replace('[^가-힣]', ' ', regex = True)
    df['Review']

    import konlpy
    kkma = konlpy.tag.Kkma() #형태소 분석기 꼬꼬마(Kkma)

    nouns = df['Review'].apply(kkma.nouns)
    nouns

    # 단어 데이터프레임 만들기
    nouns = nouns.explode()
    nouns

    # 두 글자 이상만
    df_word = pd.DataFrame({'word' : nouns})
    df_word['count'] = df_word['word'].str.len()
    df_word = df_word.query('count >= 2')
    df_word

    df_word = df_word.groupby('word', as_index = False).count().sort_values('count', ascending = False)
    df_word

    # 영화처럼 불필요한 단어 제거
    df_word = df_word.iloc[1:, :]
    df_word.head(5)

    top20 = df_word.head(20)
    
    bar_wordcount(top20,'한산_댓글모음')
    barh_wordcount(top20,'한산_댓글모음')