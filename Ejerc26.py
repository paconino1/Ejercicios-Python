""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 26: Estadísticas de Evaluaciones
 El usuario introducirá 5 notas de alumnos. Utiliza un contador y un acumulador para determinar
 cuántos alumnos han aprobado y cuál es la nota media del grupo.
 ============================================================================== """

numero_aprobados = 0
suma_nota = 0

for i in range (1, 6):
  i = float(input("Introduzca la nota: "))
  suma_nota += i

  if i >= 5:
    numero_aprobados += 1

nota_media = suma_nota / 5

print(f"Alumnos aprobados: {numero_aprobados} \nNota media: {nota_media:.2f}")