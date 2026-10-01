""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 7: Formateador de Nombres de Usuarios
 Escribe un programa que pida el nombre completo de una persona. La salida debe mostrar:
1. El nombre completo en mayúsculas.
2. El nombre completo en minúsculas.
3. El nombre con la primera letra de cada palabra en mayúscula (Title Case).
4. La cantidad total de caracteres (sin contar los espacios en blanco).
 ============================================================================== """

nombre = input("Introduzca su nombre completo: ")

nombre_sin_espacios = nombre.replace(" ","")

print(nombre.upper())
print(nombre.lower())
print(nombre.title())
print(f"Hay {len(nombre_sin_espacios)} caracteres.")