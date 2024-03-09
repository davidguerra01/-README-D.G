# farenheit= (9/5)*(grad_cent+32)
# kelvin= 273.15+grad_cent

def celsius_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convertir_grados(celsius):
    farenheit = celsius_to_farenheit(celsius)
    kelvin = celsius_to_kelvin(celsius)
    return farenheit, kelvin

# Ejemplo de uso:
grados_celsius = 30
farenheit, kelvin = convertir_grados(grados_celsius)
print(f"{grados_celsius} grados Celsius son {farenheit} grados Farenheit y {kelvin} grados Kelvin.")