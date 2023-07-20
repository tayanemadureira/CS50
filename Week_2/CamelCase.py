def main():
    print("Bem-vindo ao Case Camel!")
    print("Este programa converte uma string no formato camelCase para o formato snake_case.")

    camel_case = input("Digite a string em camelCase: ")

    print("Resultado em snake_case: ", end="")
    for c in camel_case:
        if c.islower():
            print(c, end="")
        if c.isupper():
            print("_", c.lower(), end="", sep="")

    print()

if __name__ == "__main__":
    main()
