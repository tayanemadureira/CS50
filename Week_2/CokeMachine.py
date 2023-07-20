def main():
    print("Bem-vindo à Máquina de Coca!")
    print("O preço de uma coca é R$ 50.")
    print("Por favor, insira moedas de R$ 25, R$ 10 ou R$ 5.")

    preco = 50
    total_pago = 0
    moedas_validas = [25, 10, 5]

    while preco > 0:
        print(f"Valor Devido: R$ {preco:.2f}")
        inserir_moeda = int(input("Insira a Moeda: "))

        if inserir_moeda in moedas_validas:
            preco -= inserir_moeda
            total_pago += inserir_moeda

    if total_pago >= 50:
        troco = total_pago - 50
        print(f"Troco: R$ {troco:.2f}")

if __name__ == "__main__":
    main()
