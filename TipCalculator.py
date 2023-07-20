def main():
    dollars = dollars_to_float(input("Quanto custou a refeição? "))
    percent = percent_to_float(input("Qual porcentagem você gostaria de dar uma gorjeta? "))
    tip = dollars * percent
    print(f"Deixe ${tip:.2f}")


def dollars_to_float(d):
    f = float(d.strip().replace("$", ""))
    return f


def percent_to_float(p):
    f = float(p.strip().replace("%", "")) / 100.0
    return f


main()
