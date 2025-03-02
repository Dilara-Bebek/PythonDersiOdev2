#2. Basit Hesap Makinesi
#Kullanıcıdan iki sayı ve bir işlem türü alarak sonucu döndüren bir fonksiyon yazın.

#✅ Kurallar:
#Kullanıcı +, -, *, / işlemlerinden birini seçmelidir.
#Bölme işleminde, ikinci sayı 0 olursa "Bölme işlemi için ikinci sayı 0 olamaz!" şeklinde uyarı verin.
#Kullanıcı geçersiz bir işlem girerse, "Geçersiz işlem türü!" mesajı gösterin.
#🎯 Örnek Kullanım:
#hesap_makinesi(5, 3, '+')  # Çıktı: 5 + 3 = 8
#hesap_makinesi(10, 2, '/')  # Çıktı: 10 / 2 = 5.0
#hesap_makinesi(4, 0, '/')   # Çıktı: Bölme işlemi için ikinci sayı 0 olamaz!
#hesap_makinesi(6, 2, '%')   # Çıktı: Geçersiz işlem türü!


def hesap_makinesi(sayi1,sayi2,islem):
    if(islem=='+'):
        return sayi1 + sayi2;
    elif(islem == '-'):
        return sayi1 - sayi2;
    elif(islem == '*'):
        return sayi1 * sayi2;
    elif(islem=='/'):
        if (sayi2 == 0):
            return "Bölme işlemi için ikinci sayı 0 olamaz!"
        else:
            return sayi1 / sayi2;
    else:
        return "Geçersiz işlem türü!"
    
    
sayi1_ = int(input("Lütfen 1. sayıyı giriniz : ")) 
sayi2_ = int(input("Lütfen 2. sayıyı giriniz : ")) 

islem_ = input("Lütfen yapmak istediğiniz işlemi seçiniz : ")


print("SONUÇ : " ,hesap_makinesi(sayi1_, sayi2_, islem_))

        
        
            
    
    