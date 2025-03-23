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
        total += int(product['price'])
    print(f"\nCelková cena všech položek: {total}$")

def most_expensive_product():
    max_price = 0
    for product in products:
        if float(product["price"]) > max_price:
            max_price = float(product["price"])

    print("\nNejdražší položka/y")
    for product in products:
        if float(product["price"]) == max_price:
            print(f" - {product['name']}, cena: {product['price']}$")

def cheapest_product():
    min_price = float("inf")
    for product in products:
        if float(product["price"]) < min_price:
            min_price = float(product["price"])

    print("\nNejlevnější položka/y")
    for product in products:
        if float(product["price"]) == min_price:
            print(f" - {product['name']}, cena: {product['price']}$")

def average_price():
    total = 0
    for product in products:
        total += int(product["price"])

    average = total / len(products)
    print(f"Průměrná cena:{average}$")

def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Vyhledání položk/y")
    print("3. Celková cena všech položek")
    print("4. Nejdražší položka")
    print("5. Nejlevnější položka")
    print("6. Průměrná cena")
    print("7. Přidat položku")


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

    elif choice == 4:
        most_expensive_product()
        print("")
        menu()
    elif choice == 5:
        cheapest_product()
        print("")
        menu()
    elif choice == 6:
        average_price()
        print("")
        menu()
    elif choice == 7:
        add_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
