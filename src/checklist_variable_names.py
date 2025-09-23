# Este programa contiene múltiples violaciones 
# a las convenciones de nombres de variables

# Instrucciones:
#  - Analiza el programa y encuentra todas las violaciones 
#    a las convenciones de nombres de variables descritas 
#    en la lista de chequeo del capítulo 11 "The powe of 
#    variable names" del libro "Clean Code" de Robert C. Martin.
#  - Para cada violación, explica por qué el nombre no cumple
#    con la convención y propon un nombre alternativo que 
#    respete las buenas prácticas.
#  - Refactoriza el programa para corregir todas las violaciones
#    y asegúrate de que sea más legible y mantenible.

PI = 3.14159  # ¿Por qué se usa "PI" aquí?

g = [10, 20, 30, 40, 50]  # ¿Qué representa "g"?

def calc(x, y):
    temp = sum(x) / len(x)  # ¿Qué representa "temp"?
    z = max(x)  # ¿Qué representa "z"?
    w = min(x)  # ¿Qué representa "w"?
    return temp, z, w

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

for i in range(len(g)):
    print("Elemento", i, ":", g[i])

# Llamada a la función principal
doStuff()