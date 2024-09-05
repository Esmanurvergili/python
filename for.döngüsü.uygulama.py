sayilar = [1, 3, 5, 7, 9, 12, 19, 21]

# 1- sayilar listesindekihangi sayılar 3 ün katıdır?
for sayi in sayilar:
    if (sayi%3==0):
        print(sayi)
# 2- sayilar listesindeki sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
   toplam = toplam + sayi #veyaaa buraya toplam += sayi yazılır
   print('toplam:', toplam)
# 3- sayilar listesindeki tek sayıların karesinin alınız. 
for sayi in sayilar:
    if(sayi %2 == 1)
       print(sayi ** 2)

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

# 4- sehirlerden hangileri en fazla 5 karakterlidir?
for sehir in sehirler :
   if (len(sehir) <=5):
      print(sehir)
 
urunler = [
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}
]

# 5- ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
 fiyat = int(urun['price'])
 toplam += fiyat
 print('toplam ürün fiyatı:', toplam)  
# 6- ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?
for urun in urunler:
    if (int(urun['price']) <= 5000):
       print(urun['name'])