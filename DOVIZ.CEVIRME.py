import requests
import json

api_key = "94722743bfaaf6ef4129846e"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("bozulan döviz türü: ")
alinan_doviz = input("alınan doviz türü: ") 
miktar = int (input(f"ne kadar {bozulan_doviz}bozdurmak istiyorsunuz: "))

# Döviz dönüşüm oranlarını almak için API'ye istek yapıyoruz
sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["Conversion_rates"][alinan_doviz])
print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["Conversion_rates"][alinan_doviz]))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz, miktar * sonuc_json["Conversion_rates"],alinan_doviz))

