def main():
    foods = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    print("Bem-vindo(a) à Taqueria do Felipe!")
    print("Aqui está o nosso menu com os preços:")

    for item, price in foods.items():
        print(f"{item}: R$ {price:.2f}")

    total_price = 0

    while True:
        try:
            item = input("Digite o item que deseja pedir (ou pressione Enter para sair): ").title().strip()
            if not item:
                break

            if item in foods:
                total_price += foods[item]
                print(f"Total: R$ {total_price:.2f}")
            else:
                print("Desculpe, esse item não está no nosso menu.")
        except EOFError:
            print()

    print("Obrigado(a) por pedir na Taqueria do Felipe!")

if __name__ == "__main__":
    main()
