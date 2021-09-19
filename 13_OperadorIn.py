print("Asignaturas optativas Año 2021")
print("Asignaturas optativas: Informática gráfica - Pruebas de Software - Usabilidad y Accesibilidad")
opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura.upper())
else:
    print("La asignatura escogida no está contemplada")
