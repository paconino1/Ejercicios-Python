""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 15: Comprobador de Años Bisiestos
 Un año es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por
 400. Crea un programa que determine si un año introducido por teclado cumple estas
 condiciones.
 ============================================================================== """

año = int(input("Introduzca un año: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
  print(f"El año {año} es bisiesto")
else:
  print(f"El año {año} no es bisiesto")
