products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)

def search_product():
    search_term = input("Zadej hledaný výraz:")
    matches = []

    for product in products:
        if search_term in product['name'].lower():
            matches.append(product)
    if len(matches) == 0:
        print("\nNebyl nalzen žádná odpovídající položka.\n")
        return

    print("\nNalezené položky:")
    for product in matches:
        print(f" - {product['name']}, cena: {product['price']}$")
    print()

def total_price():
    total = 0
    for product in products:
        total += product['price']
    print(f"\nCelková cena všech položek: {total}$")

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Vyhledání položk/y")
    print("3. Celková cena všech položek")
    print("2. Přidání položky")


    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        search_product()
        print("")
        menu()

    elif choice == 3:
        total_price()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
