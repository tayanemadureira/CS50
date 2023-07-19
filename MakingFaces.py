def replace_emoticons(text):
    emoticons = {
        ":)": "🙂",
        ":(": "🙁",
        ":D": "😄",
        ":P": "😛",
        ";)": "😉",
        ":'(": "😢",
        "XD": "😆",
        "<3": "❤️",
    }

    for emoticon, emoji in emoticons.items():
        text = text.replace(emoticon, emoji)

    return text

def main():
    print("Bem-vindo ao programa Making Faces!")
    print("Este programa substitui emoticons por emojis no texto digitado.")

    text = input("Digite o texto: ")
    text_with_emojis = replace_emoticons(text)

    print("\nTexto com emojis substituindo os emoticons:")
    print(text_with_emojis)

if __name__ == "__main__":
    main()
