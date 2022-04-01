mitupla = ("Juan", 13, 1, 1995, 13)
print(mitupla[2])
print(mitupla[1])

# Convierte una tupla a una lista
milista = list(mitupla)
print(milista)
print(mitupla)

# Convierte una lista a una tupla
milista2 = ["Misael", 3, 2, 2000]
mitupla2 = tuple(milista2)
print(milista2)
print(mitupla2)

# Comprueba si existe ese elemento en la tupla
print("Juan" in mitupla)
print("Andrea" in mitupla)

# Cuenta cuantas veces se repite un elemento en la tupla
print(mitupla.count(13))
# Cuenta la longitud de la tupla
print(len(mitupla))

mituplaunitaria = ("Juan",)
print(len(mituplaunitaria))


mituplasinparentesis = "Juan", 13, 1, 1995 #Empaquetado de tupla
print(mituplasinparentesis)

tupla = ("Juan", 13, 1, 1995)
nombre, dia, mes, agno = tupla # Desempaquetado de tuplas
print(nombre)
print(dia)
print(agno)
print(mes)