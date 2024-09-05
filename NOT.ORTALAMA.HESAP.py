yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sozlu: '))

ortalama = (yazili1 + yazili2 + sozlu)/3
if (ortalama >= 0) and (ortalama < 25):
    print (f'ortalamanız: {ortalama} notunuz:0')
elif (ortalama >= 25) and (ortalama <= 45):
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