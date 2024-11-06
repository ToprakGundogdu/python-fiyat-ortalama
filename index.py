import os

def domates_fiyatlari():

    ocak = float(input("Ocak Domates Fiyatı : "))
    subat = float(input("Şubat Domates Fiyatı : "))
    mart = float(input("Mart Domates Fiyatı : "))
    nisan = float(input("Nisan Domates Fiyatı : "))
    mayis = float(input("Mayıs Domates Fiyatı : "))
    haziran = float(input("Haziran Domates Fiyatı : "))
    temmuz = float(input("Temmuz Domates Fiyatı : "))
    agustos = float(input("Ağustos Domates Fiyatı : "))
    eylul = float(input("Eylül Domates Fiyatı : "))
    ekim = float(input("Ekim Domates Fiyatı : "))
    kasım = float(input("Kasım Domates Fiyatı : "))
    aralik = float(input("Aralık Domates Fiyatı : "))

    fiyatortalama = (ocak + subat + mart + nisan + mayis + haziran + temmuz + agustos + eylul + ekim + kasım + aralik) / 12

    print("\nYıllık Toplam Domates Alış Fiyatı : ", fiyatortalama)
    print("\nEkranda yazanları silmek istiyorsanız 1, baştan başlamak istiyorsanız 2 yazın.")

def ekran_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    ekran_temizle()
    domates_fiyatlari()  

    secim = input("\nSeçiminizi yapın: ")

    if secim == '1':
        ekran_temizle()
    elif secim == '2':
        ekran_temizle() 
        print("Program yeniden başlıyor...") 
    else:
        print("Geçersiz seçim. Programı sonlandırıyorum.")
        break  
