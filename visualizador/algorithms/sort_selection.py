# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"


def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"


def step():
    global items, n, i, j, min_idx, fase

    # ----------------------------------------------------
    # 1) Si i llegó al final → terminó el algoritmo
    # ----------------------------------------------------
    if i >= n - 1:
        return {"done": True}

    # ----------------------------------------------------
    # FASE 1: BUSCAR EL MÍNIMO EN LA SUBLISTA items[i..n-1]
    # ----------------------------------------------------
    if fase == "buscar":

        # Si j está dentro de la lista, comparamos
        if j < n:

            # Usamos j_actual para devolver la comparación de este step
            j_actual = j

            # Comparamos el actual con el mínimo encontrado hasta ahora
            if items[j] < items[min_idx]:
                min_idx = j

            # Avanzamos j para la próxima comparación
            j += 1

            return {
                "a": min_idx,      # índice del mínimo actual
                "b": j_actual,     # índice comparado
                "swap": False,
                "done": False
            }

        else:
            # Ya no quedan más comparaciones → pasamos a la fase de swap
            fase = "swap"

    # ----------------------------------------------------
    # FASE 2: HACER EL SWAP (SOLO UNO)
    # ----------------------------------------------------
    if fase == "swap":

        # Si el mínimo no está en i, intercambiamos
        if min_idx != i:
            a = i
            b = min_idx
            items[a], items[b] = items[b], items[a]

            # Después del swap avanzamos a la siguiente pasada
            # pero este step ya termina aquí
            fase = "buscar"
            i += 1
            j = i + 1
            min_idx = i

            return {
                "a": a,
                "b": b,
                "swap": True,
                "done": False
            }

        # Si min_idx == i → no se hace swap
        # Simplemente avanzamos a la siguiente pasada
        fase = "buscar"
        i += 1
        j = i + 1
        min_idx = i

        return {
            "a": i - 1,   # no hubo swap, pero indicamos posición "tocada"
            "b": i - 1,
            "swap": False,
            "done": False
        }
