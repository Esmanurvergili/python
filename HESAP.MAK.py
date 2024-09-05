x = float(input("ilk sayiya giriniz."))
y = float(input("ikinci sayi giriniz."))
islem = input("""yapmak istediginiz islemi giriniz.
 (toplama: + cikarma: - carpma: * bolme: / tam bolme:// kalan: % üs alma: ** minimum deger: min maximum deger: max)             
""")
if islem == "+":
    print("sonuc: "+str(x+y))
elif islem =="-":
      print("sonuc: "+str(x-y))
elif islem =="*":
      print("sonuc: "+str(x*y))
elif islem =="/":
      print("sonuc: "+str(x/y))
elif islem =="//":
      print("sonuc: "+str(x//y))
elif islem =="%":
      print("sonuc: "+str(x%y))
elif islem =="**":
      print("sonuc: "+str(x**y))
elif islem =="min":
      print("sonuc: "+str(min(x,y)))
elif islem =="max":
      print("sonuc "+str(max(x,y)))
else:
      print("doğru işlem yapiniz")
      

                        