""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 23: Contador de Vocales
 Dado un texto introducido por el usuario, utiliza un bucle for para contar cuántas vocales (a, e, i,
 o, u) contiene en total.
 ============================================================================== """

texto = input("Introduzca un texto: ")
vocales = 0

for letra in texto:
  if letra.lower() in "aeiou":
    vocales += 1

print(f"Su texto contiene {vocales} vocales.")