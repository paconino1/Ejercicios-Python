""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 11: Clasificador de Números
 Pide un número entero al usuario e indica mediante un condicional si el número es positivo,
 negativo o cero, y si además es par o impar.
 ============================================================================== """

numero = int(input("Introduzca un número entero: "))

if numero == 0:
  print("El número es cero.")
elif numero > 0:
  print("El número es positivo.")
else:
  print("El número es negativo.")

if numero % 2 == 0:
  print("El número es par.")
else:
  print("El número es impar.")