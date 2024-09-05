website = "http://www.esmanurvergili.com"
course = "python kursu: Baştan Sona Pyhton Programlama Rehberiniz (40 saat)"
# 1- "hello world" karakter dizisinin baş ve sondaki  boşluk karakterini silin.
result = ' Hello World '.strip() # baş ve son iki boşluğu siler.
result = ' Hello World '.lstrip() # sadece soldaki boşluğu siler.
result =' Hello World '.rstrip() #sadece sağdaki boşluğu siler.
# 2- "www.esmanurvergili.com" içindeki esmanurvergili bilgisi haricindeki her karakteri silin 
result =  website.strip('htp:/w.com')
# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.
result = (course.lower())
# 4- "website" içindeki kaç tane a karakteri silin.
result = website.count('a')
# 5- "website" www ile başlayıp .com ile bitiyor mu?
result = website.startswith('www')
result = website.endswith('.com')
# 6- "website" içinde .com ifadesi var mı ?
result = website.find('.com')
result = website.index('.com')
# 7- "course" içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result = course.isalpha() # hepsi alfabetik mi
result =course.isdigit() # hepsi rakam mı
# 8- "contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna ekleyiniz. 
result = 'contents'.center(50,'*') # sağa ve sola yıldız ekler
result = 'contents'.ljust(50,'*') #sağa yıldız ekler
result = 'contents'.rjust(50,'*') # sola yıldız ekler
# 9- "course" karakter dizisindeki tüm boşluk karakterini "-" ile değiştirin
result = course.replace(' ','-')
# 10- "hello World" karakter dizisindeki "World" ifadesini "there" olarak değiştirin. 
result = 'hello world'.replace("world","there")
# 11- "course" karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')

print(result)