
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    # Si ya terminamos todas las pasadas
    if i >= n - 1:
        return {"done": True}

    # Si llegamos al final de una pasada, reiniciamos j y avanzamos i
    if j >= n - i - 1:
        j = 0
        i += 1
        if i >= n - 1:
            return {"done": True}

    # Índices a comparar en este micro-paso
    a = j
    b = j + 1
    swap = False

    # Comparación e intercambio si corresponde
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzamos puntero j para el siguiente paso
    j += 1

    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False
    }
