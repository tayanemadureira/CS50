def main():
    print("Bem-vindo(a) à Informação Nutricional!")
    print("Digite o nome de uma fruta para ver a quantidade de calorias associadas.")

    frutas = {
        "Maçã": 130,
        "Abacate": 50,
        "Banana": 110,
        "Melão": 50,
        "Goiaba": 60,
        "Uvas": 90,
        "Melão": 50,
        "Kiwi": 90,
        "Limão": 15,
        "Limão": 20,
        "Nectarina": 60,
        "Laranja": 80,
        "Pêssego": 60,
        "Pera": 100,
        "Abacaxi": 50,
        "Ameixas": 70,
        "Morangos": 50,
        "Cerejas": 100,
        "Tangerina": 50,
        "Melancia": 80,
    }

    fruta = input("Digite o nome da fruta: ").title().strip()

    if fruta in frutas:
        print(f"Calorias: {frutas[fruta]}")
    else:
        print("Fruta não encontrada na lista de informações nutricionais.")

if __name__ == "__main__":
    main()
