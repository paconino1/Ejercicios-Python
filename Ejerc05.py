# ==============================================================================
# Autor: Francisco Niño Caballero
#
# Enunciado: Ejercicio 5: Factura de Módulo DAM
# Un comercio de componentes informáticos aplica un IVA del 21% a sus productos. Pide el
# nombre de un artículo y su precio base imponible. Muestra el importe del IVA aplicado y el
# precio final redondeado a dos decimales.
# ==============================================================================

nombre = input("Introduzca el nombre del artículo: ")
precio_base = float(input("Introduzca el precio base imponible del artículo: "))

iva = precio_base * 0.21
precio_final = precio_base + iva

print(f"Artículo: {nombre}\n IVA aplicado: {iva}\n Precio final: {precio_final:.2f}")