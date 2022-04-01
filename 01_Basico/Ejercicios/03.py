"""Crea un programa que pida tres números por teclado. El programa imprime en consola
la media aritmética de los números introducidos"""

numero1 = int(input("Ingresa el numero 1: "))
numero2 = int(input("Ingrasa el numero 2: "))
numero3 = int(input("Ingresa el numero 3: "))

def mediaAritmetica (numero1, numero2, numero3):
    sumatoria = numero1 + numero2 + numero3
    promedio = sumatoria / 3
    print("La media aritmerica de los números introducidos es: " +str(promedio))

mediaAritmetica(numero1, numero2, numero3)
