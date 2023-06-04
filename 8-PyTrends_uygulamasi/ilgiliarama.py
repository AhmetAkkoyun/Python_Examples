# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:06:52 2021

@author: ahmet
"""

##################################
##                              ##
## GOOGLE TRENDS KARŞILAŞTIRMA  ##
##                              ##
##################################


import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends = TrendReq()


kw_list=['fenerbahçe']

# payload build işlemi yaparken keyword listemizi oluşturalım.
# bu kez tek anahtar kelime üzerinden analizler yapacağız
pytrends.build_payload(kw_list, timeframe='2015-01-01 2021-11-30', geo='TR')


# related topicsleri bulalım
df_rt = pytrends.related_topics()

lst = df_rt[kw_list[0]]


# rising ile ilgili dataframe bize aranan kelime ile ilgili yükselen arama trendini verir
rising_values = df_rt[kw_list[0]]['rising']


# print(rising_values.head())   # konuları başlıkları vs görmek için aç



df_rq = pytrends.related_queries()  # alakalı aramaları görmek için aç
# print(df_rq[kw_list[0]]['rising'].head())  # rising ifadesi top olarak değişebilir


print(pytrends.top_charts(date='2014', geo="TR"))  # belirtilen ülkede ve yılda en çok yapılan arama


# detaylı bilgi ve metodlar için https://pypi.org/project/pytrends/









