# int e float
## x = float(input("What's x? "))

## y = float(input("What's y? ")) 
# int para n° inteiros, float para decimais. 
# round faz o resultado ser o n° inteiro mais proximo.
# z = round(x + y)
# z = round(x / y), 2  > mais proximo com 2 decimais.
# print (f"{z:,}") > imprime o valor com ,

## z = (x / y)

## print(f"{z:.2f}") 
#especifica quantos digitos deseja imprimir

def main():
    x = int(input("What's x? "))
    print("X squared is", square(x))
def square(n):
    #return n * n
    return pow(n,2)

main()