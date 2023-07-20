def main():
    print("Bem-vindo ao programa File Extensions!")
    print("Por favor, forneça o nome de um arquivo para identificar o tipo de conteúdo associado.")

    arquivo = input("Nome do arquivo: ").lower().strip().split(".")

    extensoes_texto = ["txt"]
    extensoes_aplicacao = ["zip", "pdf"]
    extensoes_imagem = ["png", "gif", "jpg", "jpeg"]

    if arquivo[-1] in extensoes_texto:
        print("text/plain")
    elif arquivo[-1] in extensoes_aplicacao:
        print(f"application/{arquivo[-1]}")
    elif arquivo[-1] in extensoes_imagem:
        print(f"image/{arquivo[-1]}")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()