""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 19: Menú Interactivo de Consola
 Diseña un menú con tres opciones: 1. Saludar, 2. Calcular el doble de un número, 3. Salir. El
 programa debe ejecutarse en bucle mostrando el menú hasta que el usuario elija la opción 3.
 ============================================================================== """

numero = 0

while numero != 3:
    print("Menú:")
    print("1. Saludar")
    print("2. Calcular el doble de un número")
    print("3. Salir")
    numero = int(input("Elige una opción (1-3): "))

    if numero == 1:
        nombre = input("Introduce tu nombre: ")
        print(f"¡Hola, {nombre}!")
    elif numero == 2:
        num = float(input("Introduce un número: "))
        print(f"El doble de {num} es {num * 2}.")
    elif numero == 3:
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 3.")