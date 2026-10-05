""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 25: Pide la altura de un triángulo y dibuja en consola un patrón
 como el siguiente.
 ============================================================================== """

altura = int(input("Introduzca la altura de un triángulo: "))

for i in range(1, altura+1):
  print(i * "*")