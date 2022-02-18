import random
    
def tarih_hesapla(gun, ay, yil):
         return gun, ay, yil
fiyat=5
gun, ay, yil=1, 1, 2021
if yil %4==0:
       gun_sayisi=366
else:
        gun_sayisi=365
f=open("fiyattakibi.txt" "w")
for i in range(gun_sayisi):
f.write(str(gun)) + " - "+ str(ay) + "-" + str(yil)+ ":" + str(fiyat)+ "\n")
def bir_sonraki_gunu_hesapla(gun, ay,yil):
        gun+=1
        if ay in [1, 3, 5, 7, 8, 10, 12] and gun >31:
                gun=1
                ay+=1
        elif ay in[4, 6, 9,11] and gun >30:
           gun = 1
           ay+ =1
        elif ay == 2:
                if yil % 4 ==0 and gun >29:
                elif yil %4 !=0 and gun>28:
           gun=1
           ay+=1

        return gun, ay, yil
 for i in range(gun_sayisi):
f.write(str(gun)) + " - "+ str(ay) + "-" + str(yil)+ ":" + str(fiyat)+ "\n")       
gun,ay,yil=bir-bir_sonraki_gunu_hesapla(gun,ay,yil) 
fiyat+=random.randit(-1, 3) 
if  fiyat < 1:
        fiyat= 1       
#yillik fiyat ortalamasinin hesabi:
try: #dosyayi korumaya aliyoruz kazara bozariz diye
def yillik_ortalama_hesap
f =open("fiyattakibi.txt", "r")
toplam=0
gun_sayisi=0
for satir in f:
    satir=satir.rstrip() .split(":") # split fonk ile listeye donusur
    print(satir)
    toplam+=int(satir[1])

print("yillik ortalama",  yillik_ortalama_hesap())
print("ocak ortalama",  aylik_ortalama_hesap(1))
print("haziran ortalama",  aylik_ortalama_hesap(6))
print("aralik ortalama",  aylik_ortalama_hesap(12))
except FileNotFoundError as err:
        print(err)
 def aylik_ortalama_hesap(ay):
f =open("fiyattakibi.txt", "r")
toplam=0
gun_sayisi=0
for satir in f:
    if "-" + str(ay) + "-"in satir:
    satir=satir.rstrip().split(":")
    toplam+= int()(satir[1])



    f.close()
    



