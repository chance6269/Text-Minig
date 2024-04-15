# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:13:40 2024

@author: jcp
"""
# 3. 데이터 시각화
def visualize():
    import pandas as pd
    # 엑셀 파일 읽어오기
    selected_pp = pd.read_excel('./data/selected_pp.xlsx')
    pp_all = pd.read_excel('./data/all_pp.xlsx')

    selected_d = pd.read_excel('./data/selected_d.xlsx')
    d_all = pd.read_excel('./data/all_d.xlsx')
    
    # 상위 20개
    top20_selected = selected_d[:20]
    top20 = d_all[:20]
    
    # 상위 10개
    top10_selected = selected_d[:10]
    top10 = d_all[:10]
    
    from module import wc
    from module import bar_wc as bw

    # 불용어 제거 후
    
    # 막대차트
    bw.bar_wordcount(top10_selected, './img/selected_d')
    bw.barh_wordcount(top10_selected, './img/selected_d')

    bw.bar_wordcount(top10, './img/speeches_d')
    bw.barh_wordcount(top10, './img/speeches_d')

    # 워드클라우드
    wc.make_wordcloud(top20_selected, './img/selected_d')
    wc.make_img_wordcloud(top20_selected, './img/selected_d', './module/bird.png')

    wc.make_wordcloud(top20, './img/speeches_d')
    wc.make_img_wordcloud(top20, './img/speeches_d', './module/bird.png')
    
    
    # 불용어 제거 안한 것 막대차트
    
    top20_sd = selected_pp[:20]
    top20_nd = pp_all[:20]
    
    bw.bar_wordcount(top20_sd, './img/selected')
    bw.barh_wordcount(top20_sd, './img/selected')

    bw.bar_wordcount(top20_nd, './img/speeches')
    bw.barh_wordcount(top20_nd, './img/speeches')

# %%
