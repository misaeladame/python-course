class Coche():

  # Constructor
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
      chequeo = self.__chequeo_interno()


    if(self.__enmarcha and chequeo):
      return "El coche está en marcha"
    elif(self.__enmarcha and chequeo==False):
      return "Algo ha ido mal en el chequeo, no podemos arrancar"
    else:
      return "El coche está parado"

  def estado(self):
    print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

  def __chequeo_interno(self):
    print("Realizando chequeo interno")

    self.gasolina = "ok"
    # self.aceite = "ok"
    self.aceite = "mal"
    self.puertas = "cerradas"

    if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
      return True
    else:
      return False  

miCoche = Coche()  # Instanciar una clase

# print("El largo del coche es:", miCoche.largoChasis)
# print("El coche tiene", miCoche.ruedas, "ruedas")
print(miCoche.arrancar(True))
miCoche.estado()

# print(miCoche.chequeo_interno())

print("------------- A continuación creamos el segundo objeto -----------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()

# print(miCoche2.chequeo_interno())