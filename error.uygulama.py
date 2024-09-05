liste = ["1","2","5a","10b","abc","10"]
###
# 1: liste elemanları içindeki sayısal değerleri bulunuz.
for x in liste:
    try:
        result = int(x) 
        print(result)
    except ValueError: 
        continue
# 2: kullanıcı 'q' değerini girmedikçe aldğınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
while True: 
    sayi = input('sayi: ')
    if sayi == 'q':
        break

    try:
        result = float(sayi)
        print('girdiginiz sayı: ', result)
        break
    except ValueError:
        print('geçersiz sayı')
    continue
# 3: girilen parola içinde türkçe karakter hatası veriniz.

def checkPassword(parola):
    turkce_karakterler = 'şçğüöİı'

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError('parola türkçe karakter içermez.')
        else:
            pass
print ('geçerli parola')

parola = input("parola: ")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)
# 4: faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.
def faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('negatif değer')
    
    result = 1 
    for i in range(1,x+1):
        result *=i
        
    return result
    
for x in [5,10,20,-3,'10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)