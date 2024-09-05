age = int(input("yasinizi girin. "))
reading_status= input("okuyor musunuz? (evet:e, hayir:h)")

if age >= 18 and  reading_status =="h":
   print("askere gelme yasiniz geldi. ")

elif age >= 18 and reading_status == "e":
   print("okulunuz bittiğinde askere geleceksiniz. ")

else :
   print("askerlik yasiniz daha gelmedi. ")