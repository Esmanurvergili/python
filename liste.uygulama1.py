names = ["Ali","Yağmur","Hakan","Deniz"]
years = ["1998","2000","2001","2003",'2003']
sayı = [1,2,3,4,1]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
input(names)
# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
input(names)
# 3- "Deniz" ismini listeden siliniz.
names.remove("Deniz")
input(names)
# 4- "Deniz" isminin indeksi nedir?
#names.remove('Deniz')
print(names)
# 5- "Ali" listenin bir elemanı mıdır?
result = 'ali' in names
result = names.indeks('ali')
# 6- liste elemanlarını ters çevirin.
names.reverse()
print (names)
# 7- liste elemanlarını alfabetik olarak sıralayınız  .
names.sort()
print(names)
# 8- years listesini rakamsal büyüklüğüne göre sıralayınız.
years.sort()
print(years)
# 9- str = "Chevrolet, Dacia" karakter dizisini listelemeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(",")
print(result)
# 10- years dizisinin en büyük ve en küçük elemanı nedir?
min = min(years)
max = max(years)
print(min, max)
# 11- years dizisinde kaç tane 1998 değeri vardır?
result = years.count("1998")
#print(result)
intlideger=sayı.count(1)
print(intlideger)
# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print= years
# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)
marka=input("marka: ")
markalar.append(marka)

print(markalar)