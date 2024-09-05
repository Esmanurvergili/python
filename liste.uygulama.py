# 1- BMW, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
Arabalar = ['BMW', 'Mercedes', 'Opel', 'Mazda']
# 2- liste kaç elemanlıdır? 
result = (len(Arabalar))
# 3- listenin ilk ve son elemanı nedir? 
result = Arabalar[0]
result = Arabalar[3] # veya
result = Arabalar[-1] #diyebiliriz
# 4- mazda değerini Toyota ile değiştirin.
Arabalar[-1]= 'Toyota'
result =Arabalar
# 5- Mercedes listesinin bir elemanı mıdır?
result = 'Mercedes' in Arabalar
# 6- listenin -2 indeksindeki değer nedir ?
result = Arabalar[-2]
# 7- listenin ilk 3 elemanı alın.
result = Arabalar[0:3]
# 8- listenin son 2 elemanı yerine "Toyata" ve "Renault" değerini ekleyin.
Arabalar[-2:]='Toyota','Renault' # veya
Arabalar[-2:] = ['Toyota', 'Renault'] # olabilir tek fark parantez içine alır ayrı bir liste oluşturur.
result = Arabalar
# 9- listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = (Arabalar + ["Audi", "Nissan"])
# 10- listenin son elemanı silin.
del Arabalar[-1]
result = Arabalar
# 11- liste elemanlarını tersten yazdırınız.
result = Arabalar[::-1]
# 12- aşağıdaki verileri bir liste içine saklayınız.
#studenta= Yiğit Bilgi 2001, (70,60,70)
#studentb= Esmanur Vergili 2003 (85,75,95)
#studentc=  Berfin Bilkay 2000 (80,90,75)

studenta= ["Yiğit", "Bilgi", "2001" (70,60,70)]
studentb= ["Esmanur", "Vergili", "2003", (85,75,95)]
studentc= ["Berfin", "Bilkay", "2000", (80,90,75)]
student = studenta + studentb + studentc
print (student)
student =[studenta, studentb, studentc]
# 13- liste elemanlarını ekrana yazdırınız.
result = studenta[0]
result = studentb[1]
result = studentc[2],[-1]

print(result)           