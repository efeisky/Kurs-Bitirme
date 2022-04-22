#Kütüphaneler
import secrets
import random
import time as t

#Şifreler
sifreler = {}

#Şifre Dereceleri
sifre_uzunluk=16
kolay_sifre=['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
zor_sifre=['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '*', '.', '_', '-']

#Program
print("Şifre programına hoş geldin.")
while True:
    print("Lütfen aşağıdan yapmak istediğiniz işlemi seçin.\n1-Şifre ekle\n2-Şifrelerimi Göster\nProgramdan çıkmak için 'q'")
    islem= input("Seçilen İşlem Numarası: ")
    print("-------------------------------------")
    if islem=="1":
        print("Şifre ekleme bölümünü seçtiniz.")
        while True:
            amac=input("Şifrenizi kullanma amacınızı giriniz: ")
            print("-------------------------------------")
            sifre_derece=int(input("Şifrenizin zorluk derecesini seçiniz: \n1-Sadece Büyük-Küçük harf\n2-Özel karakterler, sayılar ve Büyük-Küçük harf\nSeçilen İşlem Numarası:"))
            print("-------------------------------------")
            if sifre_derece==1:
                print("Kolay Şifre modunu seçtiniz. Şifreniz oluşturuluyor lütfen bekleyiniz.")
                t.sleep(1.5)
                sifrem= "".join(random.choices(kolay_sifre,k=16))
                sifreler[amac] = sifrem
                print("Sizin için oluşturduğumuz şifre: ", sifrem)
                print("********")
                sorgu=int(input("Şifre eklemeye devam etmek istiyorsanız 1'e tıklayınız.Diğer işlemler için rastgele tuş.."))
                if sorgu==1:
                    print("*******")
                else:
                    break
            if sifre_derece==2:
                print("Zor Şifre modunu seçtiniz. Şifreniz oluşturuluyor lütfen bekleyiniz.")
                t.sleep(1.5)
                sifrem= secrets.token_urlsafe(sifre_uzunluk)
                print("Sizin için oluşturduğumuz şifre: ", sifrem)
                print("********")
                sorgu=int(input("Şifre eklemeye devam etmek istiyorsanız 1'e tıklayınız.Diğer işlemler için rastgele tuş.."))
                if sorgu==1:
                    print("*******")
                else:
                    break

    elif islem=="2":
        print("Şifreleriniz aşağıdaki gibidir.")
        print("*****************************************************")
        print(sifreler)
        print("*****************************************************")
    elif islem=="q":
        print("Programdan çıkıyorsunuz.Tekrar bekleriz:)")
        break

