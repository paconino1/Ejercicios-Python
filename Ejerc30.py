""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 30: Detector de Números Perfectos 
 Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo al 
 propio número). Crea un programa que determine si un número ingresado por el usuario es 
 perfecto
 ============================================================================== """

numero = int(input("Introduce un número para verificar si es perfecto: "))

if numero <= 1:
    print(f"{numero} no es un número perfecto.")
else:
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        print(f"{numero} es un número perfecto.")
    else:
        print(f"{numero} no es un número perfecto.")