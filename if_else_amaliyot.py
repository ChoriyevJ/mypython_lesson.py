# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 19:38:21 2022

@author: User
"""

son = int(input("Juft son kiriting : "))
if son % 2 == 0:
    print("Raxmat.")
else:
    print("Bu son juft emas.")




yosh = int(input("Yoshingizni kiriting : "))
if yosh <= 4 or yosh > 60:
    narx = 'bepul'
elif yosh < 18:
    narx = f"{10000} so'm"
elif yosh >= 18:
    narx = f"{20000} so'm"
print (f"Sizga mzeyga kirish {narx}.")

print("2 ta son kiriting : ")
sonlar = list(range(2))
numbers = []
for n in sonlar:
    numbers.append(input(f"{n+1} - sonni kiriting : "))
if numbers[0] == numbers[1]:
    print ("sonlar bir-biriga  teng.")
elif numbers[0] < numbers[1]:
    print("birinchi son ikkinchisidan  kichik.")
else :
    print("birinchi son ikkinchisidan katta.")
    




products = ['Fanta', 'Cola', 'Vafli', 'Pechenie', 'Miller', 'shokolad', 'grill', 'non', 'ham-ham', 'maslo']
savat =[]
print("5 ta mahsusol kiriting : ")
num = list(range(5))
for n in num:
    savat.append(input(f"{n+1} - mahsulotni kiriting : "))
for product in savat:
    if product.title() in products:
        print(f"{product.title()} do'konimizda bor.")
    else :
        print(f"Kechirasiz {product} do'konimizda yoq")






products = ['Fanta', 'Cola', 'Vafli', 'Pechenie', 'Miller', 'Shokolad', 'Grill', 'Non', 'Ham-ham', 'Maslo']
savat =[]
yes_products = []
no_products = []
print("5 ta mahsusol kiriting. ")
num = list(range(5))
for n in num:
    savat.append(input(f"{n+1} - mahsulotni kiriting: "))
for product in savat:
    if product.title() in products:
        yes_products.append(product)
    else:
        no_products.append(product)     
if no_products:
    print("Quidagi mahsulotlar do'konimizda yo'q :")
    for product in no_products:
        print(product.title())
else:
    print("Siz so'ragan barcha mahsulot do'konimizda bor.")






users = ['jamshid', 'zoxid', 'xusniddin', 'asatbek', 'anvar']
login = input("Yangi login kiriting :  ")
if login.lower() in users:
    print("Login band, yangi login tanlang.")
else:
    print(f"Xush kelibsiz, {login.title()}.")







sonlar = list(range(2,11))
son = int(input("Butun son kiriting : "))
for n in sonlar:
    if son%n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")


















