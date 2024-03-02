# Crear_un_codigo_que_me_de_las_temperaturas_de_dos_ciudades_distintas
print("Hello")
print("Which city's temperature are you interested in?")
chosen_city = input("Enter a city (Puyo, Guayaquil, Ambato): ").capitalize()

temperatures = {
    "Puyo": [
        [
            [20, 21, 22, 23, 24, 25, 26],  # Semana 1
            [19, 20, 21, 22, 23, 24, 25],  # Semana 2
            [18, 19, 20, 21, 22, 23, 24],  # Semana 3
            [17, 18, 19, 20, 21, 22, 23]   # Semana 4
        ]
    ],
    "Guayaquil": [
        [
            [25, 26, 27, 28, 29, 30, 31],  # Semana 1
            [24, 25, 26, 27, 28, 29, 30],  # Semana 2
            [23, 24, 25, 26, 27, 28, 29],  # Semana 3
            [22, 23, 24, 25, 26, 27, 28]   # Semana 4
        ]
    ],
    "Ambato": [
        [
            [18, 19, 20, 21, 22, 23, 24],  # Semana 1
            [17, 18, 19, 20, 21, 22, 23],  # Semana 2
            [16, 17, 18, 19, 20, 21, 22],  # Semana 3
            [15, 16, 17, 18, 19, 20, 21]   # Semana 4
        ]
    ]
}

# Obtener las temperaturas para la ciudad seleccionada
city_temperatures = temperatures.get(chosen_city)

# Si la ciudad seleccionada existe, mostrar las temperaturas
if city_temperatures:
    for capa in city_temperatures:
        for semana, fila in enumerate(capa, start=1):
            total_temp = 0
            for temp in fila:
                total_temp += temp
            average_temp = total_temp / len(fila)
            print(f"Week {semana}: Average Temperature: {average_temp:.2f}°C")
else:
    print("City not found. Please enter a valid city.")
