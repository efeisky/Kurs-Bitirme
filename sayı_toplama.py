#Kütüphane
import random
import time as t

#Program

print("Sayı toplatmaca oyununa hoş geldin.")
print("Sizin için özel hazırladığım sayı oluşuyor.0-100 arasında")
sayı= random.randint(0,100)
print(sayı)
t.sleep(1.5)
print("Oyun kuralları gereğince siz toplamda 3 sayı gireceksiniz. Eğer girdiğiniz sayıların toplamı özel sayıya eşit olursa kazanırsınız.")

tekrar=0
while True:
    secim_1= int(input("1. Sayınızı seçiniz: "))
    secim_2= int(input("2. Sayınızı seçiniz: "))
    secim_3= int(input("3. Sayınızı seçiniz: "))
    print("---------------------")
    toplam= secim_1+secim_2+secim_3
    tekrar+=1
    if toplam==sayı:
        print(f"Tebrik ederiz. Tahmin edeceğiniz sayı {sayı} idi ve doğru bildiniz.\nTekrar sayınız:{tekrar}")
        devam=input("Devam etmek ister misiniz? (1-Evet q-Hayır): ")
        if devam=="1":
            sayı= random.randint(0,100)
        elif devam=="q":
            print("Program sonlandırılıyor.")
            t.sleep(1.5)
            break
    elif toplam!=sayı:
        print("Ne yazık ki doğru bilemediniz. Eğer devam ederseniz aynı sayı ile devam edeceksiniz.")
        devam=input("Devam etmek ister misiniz? (1-Evet q-Hayır): ")
        if devam=="1":
            print("Sayıları tekrardan tahmin ediniz.")
            print("******************")
        elif devam=="q":
            print("Program sonlandırılıyor.")
            t.sleep(1.5)
            break