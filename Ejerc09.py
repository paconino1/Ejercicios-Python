""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 9: Detector de Subcadenas
 Pide al usuario un texto largo y una palabra de búsqueda. El programa debe indicar mediante
 un booleano (True/False) si la palabra está presente en el texto, ignorando diferencias entre
 mayúsculas y minúsculas.
 ============================================================================== """

texto = input("Introduzca un texto largo: ").lower()
palabra = input("Introduzca una palabra de búsqueda: ")
existe_palabra = palabra.lower() in texto

if existe_palabra:
  print(f"La palabra {palabra} existe en el texto.")
else:
  print(f"La palabra {palabra} no existe en el texto.")