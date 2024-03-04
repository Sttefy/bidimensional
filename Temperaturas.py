# Crear_un_codigo_que_me_de_las_temperaturas_de_dos_ciudades_distintas
temperatures = [
    # Ciudad: Puyo
    [
        {"city": "Puyo"},  # Información de la ciudad
        [  # Semana 1
            {"day": "Monday", "temp": 23},
            {"day": "Tuesday", "temp": 12},
            {"day": "Wednesday", "temp": 32},
            {"day": "Thursday", "temp": 25},
            {"day": "Friday", "temp": 18},
            {"day": "Saturday", "temp": 22},
            {"day": "Sunday", "temp": 28},
        ],
        [  # Semana 2
            {"day": "Monday", "temp": 12},
            {"day": "Tuesday", "temp": 22},
            {"day": "Wednesday", "temp": 15},
            {"day": "Thursday", "temp": 27},
            {"day": "Friday", "temp": 17},
            {"day": "Saturday", "temp": 32},
            {"day": "Sunday", "temp": 19},
        ],
        [  # semana 3
            {"day": "Monday", "temp": 28},
            {"day": "Tuesday", "temp": 32},
            {"day": "Wednesday", "temp": 23},
            {"day": "Thursday", "temp": 22},
            {"day": "Friday", "temp": 12},
            {"day": "Saturday", "temp": 25},
            {"day": "Sunday", "temp": 18},
        ],
        [   # semana 4
             {"day": "Monday", "temp": 20},
             {"day": "Tuesday", "temp": 31},
             {"day": "Wednesday", "temp": 18},
             {"day": "Thursday", "temp": 29},
             {"day": "Friday", "temp": 31},
             {"day": "Saturday", "temp": 24},
             {"day": "Sunday", "temp": 21},
        ],
    ],
    [
        {"city": "Guayaquil"},
        [   # semana 1
             {"day": "Monday", "temp": 32},
             {"day": "Tuesday", "temp": 26},
             {"day": "Wednesday", "temp": 31},
             {"day": "Thursday", "temp": 30},
             {"day": "Friday", "temp": 18},
             {"day": "Saturday", "temp": 30},
             {"day": "Sunday", "temp": 28},
        ],
        [   # semana 2
             {"day": "Monday", "temp": 15},
             {"day": "Tuesday", "temp": 24},
             {"day": "Wednesday", "temp": 18},
             {"day": "Thursday", "temp": 16},
             {"day": "Friday", "temp": 24},
             {"day": "Saturday", "temp": 32},
             {"day": "Sunday", "temp": 20},
        ],
        [   # semana 3
             {"day": "Monday", "temp": 16},
             {"day": "Tuesday", "temp": 30},
             {"day": "Wednesday", "temp": 32},
             {"day": "Thursday", "temp": 21},
             {"day": "Friday", "temp": 29},
             {"day": "Saturday", "temp": 15},
             {"day": "Sunday", "temp": 22},
        ],
        [   # semana 4
             {"day": "Monday", "temp": 25},
             {"day": "Tuesday", "temp": 15},
             {"day": "Wednesday", "temp": 24},
             {"day": "Thursday", "temp": 27},
             {"day": "Friday", "temp": 32},
             {"day": "Saturday", "temp": 24},
             {"day": "Sunday", "temp": 29},
        ],
    ],
    [
        {"city": "Ambato"},
        [   # semana 1
             {"day": "Monday", "temp": 17},
             {"day": "Tuesday", "temp": 15},
             {"day": "Wednesday", "temp": 18},
             {"day": "Thursday", "temp": 27},
             {"day": "Friday", "temp": 14},
             {"day": "Saturday", "temp": 20},
             {"day": "Sunday", "temp": 15},
        ],
        [   # semana 2
             {"day": "Monday", "temp": 16},
             {"day": "Tuesday", "temp": 14},
             {"day": "Wednesday", "temp": 20},
             {"day": "Thursday", "temp": 14},
             {"day": "Friday", "temp": 18},
             {"day": "Saturday", "temp": 15},
             {"day": "Sunday", "temp": 15},
        ],
        [   # semana 3
             {"day": "Monday", "temp": 20},
             {"day": "Tuesday", "temp": 17},
             {"day": "Wednesday", "temp": 15},
             {"day": "Thursday", "temp": 14},
             {"day": "Friday", "temp": 15},
             {"day": "Saturday", "temp": 18},
             {"day": "Sunday", "temp": 18},
        ],
        [   # semana 4
             {"day": "Monday", "temp": 19},
             {"day": "Tuesday", "temp": 14},
             {"day": "Wednesday", "temp": 20},
             {"day": "Thursday", "temp": 18},
             {"day": "Friday", "temp": 16},
             {"day": "Saturday", "temp": 15},
             {"day": "Sunday", "temp": 14},
        ],
    ]
]
# Obtener las temperaturas para la ciudad seleccionada
print("Hello")

no_ciudad = 0
for ciudad_temps in temperatures:
    no_ciudad += 1
    city_name = ciudad_temps[0]["city"]
    print(f"CIUDAD No. {no_ciudad}: {city_name}")
    no_semana = 0
    for semana in ciudad_temps[1:]:
        no_semana += 1
        suma = 0
        for day in semana:
            suma += day["temp"]
        promedio = round(suma / len(semana), 2)
        print(f"El promedio semana No. {no_semana} es: {promedio}")

