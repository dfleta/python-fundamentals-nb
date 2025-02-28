Fundamentos de programación en Python
=====================================

Código de los libros:

- _Learning Python -5th edition-_ por Mark Lutz 
- _Python Notes for Professionals, free programming books_ de [GoalKicker.com](https://goalkicker.com/)

## Índice de Contenidos

### Conceptos Básicos
1. [Strings](notebooks/unidad_01_strings.ipynb) - Manipulación y operaciones con cadenas de texto

2. [Variables, Referencias y Objetos](notebooks/variables%20_referencias_objetos.ipynb) - Conceptos fundamentales sobre variables y objetos en Python
   - Objetos Inmutables
   - Objetos Mutables
   - Shared References and Equality
   - Cache

3. [Regla LEGB](notebooks/codigo_regla_LEGB.ipynb) - Explicación de la regla de alcance LEGB
   - GLOBAL SCOPE
   - LEGB rule
   - NESTED SCOPES
   - Factory Functions: Closures

### Estructuras de Datos
1. [Operaciones sobre Listas](notebooks/operaciones_sobre_listas.ipynb) - Manipulación y operaciones con listas
   - Basic List Operations
   - List Iteration and Comprehension

2. [Operaciones sobre Diccionarios](notebooks/operaciones_sobre_diccionarios.ipynb) - Trabajo con diccionarios y sus métodos
   - Cambiando diccionarios in place
   - Métodos de un objeto diccionario
   - values

3. [Conjuntos](notebooks/conjuntos.ipynb) - Operaciones y manipulación de conjuntos
   - Operaciones sobre conjuntos
   - Operaciones matemáticas (unión, intersección, diferencia)
   - Supersets y subsets

### Control de Flujo y Funciones
1. [Operadores Lógicos](notebooks/operadores_logicos.ipynb) - Uso de operadores lógicos y condicionales
   - Operadores lógicos
   - and
   - or
   - Tablas de verdad

2. [Argumentos](notebooks/argumentos.ipynb) - Manejo de argumentos en funciones
   - Arguments and Shared References
   - Special Argument-Matching Modes
   - Arbitrary Arguments Examples

3. [Excepciones](notebooks/excepciones.ipynb) - Manejo de errores y excepciones
   - Sintaxis de la sentencia try
   - Ejemplo try
   - Jerarquía de Excepciones

### Programación Avanzada
1. [Módulos](notebooks/modulos.ipynb) - Importación y uso de módulos
   - Creación módulos
   - Uso de módulos
   - sys.path
   - Sentencia import
   - Sentencia from
   - Sentencia from *
   - Importación única

2. [List Comprehensions](notebooks/cap_14_list_comprehensions.ipynb) - Creación de listas mediante comprensión
   - Extended List Comprehension Syntax
   - Filter clauses: if
   - Bucles anidados: for
   - Tuples
   - Range

3. [Comprensiones y Generadores](notebooks/cap_20_comprehensions_and_generators.ipynb) - Uso avanzado de comprensiones y generadores
   - List Comprehensions and Functional Tools
   - Example: List Comprehensions and Matrixes
   - Don't Abuse List Comprehensions: KISS

### Programación Funcional
1. [Programación Funcional](notebooks/cap_19_functional_programming_tools.ipynb) - Herramientas de programación funcional
   - Anonymous Functions: lambda
   - Mapping Functions over Iterables: map
   - Multiple sequence arguments
   - Selecting Items in Iterables: filter
   - Combining Items in Iterables: reduce
   - Ejercicios propuestos

2. [Ejercicios Codewars Funcional](notebooks/ejercicios_codewars_functional.ipynb) - Ejercicios prácticos de programación funcional

## Requisitos opcionales

Para eliminar los metadatos de un _jupyter notebook_ instala el paquete [nb-clean](https://pypi.org/project/nb-clean/):

### Opción 1

`python -m venv venv`

`source venv/bin/activate`

`pip install nb-clean`

### Opción 2

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirementents.txt`


En mi caso, preservo las salidas de las celdas puesto que me interesa dejarlas en seguimiento `git`, ya que forman parte de la documentación. El resto de metadatos, sobretodo el número de ejecuciones de la celda, las elimino para evitar cambios en el _index_.

Despues de ejecutar una o todas las celdas de un _notebook_ ejecuta desde consola:

`nb-clean clean --preserve-cell-outputs conjuntos.ipynb`
