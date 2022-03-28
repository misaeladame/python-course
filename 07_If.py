print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno: ")
#nota_alumno = int(input("Introduce la nota del alumno: "))

def evaluacion(nota):
  valoracion = "aprobado"
  if nota < 5:
      valoracion = "reprobado"
  return valoracion


print(evaluacion(int(nota_alumno)))
#print(evaluacion(nota_alumno))