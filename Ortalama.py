while True:
    try:
        sinav_1 = float(input("Sınav 1 Not giriniz: "))
        if(sinav_1 >=0) and (sinav_1 <=100) and (sinav_1!= 0):
            break
        else:
            print("Lütfen 1 ve 100 arasında bir sayı giriniz.")
    except ValueError:
        print("Lütfen İNTEGER değer giriniz.")

while True:
    try:
        sinav_2 = float(input("Sınav 2 Not giriniz: "))
        if(sinav_2 >=0) and (sinav_2 <=100) and (sinav_2!= 0):
            break
        else:
            print("Lütfen 1 ve 100 arasında bir sayı giriniz.")
    except ValueError:
        print("Lütfen İNTEGER değer giriniz.")
        
while True:
    try:
        sinav_3 = float(input("Sınav 3 Not giriniz: "))
        if(sinav_3 >=0) and (sinav_3 <=100) and (sinav_3!= 0):
            break
        else:
            print("Lütfen 1 ve 100 arasında bir sayı giriniz.")
    except ValueError:
        print("Lütfen İNTEGER değer giriniz.")

ortalama = (sinav_1 + sinav_2+ sinav_3)/3

if(ortalama >=0) and (ortalama <25):
    print(f"Ortalama: {ortalama} Notunuz: 0")
elif(ortalama >=25) and (ortalama <45):
    print(f"Ortalama: {ortalama} Notunuz: 1")
elif(ortalama >=45) and (ortalama <55):
    print(f"Ortalama: {ortalama} Notunuz: 2")
elif(ortalama >=55) and (ortalama <70):
    print(f"Ortalama: {ortalama} Notunuz: 3")
elif(ortalama >=70) and (ortalama <85):
    print(f"Ortalama: {ortalama} Notunuz: 4")
elif(ortalama >=85) and (ortalama <100):
    print(f"Ortalama: {ortalama} Notunuz: 5")
else:
    print("Hatalı Not Girildi")