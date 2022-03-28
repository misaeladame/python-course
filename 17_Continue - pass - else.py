for letra in "Python":
  if letra == "h":
    continue
  print("Viendo la letra: " +letra)

print()
#------------------------------------------------------------------
nombre = "Pildoras informaticas"

contador=0

for i in nombre:
  if i == " ":
    continue
  contador+=1

print(contador)

print()
"""
#-------------------------------------------------------------------
while True:
  pass # devuelve un null
#-------------------------------------------------------------------
class MiClase:
  pass # Para implementar mas tarde
#-------------------------------------------------------------------
"""
email=input("Introduce tu email, por favor: ")
for i in email:
  if i == "@":
    arroba = True
    break
else:
  arroba = False

print(arroba)