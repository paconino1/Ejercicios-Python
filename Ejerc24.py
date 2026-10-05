""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 24: Cálculo de Factorial
 Crea un programa que pida un entero no negativo y calcule su factorial
 utilizando un bucle for.
 ============================================================================== """

numero = int(input("Introduzca un entero no negativo: "))
resultado = 1

while numero < 0:
  numero = int(input("Introduzca un entero no negativo: "))

if numero == 0:
  print(f"{numero}! = 1")
else:
  for i in range(1, numero+1):
    resultado *= i

  print(f"{numero}! = {resultado}")