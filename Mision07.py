# Autor: Mariana Coria Rodriguez, A01374765
# Ciclos while



def dividir(dividendo, divisor):
    contador = 0
    residuo = 0
    residuo += dividendo
    while residuo >= divisor:
        valor = (residuo-divisor)
        residuo = valor
        contador = contador+1
    print(dividendo, "/", divisor, "=", contador, "sobra", residuo)

def encontrarMayor():
    print ("Teclea un número para encontrar el mayor")
    potasio2 = int(input("Teclea un número [-1 para salir]: "))
    potasioGuardado = 0
    if potasio2 == -1:
        print("No hay valor mayor")
    else:
        while potasio2 != -1:
            if potasio2 > potasioGuardado:
                potasioGuardado = potasio2
                potasio2 = int(input("Teclea un número [-1 para salir]: "))
            else:
                potasio2 = int(input("Teclea un número [-1 para salir]: "))
        print("El mayor es: ", potasioGuardado)


def main():
    print("Misión 07. Ciclos While")
    print("Autor: Mariana Coria Rodríguez")
    print("Matrícula: A01374765")
    print("1. Calcular divisines")
    print("2. Encontrar el mayor")
    print("3. Salir")
    potasio = int(input("Teclea tu opción: "))

    while potasio != 3:
        if potasio < 1 or potasio > 3:
            print("ERROR")
            print("Misión 07. Ciclos While")
            print("Autor: Mariana Coria Rodríguez")
            print("Matrícula: A01374765")
            print("1. Calcular divisines")
            print("2. Encontrar el mayor")
            print("3. Salir")
            potasio = int(input("Teclea tu opción: "))
        elif potasio == 1:
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo, divisor)
            print("Misión 07. Ciclos While")
            print("Autor: Mariana Coria Rodríguez")
            print("Matrícula: A01374765")
            print("1. Calcular divisines")
            print("2. Encontrar el mayor")
            print("3. Salir")
            potasio = int(input("Teclea tu opción: "))

        elif potasio == 2:
            encontrarMayor()
            print("Misión 07. Ciclos While")
            print("Autor: Mariana Coria Rodríguez")
            print("Matrícula: A01374765")
            print("1. Calcular divisines")
            print("2. Encontrar el mayor")
            print("3. Salir")
            potasio = int(input("Teclea tu opción: "))

    print("Bye")

main()
