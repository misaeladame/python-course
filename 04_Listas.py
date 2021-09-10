miLista = ["María", "pepe", "Marta", "Antonio"]

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

miLista.insert(2, "Misael")
print(miLista[:])


miLista.append("Sandra")
print(miLista[:])

miLista.extend(["Lugo", "Ivan", "Lucía"])
print(miLista[:])

print(miLista.index("Antonio"))
print(miLista.index("Lucía"))

miLista.append("Marta")
print(miLista[:])
print(miLista.index("Marta"))


print("pepe" in miLista)
print("Leonel" in miLista)





miLista2 = ["Maria", 5, True, 78.35]
print(miLista2[:])
print(miLista2[2])

miLista2.extend(["Sandra", "Ana", "Lucia"])
miLista2.remove("Ana")
print(miLista2[:])

miLista2.remove(5)
print(miLista2[:])

miLista2.pop()
print(miLista2[:])





miLista3 = ["Mario", 3, False, 69.696969]
miLista4 = ["Juan", "Luis"]

miLista5 = miLista3 + miLista4
print(miLista5[:])

miLista3 = ["Mario", 3, False, 69.696969] * 3
print(miLista3[:])
