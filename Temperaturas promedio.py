# Temperatura promedio de las 3 ciudades durante el período  de 4 semanas
def calcular_temperatura_promedio_semanal(ciudad_temperaturas):
    total_temperaturas = sum(ciudad_temperaturas)
    temperatura_promedio = total_temperaturas / len(ciudad_temperaturas)
    return temperatura_promedio

# Datos de temperatura para cada ciudad durante 4 semanas
# Temperaturas en grados Celsius

Quito_temperaturas = [19, 27, 33, 30]
Guayaquil_temperaturas = [40, 45, 41, 43]
Cuenca_temperaturas = [31, 30, 41, 23]

# Calcular temperatura promedio semanal para cada ciudad

temp_prom_Quito = calcular_temperatura_promedio_semanal(Quito_temperaturas)
temp_prom_Guayaquil = calcular_temperatura_promedio_semanal(Guayaquil_temperaturas)
temp_prom_Cuenca = calcular_temperatura_promedio_semanal(Cuenca_temperaturas)

print("Temperatura promedio semanal:")
print(f"Quito: {temp_prom_Quito}°C")
print(f"Guayaquil: {temp_prom_Guayaquil}°C")
print(f"Cuenca {temp_prom_Cuenca}°C")