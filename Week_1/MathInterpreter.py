def main():
    print("Bem-vindo ao Math Interpreter!")
    print("Este programa realiza operações matemáticas básicas.")

    expressao = input("Digite a expressão matemática (Exemplo: 10 + 5): ").strip()
    x, operador, z = expressao.split()

    num1 = float(x)
    num2 = float(z)

    if operador == "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado:.1f}")
    elif operador == "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado:.1f}")
    elif operador == "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado:.1f}")
    elif operador == "/":
        resultado = num1 / num2
        print(f"Resultado: {resultado:.1f}")
    else:
        print("Operador inválido. Por favor, utilize apenas +, -, *, ou /.")

if __name__ == "__main__":
    main()
