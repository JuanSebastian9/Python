# Crear una matriz 31x24 con temperaturas inicializadas en 0.0
temps = [[0.0 for h in range(24)] for d in range(31)]

#
# La matriz se actualiza aquí con mediciones reales.
# Ejemplo: temps[0][11] = 25.5 (Día 1, temperatura al mediodía: 25.5°C)
#

# Calcular la temperatura promedio al mediodía
total = 0.0

for day in temps:
    total += day[11]  # Sumar la temperatura del mediodía de cada día

average = total / 31  # Dividir por la cantidad de días

print("Temperatura promedio al mediodía:", average)

# Encontrar la temperatura más alta del mes
highest = -100.0

for day in temps:
    for temp in day:  # Revisar cada hora del día
        if temp > highest:
            highest = temp  # Actualizar la temperatura más alta

print("La temperatura más alta fue:", highest)

# Contar los días con temperatura al mediodía de al menos 20°C
hot_days = 0

for day in temps:
    if day[11] > 20.0:  # Verificar si la temperatura al mediodía supera 20°C
        hot_days += 1

print(hot_days, "fueron los días calurosos.")
