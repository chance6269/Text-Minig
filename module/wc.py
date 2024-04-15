# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:58:05 2024

@author: jcp
"""

# 워드클라우드 만들기
# - 워드클라우드는 Java 등 갖가지 문제점이 발생합니다. 버전 등을 잘 확인해주셔야 합니다.
# 제약사항:
 # 인수 df의 열이 2개이며 열 이름이 word, count이어야 함.
from . import add_font as af
# %%
def make_wordcloud(df, filename='wordcloud'):
    try:    
        from wordcloud import WordCloud # 워드클라우드 제작 라이브러리
        import matplotlib.pyplot as plt # 워드클라우드 시각화 라이브러리
        # df를 dict로 변환
        dic_word = df.set_index('word').to_dict()['count']
        
        # 워드클라우드 객체 생성
        wc = WordCloud(random_state = 123, font_path = f'{af.fontpath()}/NanumBarunGothic.ttf', width = 400,
                       height = 400, background_color = 'white')
    
        img_wordcloud = wc.generate_from_frequencies(dic_word)
    
        plt.figure(figsize = (10, 10)) # 크기 지정하기
        plt.axis('off') # 축 없애기
        plt.imshow(img_wordcloud) # 결과 보여주기
        plt.savefig(filename + '_wc') # 파일 저장
        plt.show()
    except Exception as e:
        print(e)

# %%

def make_img_wordcloud(df, filename, img_file):
    try:
        import numpy as np
        from wordcloud import WordCloud # 워드클라우드 제작 라이브러리
        import matplotlib.pyplot as plt # 워드클라우드 시각화 라이브러리
        import PIL
        icon = PIL.Image.open(img_file)
    
        img = PIL.Image.new('RGB', icon.size, (255,255,255))
        img.paste(icon, icon)
        img = np.array(img)
        # df를 dict로 변환
        dic_word = df.set_index('word').to_dict()['count']
        
        # 워드클라우드 객체 생성
        wc = WordCloud(random_state = 123, font_path = f'{af.fontpath()}/NanumBarunGothic.ttf', width = 400,
                       height = 400, background_color = 'white', mask=img, colormap='inferno')
    
        img_wordcloud = wc.generate_from_frequencies(dic_word)
    
        plt.figure(figsize = (10, 10)) # 크기 지정하기
        plt.axis('off') # 축 없애기
        plt.imshow(img_wordcloud) # 결과 보여주기
        plt.savefig(filename + '_mask_wc') # 파일 저장
        plt.show()
    except Exception as e:
        print(e)
    
# %%
    
if __name__ == "__main__":
    
    import pandas as pd # 데이터 프레임 라이브러리
    
    
    
    df = pd.read_csv('한산_댓글모음.csv')
    df
    
    df['Review'] = df['Review'].str.replace('[^가-힣]', ' ', regex = True)
    df['Review']
    
    import konlpy
    kkma = konlpy.tag.Kkma() #형태소 분석기 꼬꼬마(Kkma)
    
    nouns = df['Review'].apply(kkma.nouns)
    nouns
    
    # 5. 단어 데이터프레임 만들기
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

    make_wordcloud(df_word)
    # %%
    make_img_wordcloud(df_word,'한산_댓글모음' ,'bird.png')