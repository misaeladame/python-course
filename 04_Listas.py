miLista = ["María", "pepe", "Marta", "Antonio"]

# Imprime todos los elementos de la lista
print(miLista[:])

print(miLista[2])

print(miLista[-2])
print(miLista[-3])

print(miLista[0:3])
print(miLista[:3])
print(miLista[:2])

print(miLista[1:2])
print(miLista[1:3])

print(miLista[2:])

# Inserta un elemento
#           indice , contenido
miLista.insert(2, "Misael")
print(miLista[:])

# Ingresa un elemento al final de la lista
miLista.append("Sandra")
print(miLista[:])

# Inserta elementos "n" al final de la lista
miLista.extend(["Lugo", "Ivan", "Lucía"])
print(miLista[:])

# Imprime el indice del elemento 
print(miLista.index("Antonio"))
print(miLista.index("Lucía"))

miLista.append("Marta")
print(miLista[:])
print(miLista.index("Marta"))

# Comprueba si existe un elemento en la lista
print("pepe" in miLista)
print("Leonel" in miLista)




# Lista con elementos de diferente tipoi
miLista2 = ["Maria", 5, True, 78.35]
print(miLista2[:])
print(miLista2[2])

miLista2.extend(["Sandra", "Ana", "Lucia"])
# Elimina el elemento con ese nombre
miLista2.remove("Ana")
print(miLista2[:])

miLista2.remove(5)
print(miLista2[:])

# Elimina el ultimo elemnto de la lista
miLista2.pop()
print(miLista2[:])





miLista3 = ["Mario", 3, False, 69.696969]
miLista4 = ["Juan", "Luis"]

# Concatena las listas
miLista5 = miLista3 + miLista4
print(miLista5[:])

# Multiplica las lista
miLista3 = ["Mario", 3, False, 69.696969] * 3
print(miLista3[:])
