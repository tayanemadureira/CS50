def main():
    print("Bem-vindo ao Home Federal Saving Bank!")
    print("Por favor, digite uma saudação para saber o valor correspondente.")

    saudacao = input("Saudação: ").lower().strip()

    if saudacao.startswith("hello"):
        print("Valor: $0")
    elif saudacao.startswith("h"):
        print("Valor: $20")
    else:
        print("Valor: $100")

if __name__ == "__main__":
    main()
