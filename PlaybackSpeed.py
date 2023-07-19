import time

def playback_speed(text, speed):
    words = text.split()
    delay = 1 / speed  # Calcula o atraso com base na velocidade

    for word in words:
        print(word, end=' ', flush=True)  # Imprime a palavra com um espaço
        time.sleep(delay)  # Atraso para simular a velocidade de reprodução

def main():
    print("Bem-vindo ao programa Playback Speed!")
    print("Este programa simula a velocidade de reprodução do texto.")

    text = input("Digite o texto: ")
    speed = float(input("Digite a velocidade de reprodução (por exemplo, 1.0 para 1x, 2.0 para 2x): "))

    print("\nReproduzindo o texto com a velocidade escolhida:")
    playback_speed(text, speed)

if __name__ == "__main__":
    main()
