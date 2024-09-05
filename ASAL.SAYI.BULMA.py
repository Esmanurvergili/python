# Performansı artırmak için yalnızca sayının kareköküne kadar kontrol yapacağız
# Eğer bir sayı 2'den sayının kareköküne kadar olan sayılarla bölünüyorsa, asal sayı değildir

sayi=int(input("sayi giriniz: "))
asalmi = True
if sayi == 1:
    print('1 asal sayı değildir')

for i in range(2, sayi):
     if (sayi% i == 0):  # Eğer sayıyı i ile böldüğümüzde kalan 0 ise
          asalmi = False  # asal değildir
          break 

if asalmi:
     print('sayı asaldır.')

else:
     print('sayı asal değildir')