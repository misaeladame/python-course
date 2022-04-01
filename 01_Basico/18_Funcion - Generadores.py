# Función "tradicional"
def generaPares(limite):
  num = 1
  miLista = []
  while num<limite:
    miLista.append(num*2)
    num=num+1
  return miLista

print(generaPares(10))

# Utilizando un generador
def generaParesGenerador(limite):
  num=1
  while num<limite:
    yield num*2
    num=num+1

devuelvePares = generaParesGenerador(10)
for i in devuelvePares:
  print(i)

print("Aquí podría ir más código")
devuelvePares = generaParesGenerador(10)
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))