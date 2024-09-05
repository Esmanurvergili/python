# 1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def yazdir (kelime, adet):
    print(kelime * adet)

yazdir('merhaba' , 10)
    
# 2- kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazın.
def listeyecevir(*params):
    liste = []

    for param in params:
        liste.append(param)
    return liste
result = listeyecevir(10,20,30,'merhaba')
print (result)
# 3- gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

def asalsayilaribul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
             for i in range (2, sayi):                
                 if (sayi % i == 0):
                    break
             else: 
                print(sayi)
                    
sayi1= int(input('sayi 1: '))
sayi2= int(input('sayi 2: '))
asalsayilaribul(sayi1, sayi2)


# 4- kendisine gönderilen bir sayının tam bölenlerini bir liste şekline döndürün.
 
def tambolenleribul(sayi):
    tambolenler = []

    for i in range(2, sayi):
         if (sayi % i == 0):
             tambolenler.append(i)

    return tambolenler
print(tambolenleribul(20)