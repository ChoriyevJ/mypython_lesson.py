# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:23:19 2022

@author: User
"""
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print (car.title())
    else:
        print(car.upper())


login = input("Ismingizni kiriting : ")
if login.lower() == "admin":
    print (f"Xush kelibsiz, {login.title()}.Foydalanuvchilar ro'yxatini ko'rasizmi ? ")
else:
    print(f"Xush kelibsiz, {login.title()} !")

sonlar = list(range(2))
numbers = []
print("2 ta son kiriting:")
for n in sonlar:
    numbers.append(input(f"{n+1} - sonni kiriting : "))
if numbers[1] == numbers[0]:
    print ("Sonlar bir-biriga teng ekan.")
else:
    print("Axmoq bir xil son kiritsang o'lasanma!")


son = int(input("Ixtiyoriy son kiriting : "))
if son > 0:
    print("Musbat son.")
elif son == 0:
    print ("NOOLL")
else:
    print("Manfiy son.")


son = int(input('Ixtiyoriy son kiriting : '))
if son >= 0:
    print(f"Sonning ildizi {son**0.5} ga teng")
else:
    print ("Musbat son kiriting.")
    
    
if son == 0:
    print("NOLL juft ham toq ham emas.")
elif son%2 == 0:
    print ("juft son.")

elif son%2 == 1:
    print ("Toq son")
    


narx = 15000
choy = True
non = True
salat = False
kompot = True
assorti = False

if choy:
    print ("Mijoz choy oldi")
    narx = narx + 1000
if non:
    print ("Mijoz non oldi")
    narx = narx +3000
if salat:
    print ("Mijoz salat oldi")
    narx = narx + 5000
if kompot:
    print ("Mijoz kompot oldi")    
    narx = narx + 3000
if assorti:
    print ("Mijoz assorti oldi")
    narx = narx + 10000
print (f"Jami {narx} so'm")


print(True or True)
print(True or False)
print(False or False)
print(False or True  )

menyu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa' ]
print('manti' in  menyu)
print('osh' in menyu)
ovqat = input("Qanaqa ovqat hohlaysiz ? ")
if ovqat.lower() not in menyu:
    
    print("Bizda bunaqa taom yoq.")
else:
   
    print("Buyurtma qabul qilindi")


menyu = ['osh', 'kabob', 'qazonkabob', 'norin', 'somsa' ]
buyurtmalar = ['somsa', 'manti', 'kabob', 'salat']
for taom in buyurtmalar:
    if taom in menyu:
        print(f"{taom.title()} menyuda bor")
    else:
        print(f"Kechirasiz, {taom} menyuda yoq ")

jurnal = ['Jasmina', 'Daler', 'Bekzod', 'Jahon', 'Guli']
spiska = ['Jasmina', 'Toxir', 'Dima', 'Guli', 'Alisher']
for mehmon in jurnal:
    if mehmon in spiska:
        print(f"{mehmon.title()}, siz taklif qilingansiz.")
    else :
        print(f"Uzr {mehmon}, sizdi endi taklif qilmoqchi edik. ")

list1 = []
if list1:
    print("Ro'yxatda elementlar bor")
else:
    print("Ro'yxat bo'sh")



menyu = ['osh', 'kabob', 'qazonkabob', 'norin', 'somsa' ]
buyurtmalar = ['somsa', 'manti', 'kabob', 'salat']
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menyu:
            print(f"{taom.title()} menyuda bor")
        else:
            print(f"Kechirasiz, {taom} menyuda yoq ")
else:
    print("Savatchangiz bo'sh.")
       

menyu = ["somsa", "osh", "shashlik", "go'sht", "sho'rva","salat"]
buyurtmalar = []
sonlar = list(range(3))
for n in sonlar:
    buyurtmalar.append(input(f"{n+1}- siga nima xohlaysiz : "))
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menyu:
            print (f"{taom.title()} menyuda bor.")
        else:
            print (f"Kechirasiz, {taom} menyuda yoq.")
else:
    print("Siz hali taom tanlamadiz!")














