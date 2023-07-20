def main():
    print("Bem-vindo(a) à Lista de Compras!")
    print("Digite a data no formato mês/dia/ano ou mês, dia e ano separados por vírgula.")
    print("O programa converterá a data para o formato yyyy-mm-dd.")
    print("Pressione Enter para adicionar o próximo item. Digite CTRL+D (EOF) para finalizar a lista.")

    months = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro"
    ]

    while True:
        date = input("Digite a data: ")
        try:
            if "/" in date:
                mm, dd, yyyy = date.split("/")
            elif "," in date:
                mmdd, yyyy = date.split(", ")
                mm, dd = mmdd.split(" ")
                # Não é necessário verificar se mm está em months. KeyError é tratado separadamente.
                mm = (months.index(mm)) + 1
            if int(mm) > 12 or int(dd) > 31:
                raise ValueError
        except (AttributeError, ValueError, NameError, KeyError):
            print("Data inválida ou formato incorreto. Certifique-se de digitar a data corretamente.")
        else:
            print(f"{int(yyyy)}-{int(mm):02}-{int(dd):02}")
            break


if __name__ == "__main__":
    main()
