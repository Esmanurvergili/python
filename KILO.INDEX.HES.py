isim = input('adınız: ')
yaş =input('yaşınız: ')
kg =float(input('kilonuz: '))
hg =float(input('boyunuz:'))

index = (kg) / (hg**2)  # Kilo indeksini hesapla
# Kilo indeksine göre değerlendirme yap
zayif= (index>=0) and (index<=18.4)
normal = (index>18.5) and (index<=24.9)
kilolu = (index>24.9) and (index<=29.9)
obez = (index>=29.9) and (index<=34.9)
print(f'{isim} kilo indeksin:{index} ve kilo değerlendirmen zayif: {zayif}')
print(f'{isim} kilo indeksin:{index} ve kilo değerlendirmen normal: {normal}')
print(f'{isim} kilo indeksin:{index} ve kilo değerlendirmen kilolu: {kilolu}')
print(f'{isim} kilo indeksin:{index} ve kilo değerlendirmen obez: {obez}')