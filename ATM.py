kartsifresi = "1453"
bakiye = 3000
denemehakki = 3
print("x bankasına hosgeldiniz")
kart_islem = True

islemdurumu = True
while islemdurumu :
    girilensifre = input("lütfen kart şifrenize giriniz: ")
    if girilensifre != kartsifresi:   # Şifre yanlışsa, deneme hakkını azalt ve kullanıcıya bilgi ver
        print("yanlış şifre. tekrar deneyiniz.")
        denemehakki -= 1
        print(denemehakki, "deneme hakkınız kaldı")
        if denemehakki == 0:  # Deneme hakkı sıfırsa kartı bloke et ve işlemi sonlandır
            print("kartınız bloklandı. banka ile görüşün.")
            islemdurumu = False
    else: 
        print("giriş ypaıldı.")
        print("""
        yapılacak işlem seçiniz
                   
            1- para çekme
            2- para yatırma
            3- bakiye sorgulama
            4-çıkış      
                    
             """)
        while kart_islem :
            islemno = input("işlem numarasını giriniz: ")
            if islemno == "4":
                 print("çıkış yapıldı.")
                 islemdurumu = False
                 kart_islem = False
            elif islemno == "3" :
                 print("toplam bakiye:", bakiye,"₺")  # tl işareti için alt gr + t
            elif islemno == "2" :
                 yatirilacakmiktar = int(input("yatırılacak miktar: "))
                 bakiye += yatirilacakmiktar
                 print("işlem gerçekleşti.")
            elif islemno == "1" :
                 cekilecekmiktar = int(input("çekilecek miktar: "))
                 if cekilecekmiktar > bakiye: 
                     print("yetersiz bakiye.")
                 else:
                     bakiye -=cekilecekmiktar
                     print("işlem gerçekleşti.")

