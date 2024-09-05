import requests
import json

api_key = "94722743bfaaf6ef4129846e"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulan döviz türü (örneğin, USD): ").upper()
alinan_doviz = input("Alınan döviz türü (örneğin, EUR): ").upper()
miktar = float(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

# Döviz dönüşüm oranlarını almak için API'ye istek yapıyoruz
response = requests.get(api_url + bozulan_doviz)
response_json = response.json()

# Dönüşüm oranları sözlüğünden istenilen döviz oranını alıyoruz
doviz_orani = response_json["conversion_rates"].get(alinan_doviz)

if doviz_orani:
    print(f"1 {bozulan_doviz} = {doviz_orani} {alinan_doviz}")
    sonuc = miktar * doviz_orani
    print(f"{miktar} {bozulan_doviz} = {sonuc:.2f} {alinan_doviz}")
else:
    print(f"{alinan_doviz} için dönüşüm oranı bulunamadı.")