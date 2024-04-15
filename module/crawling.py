# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:22:37 2024

@author: jcp
"""

def crawling():
    # 사건 직전 연설문 id들
    selected = []
    selected += list(range(1309257,1309263)) # 연평해전 : 1309257~1309262
    selected += [1310208, 1310209] # 금강산 관광객 피살 : 1310208~1310209
    selected += [1330395, 1330298] # 천안함 피격 : 1330395, 1330298
    selected += [1330411] # 연평도 포격 : 1330411
    selected += [1400325,1400326,1400327] # 목함지뢰 : 1400325,1400326,1400327
    selected += [1400332] # 서부전선 포격사건 : 1400332
    selected += list(range(1401215, 1401218))+[1401939, 1401940] # 연락망 폭파 사건 : 1401939, 1401216, 1401215, 1401940, 1401217
    selected += [1401955] + list(range(1401258, 1401264)) # 공무원 피살 사건 : 1401955, 1401258~1401263

    # 대통령별 게시물id [시작, 끝]
    kim = [1308526, 1309346]
    roh = [1309348, 1310126]
    lee = [1330066, 1331000]
    lee2 = [1310127, 1310336]
    park = [1400001, 1400493]
    moon = [1400600, 1402000]
    all_president = [kim, roh, lee, lee2, park, moon]

    # 크롤링
    from module import sps

    selected_speeches = []

    speeches = []
    speeches_list = []

    speeches_all = []
    k = 0

    for president in all_president:
        
        for idn in range(president[0], president[1] + 1):
            
            speech = sps.scrape_presidential_speech(idn)
            
            if len(speech) > 0:   
                if idn in selected:
                    selected_speeches.append(speech)
                else:
                    speeches.append(speech)
                    speeches_all.append(speech)
                    k += 1
            
            if (k > 0 and k % 50 == 0) \
                or idn == all_president[-1][-1]:
                speeches_list.append(speeches)
                speeches = []
                
                print('[크롤링 종료]')
                print('마지막 artid: ', idn)
                
    print('연설문 수 : ', k)

    # excel파일로 저장
    import pandas as pd

    df_selected = pd.DataFrame({"연설문": selected_speeches})
    df_selected.to_excel('./data/selected_speeches.xlsx', index=False)

    # 연설문 전체 excel파일로 저장

    i = 1
    for speeches in speeches_list:
        df_speeches = pd.DataFrame({'연설문':speeches})
        df_speeches.to_excel('./data/speeches{}.xlsx'.format(i), index=False)
        i += 1
