# Contrato:
# init(vals)
# step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # índice del elemento que queremos insertar en la parte ordenada
j = None   # cursor que recorre hacia la izquierda (None = todavía no arrancó)

def init(vals):
    global items, n, i, j

    items = list(vals)
    n = len(items)

    # En insertion sort se empieza desde el segundo elemento (índice 1)
    i = 1
    j = None


def step():
    global items, n, i, j

    # -----------------------------------
    # 1) Ya no quedan elementos para insertar → terminó
    # -----------------------------------
    if i >= n:
        return {"done": True}

    # -----------------------------------
    # 2) Si j es None, significa que recién empezamos a insertar items[i]
    # -----------------------------------
    if j is None:
        j = i      # arrancamos comparando items[i] con items[i-1]
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # -----------------------------------
    # 3) Mientras j > 0 y el elemento anterior es mayor → desplazar
    #    PERO como es "paso a paso", hacemos SOLO un swap por step().
    # -----------------------------------
    if j > 0 and items[j-1] > items[j]:
        a = j-1
        b = j
        items[a], items[b] = items[b], items[a]   # swap
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}

    # -----------------------------------
    # 4) Si no hay que desplazar → el elemento ya quedó en su lugar.
    #    Pasamos al siguiente i.
    # -----------------------------------
    i += 1
    j = None

    # Todavía no terminamos el algoritmo
    return {"done": False}
