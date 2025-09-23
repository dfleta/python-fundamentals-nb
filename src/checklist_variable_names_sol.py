# Programa para calcular estadísticas básicas de un conjunto de datos
# Este programa contiene múltiples violaciones a las convenciones de nombres de variables

# Constantes con nombres poco descriptivos
PI = 3.14159  # ¿Por qué se usa "PI" aquí?

# Variables globales con nombres arbitrarios
g = [10, 20, 30, 40, 50]  # ¿Qué representa "g"?

# Función con un nombre genérico y parámetros poco descriptivos
def calc(x, y):
    # Variables temporales con nombres genéricos
    temp = sum(x) / len(x)  # ¿Qué representa "temp"?
    z = max(x)  # ¿Qué representa "z"?
    w = min(x)  # ¿Qué representa "w"?
    return temp, z, w

# Enumerados sin prefijo o sufijo que indique la categoría
RED = 1
GREEN = 2
BLUE = 3

# Función con un nombre que no describe su propósito
def doStuff():
    # Uso de nombres de variables booleanas poco claros
    flag = True  # ¿Qué significa "flag"?
    if flag:
        # Uso de nombres de variables que no describen su propósito
        a = calc(g, PI)
        print("Resultados:", a)

# Bucle con índices no significativos
for i in range(len(g)):
    print("Elemento", i, ":", g[i])

# Variables con nombres que hacen referencia a la solución en lugar del problema
inputRec = "Datos procesados"  # ¿Qué significa "inputRec"?

# Nombres intencionalmente mal escritos
hilite = "resaltar"  # ¿Por qué no "highlight"?

# Nombres que podrían ser malinterpretados
wrap = "envolver"  # ¿Es "wrap" o "rap"?

# Llamada a la función principal
doStuff()