def not_hesapla(satir):
    satir = satir.strip()  # Satırdaki boşlukları temizle
    liste = satir.split(':')  # Öğrenci adını ve notları ayır

    ogrenciadi = liste[0]  # Öğrenci adını al
    notlar = liste[1].split(',')  # Notları virgüllerle ayır

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1 + not2 + not3) / 3  # Ortalama hesapla

    # Ortalama aralıklarına göre harf notunu belirle
    if ortalama >= 90:
        harf = "AA"
    elif ortalama >= 85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama >= 75:
        harf = "CB"
    elif ortalama >= 70:
        harf = "CC"
    elif ortalama >= 65:
        harf = "DC"
    elif ortalama >= 60:
        harf = "DD"
    elif ortalama >= 50:
        harf = "FD"
    else:
        harf = "FF"

    # Sonucu döndür
    return f"{ogrenciadi}: {harf}\n"

def ortalamalari_oku():
    with open("sinav_notlari.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(satir.strip())  # Satırları ekrana yazdır

def not_gir():
    ad = input('Öğrenci adı: ')
    soyad = input('Öğrenci soyadı: ')
    not1 = input('Not1: ')
    not2 = input('Not2: ')
    not3 = input('Not3: ')

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3 + '\n')  # Notları dosyaya ekle

def notlari_kayit_et():
    with open('sinav_notlari.txt', "r", encoding="utf-8") as file:
        liste = []
        for satir in file:
            liste.append(not_hesapla(satir))  # Her satırı işleyip harf notunu hesapla

    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
        for i in liste:
            file2.write(i)  # Sonuçları yeni dosyaya yaz

# Ana döngü
while True:
    islem = input('1- Notları oku\n2- Not gir\n3- Notları kayıt et\n4- Çıkış\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        notlari_kayit_et()
    elif islem == '4':
        break
    else:
        print('Geçersiz seçenek, tekrar deneyin.')
