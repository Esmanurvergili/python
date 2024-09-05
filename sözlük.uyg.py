'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad':'YILMAZ',
            'telefon':'532 000 00 01'

        }
        '125': {
             'ad':'Can'
             'soyad':'KORKMAZ',
             'telefon': '532 000 00 02'
        }
        '128': {
             'ad': 'Volkan'
             'soyad':'YÜKSELEN',
             'telefon': '532 000 00 03'
        },

    }

    1- Bilgileri verilen öğrencileri kullanicidan aldiginiz bilgilerle dictionary içinde saklayiniz. 
    2- Öğrenci numarasini kullanicidan alip ilgili öğrenci bilgisini gösterin.
'''

students = {}

number= input("student number: ")
name= input("student name: ")
surname= input("student surname: ")
phone= input("student number:" )

#students[number] = {
    #'ad': name,
    #'soyad': surname,
    #'telefon': phone,
#}
 
 # VEYAAA
 # TEK FARK AŞAĞISINDAKİNDE KAÇ TANE İSTENİYORSA KOPYALA YAPIŞTIR YAPILMALI UZUN YOL YUKARIDA BİRDEN FAZLA VERİ GİRİLEBİLİR.
students.update({
     number:{
      'ad': name,
      'soyad':surname,
      'telefon':phone,
     }

 })
number= input("student number: ")
name= input("student name: ")
surname= input("student surname: ")
phone= input("student number:" )
students.update({
     number:{
      'ad': name,
      'soyad':surname,
      'telefon':phone,
     }

 })
number= input("student number: ")
name= input("student name: ")
surname= input("student surname: ")
phone= input("student number:" )
students.update({
     number:{
      'ad': name,
      'soyad':surname,
      'telefon':phone,
     }

 })
print(students)

studentno = input('öğrenci no: ')
student = students[number]

print(student)