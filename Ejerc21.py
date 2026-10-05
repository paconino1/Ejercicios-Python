""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 21: Tabla de Multiplicar
 Solicita un número entero del 1 al 10 e imprime su tabla de multiplicar completa (del 1 al 10) con
 el formato X x Y = Z.
 ============================================================================== """

numero = int(input("Introduzca un número del 1 al 10: "))

while numero < 1 or numero > 10:
  numero = int(input("Introduzca un número del 1 al 10: "))

for i in range(1, 11): 
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")