# Uzunluk birimlerini santimetreye dönüştüren fonksiyonlar
def kilometre_to_cm(km):
    return km * 100000

def hektometre_to_cm(hm):
    return hm * 10000

def dekametre_to_cm(dam):
    return dam * 1000

def metre_to_cm(m):
    return m * 100

def desimetre_to_cm(dm):
    return dm * 10

def milimetre_to_cm(mm):
    return mm / 10

def cm_to_kilometre(cm):
    return cm / 100000

def cm_to_hektometre(cm):
    return cm / 10000

def cm_to_dekametre(cm):
    return cm / 1000

def cm_to_metre(cm):
    return cm / 100

def cm_to_desimetre(cm):
    return cm / 10

def cm_to_milimetre(cm):
    return cm * 10


# Kullanıcıdan veri alma
def main():
    print("Birimi seçin: km,hm,dam,m,dm,cm,mm")
    unit = input("Birimi girin: ").strip().lower()

    value = float(input("Değeri girin: "))

     # Kullanıcının girdiği birime göre dönüşümleri yap
    if unit == "km":
        print(f"{value} kilometre = {kilometre_to_cm(value)} cm")
        print(f"{value} kilometre = {cm_to_hektometre(kilometre_to_cm(value))} hektometre")
        print(f"{value} kilometre = {cm_to_dekametre(kilometre_to_cm(value))} dekametre")
        print(f"{value} kilometre = {cm_to_metre(kilometre_to_cm(value))} metre")
        print(f"{value} kilometre = {cm_to_desimetre(kilometre_to_cm(value))} desimetre")
        print(f"{value} kilometre = {cm_to_milimetre(kilometre_to_cm(value))} milimetre")
    
    elif unit == "hm":
        print(f"{value} hektometre = {hektometre_to_cm(value)} cm")
        print(f"{value} hektometre = {cm_to_kilometre(hektometre_to_cm(value))} kilometre")
        print(f"{value} hektometre = {cm_to_dekametre(hektometre_to_cm(value))} dekametre")
        print(f"{value} hektometre = {cm_to_metre(hektometre_to_cm(value))} metre")
        print(f"{value} hektometre = {cm_to_desimetre(hektometre_to_cm(value))} desimetre")
        print(f"{value} hektometre = {cm_to_milimetre(hektometre_to_cm(value))} milimetre")
    
    elif unit == "dam":
        print(f"{value} dekametre = {dekametre_to_cm(value)} cm")
        print(f"{value} dekametre = {cm_to_kilometre(dekametre_to_cm(value))} kilometre")
        print(f"{value} dekametre = {cm_to_hektometre(dekametre_to_cm(value))} hektometre")
        print(f"{value} dekametre = {cm_to_metre(dekametre_to_cm(value))} metre")
        print(f"{value} dekametre = {cm_to_desimetre(dekametre_to_cm(value))} desimetre")
        print(f"{value} dekametre = {cm_to_milimetre(dekametre_to_cm(value))} milimetre")

    elif unit == "m":
        print(f"{value} metre = {metre_to_cm(value)} cm")
        print(f"{value} metre = {cm_to_kilometre(metre_to_cm(value))} kilometre")
        print(f"{value} metre = {cm_to_hektometre(metre_to_cm(value))} hektometre")
        print(f"{value} metre = {cm_to_dekametre(metre_to_cm(value))} dekametre")
        print(f"{value} metre = {cm_to_desimetre(metre_to_cm(value))} desimetre")
        print(f"{value} metre = {cm_to_milimetre(metre_to_cm(value))} milimetre")
    
    elif unit == "dm":
        print(f"{value} desimetre = {desimetre_to_cm(value)} cm")
        print(f"{value} desimetre = {cm_to_kilometre(desimetre_to_cm(value))} kilometre")
        print(f"{value} desimetre = {cm_to_hektometre(desimetre_to_cm(value))} hektometre")
        print(f"{value} desimetre = {cm_to_dekametre(desimetre_to_cm(value))} dekametre")
        print(f"{value} desimetre = {cm_to_metre(desimetre_to_cm(value))} metre")
        print(f"{value} desimetre = {cm_to_milimetre(desimetre_to_cm(value))} milimetre")

    elif unit == "cm":
        print(f"{value} cm = {cm_to_kilometre(value)} kilometre")
        print(f"{value} cm = {cm_to_hektometre(value)} hektometre")
        print(f"{value} cm = {cm_to_dekametre(value)} dekametre")
        print(f"{value} cm = {cm_to_metre(value)} metre")
        print(f"{value} cm = {cm_to_desimetre(value)} desimetre")
        print(f"{value} cm = {cm_to_milimetre(value)} milimetre")

    
    elif unit == "mm":
        print(f"{value} milimetre = {milimetre_to_cm(value)} cm")
        print(f"{value} milimetre = {cm_to_kilometre(milimetre_to_cm(value))} kilometre")
        print(f"{value} milimetre = {cm_to_hektometre(milimetre_to_cm(value))} hektometre")
        print(f"{value} milimetre = {cm_to_dekametre(milimetre_to_cm(value))} dekametre")
        print(f"{value} milimetre = {cm_to_metre(milimetre_to_cm(value))} metre")
        print(f"{value} milimetre = {cm_to_desimetre(milimetre_to_cm(value))} desimetre")
    
        
    elif unit == "metre":
        print(f"{value} metre = {metre_to_cm(value)} cm")
    elif unit == "kilometre":
        print(f"{value} kilometre = {kilometre_to_cm(value)} cm")
    else:
        print("Geçersiz birim seçtiniz.")

if __name__ == "__main__":  # Ana fonksiyonu çalıştır
    main()
