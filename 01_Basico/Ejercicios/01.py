"""Crea un programa que pida dos números por teclado. El programa tendrá una función
llamada "DevuelveMax" encargada de devolver el número más alto de los dos 
introducidos"""

numero1 = int(input("Introduce el número 1: "))
numero2 = int(input("Introduce el número 2: "))

def DevuelveMax(numero1, numero2):
    if numero1 > numero2:
        return numero1
    elif numero1 == numero2:
        return "Son iguales ambos numeros (" +str(numero1) +")"
    else:
        return numero2


print("El número más alto es: " +str(DevuelveMax(numero1, numero2)))
