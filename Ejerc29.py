""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 29: Registro del Mayor y Menor Número 
 Solicita al usuario la cantidad de números que desea introducir. A continuación, pide esa 
 cantidad de números enteros y determina cuál ha sido el valor máximo y cuál el mínimo 
 introducido.
 ============================================================================== """

cantidad_numeros = int(input("Introduce la cantidad de números que deseas ingresar: "))

if cantidad_numeros <= 0:
    print("La cantidad de números debe ser mayor que cero.")
else:
    numero = int(input("Introduce el primer número: "))
    maximo = numero
    minimo = numero

    for i in range(1, cantidad_numeros):
        numero = int(input("Introduce el siguiente número: "))
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    print(f"El valor máximo introducido es: {maximo}")
    print(f"El valor mínimo introducido es: {minimo}")