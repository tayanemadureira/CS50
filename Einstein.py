def calculate_energy(mass):
    speed_of_light = 300000000  # Velocidade da luz em m/s
    energy = mass * speed_of_light ** 2
    return energy

def main():
    print("Bem-vindo ao programa de cálculo de energia de Einstein!")
    
    mass = float(input("Digite a massa (em kg): "))
    
    energy = calculate_energy(mass)
    
    print(f"A energia resultante é: {energy:.2f} joules.")

if __name__ == "__main__":
    main()