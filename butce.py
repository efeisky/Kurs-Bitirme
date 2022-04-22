#Aylar

aylık={
    "Ocak":        {"Gelir": 7430,
                     "Kira" : 2500,
                     "Mutfak Harcamaları": 954,
                     "Elektrik Faturası" : 320},

    "Şubat":       {"Gelir": 6582,
                     "Kira" : 2100,
                     "Mutfak Harcamaları": 500,
                     "Elektrik Faturası" : 276},

    "Mart":        {"Gelir": 6933,
                     "Kira" : 2190,
                     "Mutfak Harcamaları": 650,
                     "Elektrik Faturası" : 376},

    "Nisan":       {"Gelir": 6582,
                     "Kira" : 2100,
                     "Mutfak Harcamaları": 500,
                     "Elektrik Faturası" : 276},

    "Mayıs":       {"Gelir": 6963,
                     "Kira" : 2190,
                     "Mutfak Harcamaları": 747,
                     "Elektrik Faturası" : 543},

    "Haziran":     {"Gelir": 7000,
                     "Kira" : 2200,
                     "Mutfak Harcamaları": 1000,
                     "Elektrik Faturası" : 500},

    "Temmuz":      {"Gelir": 7430,
                     "Kira" : 2500,
                     "Mutfak Harcamaları": 954,
                     "Elektrik Faturası" : 320},

    "Ağustos":     {"Gelir": 6582,
                     "Kira" : 2100,
                     "Mutfak Harcamaları": 500,
                     "Elektrik Faturası" : 276},

    "Eylül":       {"Gelir": 6933,
                     "Kira" : 2190,
                     "Mutfak Harcamaları": 650,
                     "Elektrik Faturası" : 376},

    "Ekim":        {"Gelir": 6582,
                     "Kira" : 2100,
                     "Mutfak Harcamaları": 500,
                     "Elektrik Faturası" : 276},

    "Kasım":       {"Gelir": 6963,
                     "Kira" : 2190,
                     "Mutfak Harcamaları": 747,
                     "Elektrik Faturası" : 543},

    "Aralık":      {"Gelir": 7000,
                     "Kira" : 2200,
                     "Mutfak Harcamaları": 1000,
                     "Elektrik Faturası" : 500},

}

#Program
print("Aile bütçesi hesaplama programına hoş geldiniz.")
ay = input("Bütçe hesapları için gereken ayı seçiniz: örn.(Haziran) ")

print(aylık[ay])