""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 12: Control de Acceso al Servidor
 Para acceder a un servidor del centro se requiere tener al menos 18 años y poseer el rol de
 "admin" o "profesor". Escribe un script que pida la edad y el rol del usuario y determine si tiene
 acceso concedido.
 ============================================================================== """

edad = int(input("Introduzca su edad: "))
rol = input("Introduzca su rol en el centro: ")

if edad >= 18 and (rol == "admin" or rol == "profesor"):
  print("Acceso concedido")
else:
  print("Acceso denegado")