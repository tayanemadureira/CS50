def main():
    print("Bem-vindo ao Just Setting Up My Twttr!")
    print("Este programa remove todas as vogais do texto digitado.")

    texto = input("Digite o texto: ")
    vogais = ["a", "e", "i", "o", "u"]

    print("Texto sem vogais: ", end="")
    for letra in texto:
        if letra.casefold() not in vogais:
            print(letra, end="")

    print()

if __name__ == "__main__":
    main()

