shopping2 = {
"nabial": ["ser","mleko"],
"kiosk": ["gazeta","bilety"]
"drogeria": ["mydlo","pasta do zebow"]
}
Ilosc = 0

linia = "Lista zakupów3\n"

for shop in shopping2:
    shopping2[shop] = [product.capitalize() for product in shopping2[shop]]   
    
    linia += f"Idę do {shop.capitalize()} i kupuję tam {shopping2[shop]}\n"
    Ilosc += (len(shopping2[shop]))

linia += (f"W sumie kupuję {Ilosc} produktów")

print(linia)
print("Drogeria added")
print("Add 3rd branch")
print ("Add new branch in Learning Git project-second try")
print ("hello")

