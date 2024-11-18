Fundamentos de programación en Python
=====================================

Código de los libros:

- _Learning Python -5th edition-_ por Mark Lutz 
- _Python Notes for Professionals, free programming books_ de [GoalKicker.com](https://goalkicker.com/)

## Requisitos opcionales

Para eliminar los metadatos de un _jupyter notebook_ instala el paquete [nb-clean](https://pypi.org/project/nb-clean/):

### Opción 1

`python -m venv venv`

`source venv/bin/activate`

`pip install nb-clean`

### Opción 2

`python -m venv venv`

`source venv/bin/activate`

`pip install requirementents.txt`


En mi caso, preservo las salidas de las celdas puesto que me interesa dejarlas en seguimiento `git`, ya que forman parte de la documentación. El resto de metadatos, sobretodo el número de ejecuciones de la celda, las elimino para evitar cambios en el _index_.

Despues de ejecutar una o todas las celdas de un _notebook_ ejecuta desde consola:

`nb-clean clean --preserve-cell-outputs conjuntos.ipynb`
