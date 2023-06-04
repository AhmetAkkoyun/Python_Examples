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


# karşılaştırılacak keywords listesi
kw_list = ["PYTHON", "JAVA", "C#", "FORTRAN",]


# payload build işlemi yapıyoruz ÜLKEYİ SEÇİYORUZ
pytrends.build_payload(kw_list, cat=None, timeframe='2000-01-01 2021-11-30', geo='TR')


# zamana göre dağılımı isteyelim
df = pytrends.interest_over_time()


# data frame'i excel olarak kaydet
df.to_excel("testfile.xls")


# tarihe göre çizim yaptıralım
plt.figure(figsize=(50, 50))
plt.plot(df.index,df[kw_list[0]],'k*')
plt.plot(df.index,df[kw_list[1]],'r*')
plt.plot(df.index,df[kw_list[2]],'y*')
plt.plot(df.index,df[kw_list[3]],'g*')
plt.legend(kw_list)

plt.show()


# detaylı bilgi ve metodlar için https://pypi.org/project/pytrends/









