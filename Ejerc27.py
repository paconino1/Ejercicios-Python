""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 27: Buscador de Números Primos (Flag)
 Crea un programa que reciba un número entero mayor que 1 y determine si es primo utilizando
 un indicador (flag) booleano y un bucle.
 ============================================================================== """

numero = int(input("Introduzca un número entero mayor que uno: "))
flag = True
numero_divisiones = 0
divisor = 1

while numero < 2:
  numero = int(input("Introduzca un número entero mayor que uno: "))

while flag and divisor < numero+1:
  if numero % divisor == 0:
    numero_divisiones += 1

  divisor += 1

  if numero_divisiones > 2:
    flag = False

if flag:
  print(f"El número {numero} es primo")
else:
  print(f"El número {numero} no es primo")
