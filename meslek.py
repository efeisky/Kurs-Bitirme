#Program fonksiyonu
def sorular(ad):
    print("---------")
    soru1=int(input("Soru 1-) Kan sever misiniz?(evet=1 - hayır= 0)\nCevabınız:"))
    print("-----------")
    soru2=int(input("Soru 2-) Yazılımla alakanız nedir?(var=1 - yok= 0)\nCevabınız:"))
    print("-----------")
    soru3=int(input("Soru 3-) Çocukları sever misiniz?(evet=1 - hayır= 0)\nCevabınız:"))
    print("-----------")
    soru4=int(input("Soru 4-) Biyoloji ilgi alanınız mıdır?(evet=1 - hayır= 0)\nCevabınız:"))
    print("-----------")
    soru5=int(input("Soru 5-) Elektrik işlerinden anlar mısınız?(evet=1 - hayır= 0)\nCevabınız:"))
    print("-----------")

    if soru1==1 and soru4==1:
        print("Size uygun mesleğin TIP Alanı olduğunu düşünüyoruz.")
        print(f"Dr. {ad} \U0001F600")
    elif soru2==1 and soru5==1:
        print("Size uygun mesleğin YAZILIMCILIK olduğunu düşünüyoruz.")
        print(f"Yazılımcı {ad} \U0001F600")
    elif soru3==1:
        print("Size uygun mesleğin ÖĞRETMENLİK olduğunu düşünüyoruz.")
        print(f"Öğretmen {ad} \U0001F600")
    else:
        print("Verdiğiniz cevaplar hiç bir meslek ile uyuşmadı. Sizin için en doğrusu bir gün yemeği dışarıda yiyin ve iyice tüm meslekleri düşünün. Emin olun algoritmadan daha iyi sonuçlar bulursunuz.")

#Program
print("Meslek bulma programına hoş geldin. Bu programda sana en uygun mesleği bulmak için çalışacağız.\nToplamda 5 tane soru sorulacaktır.")
ad = input("Lütfen adınızı giriniz: ")
print("---------------------")
print(sorular(ad))
