""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 17: Sumador Continuo hasta Cero
 Escribe un programa que lea números enteros por teclado de manera continua y los vaya
 sumando. La lectura finalizará cuando el usuario introduzca el número 0. Al terminar, muestra la
 suma total.
 ============================================================================== """

numero = int(input("Introduce un número entero (0 para finalizar): "))
suma_total = 0

while numero != 0:
    suma_total += numero
    numero = int(input("Introduce otro número entero (0 para finalizar): "))

print(f"La suma total es: {suma_total}")