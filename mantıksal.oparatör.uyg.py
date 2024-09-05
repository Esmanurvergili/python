# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('sayi: '))

result = (sayi>0) and (sayi<=100)
print(f'sayi 0-100 arasindami: {result}')
# 2- girilen bir sayını pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = float(input('sayi: '))
result = (sayi > 0) and (sayi %2 == 0)
print(str(f'girilen sayi pozitif çift sayimi: {result}'))
# 3- email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'esmanurvergili@gmail.com'
parola = '1453esma'

girilenemail = input('email: ')
girilenparola= input('parola: ')

result = (girilenemail == email) and (girilenparola == parola)
print(f'uygulamaya giriş başarılı mı: {result}')
# 4- girilen 3 sayıyı büyüklük olarak karşılaştırınız. 
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

result = (a>b) and (a>c)
print(f'a en büyük sayıdır : {result}')

result = (b>a) and (b>c)
print(f'b en büyük sayıdır : {result}')

result = (c>a) and (c>b)
print(f'c en büyük sayıdır : {result}') # kaç tane deger varsa o kadar  result printleri yazıyoruz.
# 5- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1 = float(input('1.vize: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

ortalama = ((vize1 + vize2)/2) *0.6 + (final * 0.4)
print(f'öğrencini ortalamasi: {ortalama}ve geçme durumu {result}')
#    a-) ortalama 50 olsa bile final notu en az 50 olamalıdır.
vize1 = float(input('1.vize: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

result = (ortalama>=50) and (final>=50)
print(f'öğrencini ortalamasi: {ortalama}ve geçme durumu {result}')
#    b-) finalden 70 alındığında ortalamanın önemi olmasın.
vize1 = float(input('1.vize: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

result = (ortalama>=50) and (final>=70)
print(f'öğrencini ortalamasi: {ortalama}ve geçme durumu {result}')
# 6- kişinin ad, kilo, boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    formül: (kilo/boy uzunluğunun karesi)
#    aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4 => zayıf
#    18.5-24.9 => normal
#    25.0-29.9 => fazla kilolu
#    30.0-34.9 => şişman (obez)

isim = input('adınız: ')
kg =float(input('kilonuz'))
hg =float('boyunuz')

index = (kg) / (hg**2)
zayif= (index>=0) and (index<=18.4)
normal = (index>=18.5) and (index<=24.9)
kilolu = (index>=25.0) and (index<=29.9)
obez = (index>=30.0) and (index<=34.9)
print(f'{name} kilo indeksin:{index} ve kilo değerlendirmen zayif: {zayif}')
print(f'{name} kilo indeksin:{index} ve kilo değerlendirmen normal: {normal}')
print(f'{name} kilo indeksin:{index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{name} kilo indeksin:{index} ve kilo değerlendirmen obez: {obez}')