"""Crea un programa que pida por teclado "Nombre", "Direccion" y "Tfno". Esos tres datos
deberán ser almacenados en una lista y mostrar en consola el mensaje: "Los datos
personales son: nombre apellido telefono" (Se mostrarán los datos introducidos por
teclado"""

nombre = input("Introduce tu nombre: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu telefono: ")

lista = [nombre, direccion, telefono]

print("Los datos personales son: " + str(lista[:]))