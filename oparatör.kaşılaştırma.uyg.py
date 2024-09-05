# 1- girilen 2 sayıdan hangisi büyüktür?
a = float(input("a: "))
b = float(input("b: "))

result = (a > b)
print(f'a: {b} b: {a} den büyüktür: {result}')
# 2- kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1 = float(input('1. vize: '))
vize2 = float(input('2. vize: '))
final = float(input('final: '))

ortalama = ((vize1 + vize2)/2 * 0.6) + ((final * 0.4))

print(f' not ortalamaniz : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')
# 3- girilen sayını tek mi çift mi olduğunu yazdırın.
sayi = int(input('sayi: '))
tekcift = (sayi %2 ==0)
print(f'girilen sayi çift olma durumu: {tekcift}')
# 4- girilen bir sayının negatif pozitif durumu yazdırın.
sayi = int(input('sayi: '))
pozitifmi = (sayi > 0)

print(f'girilen sayını pozitif olma durumu: {pozitifmi}')
# 5- parola ve email bilgisin isteyip doğruluğunu kontrol ediniz.
#   (email: esmanurvergili@.com parola: 1453)
email = 'esmanurvergili@gmail.com'
password = '1453'

girilenemail = input('email: ')
girilenpassword = input('parola: ')

mail= (email == girilenemail)
ipassword = (password == girilenpassword)

print(f'email bilgisi doğrumu: {mail} ve parola doğru mu: {ipassword}')
