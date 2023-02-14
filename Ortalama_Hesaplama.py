veri = []

for i in range(3):
    while True:
        try:
            sinav = float(input("Sinav {0} giriniz: ".format(i+1)))
            if sinav >= 0 and sinav <=100:
                veri.append(sinav)
                break
            else:
                print("0 İle 100 Arasinda Sayi Girebilirsiniz.")
        except ValueError:
            print("Lütfen İNTEGER değer giriniz.")
            
def sonuc(sinav1,sinav2,sinav3):
    ortalama = (sinav1+sinav2+sinav3)/3
    if ortalama >0 and ortalama <=25:
        print(f"Ortalama: {ortalama} Notunuz: 0")
    elif ortalama >25 and ortalama <45:
        print(f"Ortalama: {ortalama} Notunuz: 1")
    elif ortalama >45 and ortalama <55:
        print(f"Ortalama: {ortalama} Notunuz: 2")    
    elif ortalama >55 and ortalama <70:
        print(f"Ortalama: {ortalama} Notunuz: 3")    
    elif ortalama >70 and ortalama <85:
        print(f"Ortalama: {ortalama} Notunuz: 4")    
    elif ortalama >85 and ortalama <100:
        print(f"Ortalama: {ortalama} Notunuz: 5")
    else:
        print("Hatali Not Girdiniz. Tekrar Deneyiniz.")
        
for j in range(1):
    sonuc(veri[0],veri[1],veri[2])       
