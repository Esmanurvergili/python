yas = float(input("okula baslayacak olan cocuğun yasini girin: "))
kayit = input("kayit yaptirmak istiyor musunuz? (evet:e , hayir:h)")

if yas >= 6.5 and kayit == "e":
       print("ilkokula kayit yapma zamani geldi. ")
elif yas == 6.5 and kayit == "h":
         print("seneye ilkokula kayit yaptirmazsaniz cocuk okula gec kalir.")
elif yas < 6.5 and kayit == "h":
        sonuc=7-yas
        print(str(sonuc)+" "+ "senesi var")
elif yas < 6.5 and kayit == "e":
        sonuc=7-yas
        print("ilkokula kayit için"+" "+str(sonuc)+" "+ "sene daha beklemelisiniz daha yasina göre cok erken")

      
