        # if- elif- else #
# 1- kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#    ehliyet alma koşulu en az 18 ve eğitim durumulise yada üniversite olamlıdır.
isim =input('isminiz: ')
yas =int(input('yaşınız: '))
egitim =input('eğitim: ')
if(yas>=18):
 if (egitim == 'lise' or egitim == 'üniversite'):
   print(f'{isim} ehliyet alabilirsiniz')
else:
    print(f'{isim} ehliyet alamazsınız eğitim durumunuz yetersiz.')

    print(f'{isim} ehliyet alamazsınız yaşınız tutmuyor.')
# 2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırın.
#      0 - 24 => 0
#     25 - 44 => 1
#     45 - 54 => 2
#     55 - 69 => 3
#     70 - 84 => 4
#     85 - 100 => 5
yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sozlu: '))

ortalama = (yazili1 + yazili2 + sozlu)/3
if (ortalama >= 0) and (ortalama < 25):
   print (f'ortalamanız: {ortalama} notunuz:0')
elif (ortalama >= 25) and (ortalama <= 44):     
      print (f'ortalamanız: {ortalama} notunuz:1')
elif (ortalama >= 45) and (ortalama <= 54):
     print (f'ortalamanız: {ortalama} notunuz:2')
elif (ortalama >= 55) and (ortalama <= 69):
     print (f'ortalamanız: {ortalama} notunuz:3')
elif (ortalama >= 70) and (ortalama <= 84):
     print (f'ortalamanız: {ortalama} notunuz:4')
elif (ortalama >= 85) and (ortalama <= 100):
      print (f'ortalamanız: {ortalama} notunuz:5')
else:
     print('yanlış bilgi girdiniz')
# 3- trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. bakım => 1. yıl
#    2. bakım => 2. yıl
#    3. bakım => 3. yıl 
#    ** süre hesabını alına gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    ***datetime modülünü kullanmanız gerekiyor
#    (simdi) - (2018/9/1)=> gün
import datetime
tarih =input('aracınız hangi tarihtr trafiğe çıktı (2019/8/9): ')
tarih =tarih.split('/')
#print(tarih[0])
#print(tarih[1])
#print(tarih[2])

trafigecikis = datetime.datetime (int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigecikis
gün =fark.gün

if gün <=365:
   print('1.sercis aralığı')
elif gün>365 and gün <365*2:
   print('2. servis aralığı')
elif gün>365*2 and gün <365*3:
    print('3. servis aralığı')
else:
   print('hatalı süre')