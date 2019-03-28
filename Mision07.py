# Autor: Mariana Coria Rodriguez, A01374765
# Dividir sin dividir, restar 



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
    opcion2 = int(input("Teclea un número [-1 para salir]: "))
    opcionGuardado = 0
    if opcion2 == -1:
        print("No hay valor mayor")
    else:
        while opcion2 != -1:
            if opcion2 > opcionGuardado:
                opcionGuardado = opcion2
                opcion2 = int(input("Teclea un número [-1 para salir]: "))
            else:
                opcion2 = int(input("Teclea un número [-1 para salir]: "))
        print("El mayor es: ", opcionGuardado)


def main():
    print("Misión 07. Ciclos While")
    print("Autor: Mariana Coria Rodríguez")
    print("Matrícula: A01374765")
    print("1. Calcular divisines")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))

    while opcion != 3:
        if opcion < 1 or opcion > 3:
            print("ERROR")
            print("Misión 07. Ciclos While")
            print("Autor: Mariana Coria Rodríguez")
            print("Matrícula: A01374765")
            print("1. Calcular divisines")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))
        elif opcion == 1:
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo, divisor)
            print("Misión 07. Ciclos While")
            print("Autor: Mariana Coria Rodríguez")
            print("Matrícula: A01374765")
            print("1. Calcular divisines")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))

        elif opcion == 2:
            encontrarMayor()
            print("Misión 07. Ciclos While")
            print("Autor: Mariana Coria Rodríguez")
            print("Matrícula: A01374765")
            print("1. Calcular divisines")
            print("2. Encontrar el mayor")
            print("3. Salir")
            opcion = int(input("Teclea tu opción: "))

    print("Bye")

main()
