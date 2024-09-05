'''
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifade ederek bulmasını sağlayacağız (5 hak vereceğiz)
*random modülü için pyhton random şeklinde arama yapmalıyız
**her soru 20 puan  toplam 100 puan
***hak bilgisini kullanıcıdan alıcaz 
'''
import random
sayi = random.randint(1,100)
can = int(input(' kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0   # Tahmin sayısını saymak için sayaç


while hak > 0:   # Tahmin hakkı bitene kadar döngü devam eder
    hak -= 1    # Her tahminde bir hak azalt
    sayac += 1  
    tahmin = int(input('tahmin : '))


    if sayi == tahmin:
        print(f'tebrikler {sayac}. defada bildiniz. toplam puanınız: {100 - (100/can) * (sayac-1) }')
        break
    elif sayi > tahmin :
        print('yukarı')
    else:
        print ('aşağıda')

        if hak == 0:
            print(f'hakkınız bitti. tutulan sayı: {sayi}')
