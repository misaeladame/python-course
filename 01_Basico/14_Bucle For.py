#----------------------------------------------------------------------------
for i in [1,2,3]:
  print("Hola")

print()

#----------------------------------------------------------------------------
for i in ["primavera","verano","otoño", "invierno"]:
  print(i)

print()

#----------------------------------------------------------------------------
for i in ["Pildoras", "Informaticas", 3]:
  print("Hola", end=" ")

print()

#----------------------------------------------------------------------------
# Imprime tantas veces como caracteres hay en el String
for i in "misael_adame@protonmail.com":
  print("Hola", end=" ")

print()

#----------------------------------------------------------------------------
email = False
miEmail = input("Introduce tu direccion de email: ")
for i in miEmail:
  if(i=="@"):
    email = True

if email:
  print("Email es correcto")
else:
  print("El email no es correcto")

print()

#----------------------------------------------------------------------------
contador = 0
miEmail = input("Introduce tu dirección de email: ")

for i in miEmail:
  if (i=="@" or i=="."):
    contador=contador+1

if contador == 2:
  print("Email es correcto")
else:
  print("El email no es correcto")

print()
#----------------------------------------------------------------------------
#Tipo range
#          Va del 0 hasta el 4
for i in range(5):
  # Funcion f para concatenar facilmente variables de cualquier tipo y Strings
  print(f"valor de la variable {i}")

print()
#----------------------------------------------------------------------------
for i in range(5,10):
  print(f"valor de la variable {i}")

print()
#----------------------------------------------------------------------------
for i in range(5,50,3):
  print(f"valor de la variable {i}")

print()
#----------------------------------------------------------------------------
valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):
  if email[i]=="@":
    valido = True

if valido:
  print("Email correcto")
else:
  print("Email incorrecto")
