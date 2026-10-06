""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 10: Ocultador de Datos Sensibles (Enmascaramiento)
 Solicita un número de tarjeta de crédito de 16 dígitos como cadena de texto. El programa debe
 mostrar la tarjeta ocultando los primeros 12 dígitos con asteriscos (*) y mostrando únicamente
 los últimos 4.
 ============================================================================== """

tarjeta = input("Ingrese su número de tarjeta de crédito (16 dígitos): ").replace(" ","")
tarjeta_oculta = "*" * 12 + tarjeta[12:17]

print(f"Tarjeta protegida: {tarjeta_oculta}")