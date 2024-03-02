# Matriz 3D para almacenar datos de temperatura
# Crear una lista de ciudades
ciudades = ['Quito', 'Guayaquil', 'Cuenca']

# Crear una lista de días de la semana
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Crear una lista de semanas
semanas = [1, 2, 3, 4]

# temperaturas de ciudades
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 37}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 47}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 44},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 49},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 49}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 42},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 52}
        ]
    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 52},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 56},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 33},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 47},
            {"day": "Domingo", "temp": 51}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 53},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 49}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 44},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 48},
            {"day": "Sábado", "temp": 55},
            {"day": "Domingo", "temp": 46}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 43},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 22}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 21},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 46},
            {"day": "Jueves", "temp": 44},
            {"day": "Viernes", "temp": 47},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 19},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 36}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)