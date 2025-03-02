#1. SORU: Asal Sayı Kontrolü
#Bir sayının asal sayı olup olmadığını kontrol eden bir Python fonksiyonu yazın.

#✅ Kurallar:
#Asal sayı, sadece kendisine ve 1’e bölünebilen 1’den büyük pozitif sayılardır.
#Fonksiyon, kullanıcıdan bir sayı almalı ve asal olup olmadığını kontrol etmelidir.
#🎯 Örnek Kullanım:
#asal_mi(7)  # Çıktı: 7 bir asal sayıdır.
#asal_mi(10) # Çıktı: 10 bir asal sayı değildir.

def asal_mi(sayi):
    if sayi<2: # 2 den küçük sayılar zaten asal değildir
        return f"{sayi} bir asal sayı değildir."
    
    for i in range(2,sayi):
        print( i) 
        if sayi% i == 0: # sayıdan küçük olan tüm sayılarla bölünüp bölünmediğini kontrol ettim
            return f"{sayi} bir asal sayı değildir."
        
    return f"{sayi} bir asal sayıdır."

            
sayi = int(input("Bir sayı giriniz:"))
print(asal_mi(sayi))           
    
        
        

