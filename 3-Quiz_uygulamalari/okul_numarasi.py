okul_numarasi=input("Okul numaranızı giriniz:")

no=str(okul_numarasi)

ogrno = dict(GirisYili=no[:4], FakulteNo=no[4:6], BolumNo=no[6:8], OgrenimNo=no[8:9], OgrenciGirisSirasi=no[10:12])

print("NUMARANIN ACILIMI:")

print(type(ogrno))

for i in ogrno.items():
    print (i[0]+": "+i[1])
    
