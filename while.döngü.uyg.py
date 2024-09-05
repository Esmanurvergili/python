sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- sayilar listesini while ile ekrana yazdırın.
x = 1
while x <=21:
    print(x)
    x = x+2
# 2- başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları yazdırın.
baslangic = int(input('baslangic: '))
bitis = int(input('bitis: '))

i= baslangic
while i < bitis:
    i += 1
    if (i % 2 == 1):
       print (i)
# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100
while i > 0 :
    print(i)
    i -= 1
# 4- kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın. 
numaralar = []

i = 0
while i<5:
    sayi = int(input('sayı: '))
    numaralar.append(sayi)
    i += 1
    numaralar.sort
    
    print(numaralar)
# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde 
# # # ürün sayısın kullanıcıya sorun.
# # # dictionary listesi yapısı (name, price) şeklinde olsun.
# # # ürün ekleme işlemi bittiğinde  ürünleri ekranda while ile listeleyin. 

urunler = []
adet =int(input('kaç ürün eklemek istiyorsunuz '))
i = 0
while (i<adet):
    isim = input('ürün ismi: ')
    fiyat = input('ürün fiyatı: ')
    urunler.append({
        'isim': isim,
        'fiyat': fiyat 
        })
    i += 1
    for urun in urunler:
        print (f'ürün adı: {urun["isim"]} ürün fiyatı: {urun["fiyat"]}')