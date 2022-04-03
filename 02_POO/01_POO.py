class Coche():

  def __init__(self):
    # 4 propiedades
    # self = this
    # __ = private

    self.__largoChasis = 250 
    self.__anchoChasis = 120
    self.__ruedas = 4
    self.__enmarcha = False

  # 2 comportamientos
  def arrancar(self,arrancamos):
    self.__enmarcha = arrancamos

    if(self.__enmarcha):
      return "El coche está en marcha"
    else:
      return "El coche está parado"

  def estado(self):
    print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

miCoche = Coche()  # Instanciar una clase

# print("El largo del coche es:", miCoche.largoChasis)
# print("El coche tiene", miCoche.ruedas, "ruedas")
print(miCoche.arrancar(True))
miCoche.estado()

print("------------- A continuación creamos el segundo objeto -----------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()
