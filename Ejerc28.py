""" ==============================================================================
 Autor: Francisco Niño Caballero

 Ejercicio 28: Filtro y Acumulador de Ventas
 Simula un sistema de ventas. Procesa una lista predefinida de importes de ventas [45, 120, 230,
 80, 500, 15]. Cuenta cuántas ventas superan los 100€, acumula el total de dichas ventas
 "destacadas" e indica mediante un flag si se ha superado un objetivo global de 700€.
 ============================================================================== """

importes_ventas = [45, 120, 230, 80, 500, 15]
suma_total = 0
destacadas = 0

meta = False

for venta in importes_ventas:
  if venta > 100:
    destacadas += 1
    suma_total += venta

  if suma_total>700:
    meta = True

print(f"Ventas destacadas: {destacadas}")

if meta:
  print("Meta alcanzada: ¡Superamos los 700€!")
else:
  print("No alcanzamos la meta")