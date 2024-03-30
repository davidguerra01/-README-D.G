# Operaciones de lectura y escritura en archivos de texto en Python.
# Abrir el archivo en modo escritura
with open("my_notes.txt", "w") as f:
    # Escribir mis notas personales
    f.write("Nota 1: Llenar la despensa de la semana\n")
    f.write("Nota 2: Programar una cita con el odontologo\n")
    f.write("Nota 3: Realizar los pagos de los servicios básicos\n")
# Abrir el archivo en modo lectura
with open("my_notes.txt", "r") as f:
    # Leer el contenido del archivo línea por línea
    for line in f:
        print(line)