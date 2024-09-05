esmahesap = {
    'ad' : 'esmanur vergili',
    'hesapno' : '1234567',
    'bakiye' : 3000,
    'ekhesap' :  2000
    }

berfinhesap = {
    'ad' : 'berfin bilkay',
    'hesapno' : '1234576',
    'bakiye' : 2000,
    'ekhesap' : 1000
    }

def paracek(hesap, miktar) :
    print(f"merhaba {hesap['ad']}")

    if (hesap['bakiye']>= miktar):
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
        bakiyesorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekhesap']

        if (toplam >= miktar):
            ekhesapkullanimi = input('ek hesap kullanılsın mı (e/h)')
            
            if ekhesapkullanimi == 'e':
                ekhesapkullanilacakmiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekhesap'] -= ekhesapkullanilacakmiktar
                print('paranızı alabilirsiniz.')
                bakiyesorgula(hesap)
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else: 
            print('üzgünüz bakiye yetersiz')
            bakiyesorgula(hesap)

def bakiyesorgula(hesap):
    print(f"{hesap['hesapno']}nolu hesabınızda {hesap['bakiye']} tl bulunmaktadır ek hesap limitiniz ise {hesap['ekhesap']}tl bulunmaktadır")

paracek(esmahesap, 3000)
paracek(esmahesap, 1000)

