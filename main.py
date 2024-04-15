# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:09:26 2024

@author: jcp
"""


from module import crawling
from module import preproc as pp
from module import visual
# %%
# 데이터 수집

crawling.crawling()

# %%
# 데이터 정제

pp.prerprocess()

# %%
# 데이터 시각화

visual.visualize()