def main():
    print("Bem-vindo(a) ao Medidor de Combustível!")
    print("Digite a fração de combustível no formato x/y para obter a informação correspondente.")
    x = get_fraction("Fração: ")
    print("Nível de Combustível:", x)


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            if int(y) == 0:
                print("Denominador não pode ser zero. Tente novamente.")
                continue

            fuel_level = int(x) / int(y)

            if 0 <= fuel_level <= 0.1:
                return "E (Reserva)"
            elif 0.9 <= fuel_level <= 1:
                return "F (Tanque Cheio)"
            elif 0.1 < fuel_level < 0.9:
                return f"{int(fuel_level * 100)}%"
            else:
                print("Fração inválida. Tente novamente.")
        except (ValueError, ZeroDivisionError):
            print("Entrada inválida. Certifique-se de digitar a fração no formato correto (x/y).")


if __name__ == "__main__":
    main()
