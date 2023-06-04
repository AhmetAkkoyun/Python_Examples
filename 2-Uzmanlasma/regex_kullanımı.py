# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:01:23 2021

@author: ahmet
"""

########################
##                    ##
##  Regex Kullanımı   ##
##  Desen Eşleştirme  ##
##                    ##
########################

# yazı içinde arama yapma

import re

cumle = "Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir (Unix, Linux, Mac, Windows, Amiga, Symbian). Python ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, web programlama, uygulama ve veri tabanı yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir. Python 1980'lerin sonunda ABC programlama diline alternatif olarak tasarlanmıştı. Python 2.0, ilk kez 2000 yılında yayınlandı. 2008'de yayınlanan Python 3.0, dilin önceki versiyonuyla tam uyumlu değildir ve Python 2.x'te yazılan kodların Python 3.x'te çalışması için değiştirilmesi gerekmektedir. Python 2 versiyonun resmi geliştirilme süreci, dilin son sürümü olan Python 2.7.x serisi versiyonların ardından 1 Ocak 2020 itibarıyla resmi olarak sona erdi.[5][6] Python 2.x geliştirilme desteğinin sona ermesinin ardından, Python dilinin 3.6.x ve sonraki sürümlerinin geliştirilmesi devam etmektedir."

patern = "Python"              # büyük küçük harfe duyarlıdır

sonuc = re.search(patern, cumle) 
print(sonuc)   # yazının hangi karakterlerinde olduğunu verir span(175, 181)

print(sonuc.start(), "ile ", sonuc.end(), "arasında") # böyle de yazılır

print("******************************************************")

"""
for bulunan in re.finditer(patern, cumle):
    print(bulunan.span(), bulunan.group())  # tüm python kelimelerini bulur
"""    
    
# kaç adet bulduğunu yazmak istersek de

x = 0
for bulunan in re.finditer(patern, cumle):
    print(bulunan.span(), bulunan.group())
    x=x+1

print(x, " adet sonuç bulunmuştur.")      


print("******************************************************")

# desen eşleştirme
# ne arayacağımızı bilmiyorsak. yani bir telefon no arıyoruz ama numara bilmiyoruz.


cumle2 = "merhaba benim cep numaram 532-1112233 beni öğleden sonra arayabilirsiniz.. ulaşamazsanız 532-2223344 numaralı telefonu arayın"

# rakamlar için \d    yani digit
# harfler için \w     yani word
# boşluk için \d      yani space
# ... 

patern2 = "\d\d\d-\d\d\d\d\d\d\d"   # 3 rakam sonra tire sonra 7 rakam

sonuc2 = re.search(patern2, cumle2)

print(sonuc2)   # span=(26, 37), match='532-1112233' şeklinde ilk gördüğünü yazdı

print("******************************************************")

# tüm numaraları bulduralım

for bulunan in re.finditer(patern2, cumle2):
    print(bulunan.span(), bulunan.group())    # iki numarayı da sırayla yazdı.
    
