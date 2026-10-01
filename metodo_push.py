# Método Push

# Inventario inicial
inventario = 10

# Pronóstico de demanda para 5 días
pronostico = [25, 30, 20, 35, 25]

# Demanda real para 5 días
demanda_real = [30, 25, 40, 30, 20]

# Producción planeada (Push) según pronóstico
produccion = pronostico.copy()

print("Día | Pronóstico | Producción | Demanda Real | Inventario final | Sobrante | Faltante")
print("-------------------------------------------------------------------------------------")

for dia in range(5):

    # Se produce antes de que llegue la demanda (Push)
    inventario += produccion[dia]

    # Demanda real del día
    demanda = demanda_real[dia]

    # Inicializar sobrante y faltante
    sobrante = 0
    faltante = 0

    # Se atiende la demanda
    if inventario >= demanda:
        inventario -= demanda
        sobrante = inventario
    else:
        # Si no alcanza, se calcula el faltante
        faltante = demanda - inventario
        inventario = 0

    # Mostrar resultados del día
    print(
        dia + 1, "|",
        pronostico[dia], "|",
        produccion[dia], "|",
        demanda, "|",
        inventario, "|",
        sobrante, "|",
        faltante
    )