def main():
    print("Bem-vindo ao programa Deep Thought!")
    print("Por favor, forneça a Resposta para a Grande Questão da Vida, do Universo e de Tudo.")

    resposta = input("Qual é a Resposta? ").lower().strip()

    respostas_corretas = ["42", "quarenta e dois"]

    if resposta in respostas_corretas:
        print("Sim, essa é a Resposta!")
    else:
        print("Não, essa não é a Resposta.")

if __name__ == "__main__":
    main()