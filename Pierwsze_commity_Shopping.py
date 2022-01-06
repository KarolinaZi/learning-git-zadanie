shopping = {
"piekarnia": ["chleb","bułki","pączek"],
"warzywniak": ["marchew","seler","rukola"]
}
Ilosc = 0

print("Lista zakupów")

for shop in shopping:
    shopping[shop] = [product.capitalize() for product in shopping[shop]]   
    
    print(f"Idę do {shop.capitalize()} i kupuję tam {shopping[shop]}")
    Ilosc += (len(shopping[shop]))

print(f"W sumie kupuję {Ilosc} produktów")