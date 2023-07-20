def main():
    print("Bem-vindo(a) aos Pratos de Cortesia!")
    print("Este programa verifica se uma placa de carro personalizada é válida.")

    placa = input("Digite a placa: ")

    if is_valid(placa):
        print("Placa Válida")
    else:
        print("Placa Inválida")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        # Verifica se todos os caracteres são letras
        if s.isalpha():
            return True
        else:
            # Verifica se há número no meio da placa (apenas se os dois primeiros caracteres são letras e o último é número)
            if s[:2].isalpha() and s[-1].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        # Retorna falso se o número começar com 0 ou se o caractere seguinte for letra
                        if s[i] == "0" or (i < len(s) - 1 and s[i + 1].isalpha()):
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()