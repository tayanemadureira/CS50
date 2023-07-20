def main():
    print("Bem-vindo(a) à Lista de Compras!")
    print("Digite os itens da lista, um por vez, e suas respectivas quantidades.")
    print("Pressione Enter para adicionar o próximo item. Digite CTRL+D (EOF) para finalizar a lista.")

    grocery = {}

    while True:
        try:
            item = input().upper().strip()
            if item == "":
                break

            if item not in grocery:
                grocery[item] = 1
            else:
                grocery[item] += 1
        except EOFError:
            sorted_dict = dict(sorted(list(grocery.items())))
            print("Lista de Compras:")
            for item, quantity in sorted_dict.items():
                print(f"{quantity} {item}")
            break
        except KeyError:
            pass


if __name__ == "__main__":
    main()
