midiccionario = {"Alemania" : "Berlín", "Francia" : "Paris", "Reino Unido" : "Londres", "Mexico" : "CDMX"}
print(midiccionario["Francia"])
print(midiccionario["Mexico"])
print(midiccionario)

# Agregar un elemento al diccionario
midiccionario["Italia"] = "Lisboa"
print(midiccionario)

# Se va a sobreescribir
midiccionario["Italia"] = "Roma"
print(midiccionario)

# Eliminar un elemento del diccionario
del midiccionario["Reino Unido"]
print(midiccionario)


# Diccionario con diferentes tipos
midiccionario2 = {"Alemania" : "Berlin", 23 : "Jordan", "Mosqueteros" : 3}
print(midiccionario2)


# Usar tuplas en los diccionarios
mitupla = ("Mexico", "Francia", "Reino Unido", "Alemania")
midiccionario3 = {mitupla[0] : "CDMX", mitupla[1]: "Paris", mitupla[2]: "Londres", mitupla[3]: "Berlin"}
print(midiccionario3)
print(midiccionario3["Francia"])

# usar listas en los diccionarios
midiccionario3 = {23: "Jordan", "Nombre": "Michael", "Equipo" : "Chicago", "anillos" : [1991, 1992, 1993, 1996, 1997, 1998]}
print(midiccionario3)
print(midiccionario3["Equipo"])
print(midiccionario3["anillos"])

# usar diccionario dentro de otro diccionario (subdiccionario)
midiccionario3 = {23: "Jordan", "Nombre": "Michael", "Equipo" : "Chicago", "anillos" : { "temporadas" : [1991, 1992, 1993, 1996, 1997, 1998]}}
print(midiccionario3)

# Usar métodos en los diccionarios

# Da las claves que pertenece al diccionario
print(midiccionario3.keys())

# Imprime los valores de las claves
print(midiccionario3.values())

# Imprime la longitud del diccionario
print(len(midiccionario3))
