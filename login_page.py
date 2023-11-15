kullanici_adim="Csax"

parolam ="csax.exe"

giris_hakki=3

while giris_hakki>0:
    giris_hakki -=1

    kullanici_adi = input("Kullanıcı Adınızı Girin :")

    parola = input("Parolayı Giriniz :")

    if kullanici_adi==kullanici_adim and parola== parolam:

        print("Sisteme başarılı bir şekilde giriş yaptınız.")
        break
    else:

        print("Kullanıcı bilgileri yanlış tekrar deneyin!")
        print("Deneme Hakkiniz : ", giris_hakki)  