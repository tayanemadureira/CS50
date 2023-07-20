def main():
    print("Bem-vindo ao Meal Time!")
    print("Este programa identifica a refeição com base no horário informado.")

    horario = input("Que horas são? ").strip()

    if 7.0 <= convert(horario) <= 8.0:
        print("Hora do café da manhã.")
    elif 12.0 <= convert(horario) <= 13.0:
        print("Hora do almoço.")
    elif 18.0 <= convert(horario) <= 19.0:
        print("Hora do jantar.")
    else:
        print("Não é hora de refeição.")

def convert(horario):
    x, y = horario.split(":")
    hora = float(x)
    minutos = float(y) / 60
    return float(hora + minutos)

if __name__ == "__main__":
    main()