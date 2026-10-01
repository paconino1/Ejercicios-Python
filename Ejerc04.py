# ==============================================================================
# Autor: Francisco Niño Caballero
#
# Enunciado: Ejercicio 4: Desglose de Tiempo
# Escribe un programa que solicite una cantidad total de segundos (entero) y calcule a cuántas
# horas, minutos y segundos equivalen.
# Pista: Utiliza división entera (//) y el operador módulo (%).
# ==============================================================================

total_segundos = int(input("Escribe una cantidad de segundos: "))

while total_segundos>0:
    if total_segundos>=3600:
        horas = total_segundos//3600
        total_segundos-=(3600 * horas)
    elif total_segundos>=60:
        minutos = total_segundos//60
        total_segundos-=(60 * minutos)
    else:
        segundos=total_segundos
        total_segundos=0

print(f"Equivalen a {horas} horas, {minutos} minutos y {segundos} segundos")      