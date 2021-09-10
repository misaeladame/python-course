mitupla = ("Juan", 13, 1, 1995, 13)
print(mitupla[2])
print(mitupla[1])

milista = list(mitupla)
print(milista)
print(mitupla)

milista2 = ["Misael", 3, 2, 2000]
mitupla2 = tuple(milista2)
print(milista2)
print(mitupla2)

print("Juan" in mitupla)
print("Andrea" in mitupla)


print(mitupla.count(13))
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