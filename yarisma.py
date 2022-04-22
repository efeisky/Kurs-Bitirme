#Kütüphaneler

import time as t
import random
from datetime import datetime
#Sorular

sorular=["1 gün kaç saattir?",
"Türkiyenin en büyük dağı hangi dağdır?"
,"Dün perşembe ise yarın nedir?"
,"Everest dağı hangi ülkededir?",
"Bursaya özgü dönerli, ekmekli yemek hangisidir?",
"Süt helvası hangi şehire aittir?",
"Dünyada en çok nüfusa ait ülke hangisidir?",
"En küçük rakam hangisidir?",
"Şıklar içerisindeki en büyük negatif sayı hangisidir?",
"90/5*4 İşleminin cevabı nedir?",
"Bir insan mutfağa gidiyorum diyorsa muhtemelen ne yapacaktır?",
"Pisagora göre 3-4-x yerine ne gelmelidir?",
"Gabardin nedir?",
"Ana taşıyıcı kuleleri arasındaki mesafe en uzun olan, \"en uzun asma köprü\" hangisidir?",
"Hangi adda bir sos yoktur?",
"Bugüne kadar nerede ölen hiçbir insan olmamıştır?",
"TDK Atasözleri ve Deyimler Sözlüğü'nde hangi kelimenin geçtiği bir atasözü veya deyim yoktur?",
"Kral Arthur hangisinde hüküm sürer?",
"Balkaş Gölü'nden yola çıkıp Altay Dağları üzerinden Baykal Gölü'ne ulaşıyorsanız hangi kıtadasınızdır?",
"Cevabı \"sam yeli\" olan bir bulmaca sorusunda sorulan hangisi olur?"
]

secenekler = [["A) 12","B) 24","C) 36","D) 18"],
["A) Ağrı Dağı","B) Süphan Dağı","C) Erciyes Dağı","D) Küçükağrı Dağı"],
["A) Pazar","B) Çarşamba","C) Cumartesi","D) Cuma"],
["A) Amerika Birleşik Devletleri","B) Kanada","C) İngiltere","D) Çin-Nepal"],
["A) İskender","B) Bursa Kebabı","C) Tombik Döner","D) Muradiye Çorbası"],
["A) Adana","B) Kasımpaşa","C) Kütahya","D) Bursa"],
["A) Japonya", "B) ABD", "C) Çin","D) Hindistan"],
["A) 1","B) -1","C) 0","D) 11"],
["A) -999999","B) -10","C) -1","D) -9"],
["A) 70","B) 72","C) 62","D) 80"],
["A) Yemek Yapar","B) Uyur","C) Televizyon izler","D) Çamaşır yıkar"],
["A) 3","B) 10","C) 5","D) 7"],
["A) Bir enstrüman çeşidi","B) Bir Köpek Cinsi","C) Bir Kumaş Türü","D) Bir saç Modeli"],
["A) Japonya'daki Akaşi Kaikyo Köprüsü","B) Türkiye'deki 1915 Çanakkale Köprüsü","C) Çin'deki Yangtze Köprüsü","D) ABD'deki Golden Gate Köprüsü"],
["A) Pesto","B) Avogrado","C) Ranch","D) Paprika"],
["A) Antarktika kıtasında","B) Mariana Çukuru'nun dibinde","C) Everest Dağı'nda","D) Dünya atmosferinin dışında"],
["A) Armut","B) Kayısı","C) Kiraz","D) Erik"],
["A) Birleşik Krallık","B) Norveç","C) Camelot","D) Monako"],
["A) Afrika","B) Güney Amerika","C) Asya","D) Avrupa"],
["A) Çölden esen sıcak rüzgar","B) Denizden esen soğuk rüzgar","C) Nehirden esen sıcak rüzgar","D) Dağdan esen soğuk rüzgar"]]

cevaplar = ["B","A","C","D","A","D","C","C","C","B","A","C","C","B","B","B","B","C","C","A"]

a=random.choices(sorular,k=5)
print(len(sorular))
print(len(secenekler))
print("-------------")

#Listeler

dogru_bildiklerim=[]

yanlis_bildiklerim=[]
#Program
def program():

    print("Profesyonel Bilgi Yarışmasına hoş geldin.")
    ad = input("Lütfen adınızı yazınız: ")
    i=0
    puan=0
    bas_sure = datetime.now()
    while i<=4:

        print("--------------------")
        
        soru_bas = datetime.now()

        print(f"{ad}, Soru {i+1}-)",a[i])
        print(secenekler[sorular.index(a[i])])
        cevap=input("Lütfen cevabınızın seçeneğini yazınız örn(a/A): ")
        soru_son = datetime.now()
        print("*****")
        soru_fark = (soru_son - soru_bas).seconds

        if soru_fark>=5:
            print("Soruyu cevaplandırmanıza bakılmaksızın süreniz sona erdiği için puan alamadınız. \U000123F1")
            yanlis_bildiklerim.append(a[i])
            
        elif cevap.upper()==cevaplar[sorular.index(a[i])]:
            print(f"Tebrikler {ad}. Doğru cevap \U0001F600")
            dogru_bildiklerim.append(a[i])
            puan+=20
        else:
            print(f"Üzgünüz..{ad} Yanlış cevap!.. Lütfen daha dikkatli olun.\U0001F60A")
            yanlis_bildiklerim.append(a[i])
        i+=1
    son_sure = datetime.now()
    fark = (son_sure - bas_sure).seconds
    print("*---------------------------*")
    print(f"Yarışma süresince {fark} sn. kadar süre harcadınız.")
    print(f"Doğru bildiğin soru/sorular: ",dogru_bildiklerim)
    print(f"Yanlış bildiğin soru/sorular: ",yanlis_bildiklerim)
    print(f"Yarışmamızda 100 de {puan} puan yaptınız.Tebrikler.")

program()