""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 13: Calculadora de Calificaciones Oficiales
 Escribe un programa que lea la nota numérica de un examen (entre 0 y 10, con decimales) y
 devuelva la calificación cualitativa según el criterio oficial:
 ● : Suspenso
 ● : Aprobado
 ● : Bien
 ● : Notable
 ● : Sobresaliente
 ============================================================================== """

nota = float(input("Introduzca su nota: "))

if nota >= 9:
  print ("Sobresaliente")
elif nota >= 7:
  print ("Notable")
elif nota >= 6:
  print ("Bien")
elif nota >= 5:
  print ("Aprobado")
else:
  print("Suspenso")