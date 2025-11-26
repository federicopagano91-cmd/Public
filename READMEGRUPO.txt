# README

## Integrantes
- Federico Pagano
- Santiago Julio
- Ana Rebeco

## Algoritmos implementados
- Bubble Sort (`sort_bubble.py`)
- Selection Sort (`sort_selection.py`)
- Insertion Sort (`sort_insertion.py`)

## Notas de implementación

Todos los algoritmos cumplen el contrato `init(vals)` y `step()`, lo que permite ejecutarlos paso a paso en un visualizador.

Se usan variables globales para “guardar” el estado del algoritmo entre pasos. Cada vez que se llama a `step()`, el algoritmo continúa desde el punto en que quedó, sin reiniciar el proceso.

Se retorna un diccionario con las claves `{"a", "b", "swap", "done"}` en todos los pasos, incluso cuando no hay swap, para asegurar que el visualizador actualice correctamente las barras.

### Bubble Sort
- **Variables principales:** `i` (contador de pasadas), `j` (índice actual dentro de la pasada).
- Cada paso compara solo dos elementos consecutivos y los intercambia si es necesario.
- **Dificultad:** controlar manualmente `i` y `j` sin usar bucles.

### Selection Sort
- **Variables principales:** `i` (cabeza de la parte no ordenada), `j` (cursor), `min_idx` (índice del mínimo), `fase` ("buscar"/"swap").
- Durante la fase "buscar" solo se comparan elementos; el swap ocurre al final de cada pasada.
- **Nota:** `min_idx` se muestra en cada comparación para que el visualizador destaque el mínimo actual.

### Insertion Sort
- **Variables principales:** `i` (elemento a insertar), `j` (cursor que recorre hacia la izquierda).
- Se empieza desde el segundo elemento (índice 1) y se inserta en la sublista ordenada a la izquierda.
- Cada paso mueve solo un elemento a la vez.
- **Nota:** incluso cuando no se hace swap, se retorna un diccionario con los índices para que el visualizador actualice correctamente las barras.

### Decisiones comunes
- Todos los algoritmos permiten visualizar paso a paso el ordenamiento.
- Cada vez que se intercambian elementos, lo hacemos con una línea de código específica y se indica en el diccionario devuelto, para que el visualizador pueda mostrarlo paso a paso.
- Claridad en la visualización del proceso: cada acción del algoritmo (comparación, swap, avance de índices) está registrada paso a paso. Esto permite que un visualizador pueda mostrar exactamente lo que ocurre en cada micro-paso 
del ordenamiento.
