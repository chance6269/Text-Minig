# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:43:42 2024

@author: jcp
"""
# 2. 데이터 정제
def prerprocess():
    # 엑셀파일 읽어오기
    import pandas as pd
    df_selected = pd.read_excel('./data/selected_speeches.xlsx')

    df_list = []

    for i in range(1,87):
        df_list.append(pd.read_excel(f'./data/speeches{i}.xlsx'))

    from module import pp

    selected_pp = pp.preprocess(df_selected)
    new_idx = pd.RangeIndex(len(selected_pp))
    selected_pp = selected_pp.set_index(new_idx)

    pp_list = []
    
    for speeches in df_list:
        pp_list.append(pp.preprocess(speeches))

    # 연설문 전체 합치는 부분
    pp_all = pp_list[0]

    for pp_speeches in pp_list[1:]:
        
        pp_all = pd.concat([pp_all, pp_speeches])

    pp_all = pp_all.groupby('word').sum().sort_values(by='count', ascending=False)

    pp_all.reset_index(inplace=True)

    del_list = ['세계','정부', '국민','니다']
    selected_d = selected_pp.loc[~selected_pp['word'].isin(del_list)]
    d_all = pp_all.loc[~pp_all['word'].isin(del_list)]

    # 엑셀 저장
    # 불용어 처리 전
    selected_pp.to_excel('./data/selected_pp.xlsx', index=False)
    pp_all.to_excel('./data/all_pp.xlsx',index=False)

    # 불용어 처리
    selected_d.to_excel('./data/selected_d.xlsx', index=False)
    d_all.to_excel('./data/all_d.xlsx', index=False)
# %%


