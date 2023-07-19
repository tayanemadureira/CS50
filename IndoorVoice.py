def main():
    print("Bem-vindo ao programa Indoor Voice!")
    print("Este programa irá exibir o texto digitado em letras minúsculas e maiúsculas.")

    text = input("Digite o texto: ").strip()  # Remove espaços em branco antes e depois do texto
    
    lowercase_text = text.lower()
    uppercase_text = text.upper()

    print(f"\nTexto em letras minúsculas: {lowercase_text}")
    print(f"Texto em letras maiúsculas: {uppercase_text}")

if __name__ == "__main__":
    main()
