# Quick Sort Iterativo
items = []
n = 0
# Punteros/estado para Quick Sort Iterativo
stack = []       # Pila para almacenar los índices (low, high) de los sub-arreglos
fase = "INIT"    # INIT, PARTITION_SETUP, PARTITIONING, SWAP_PIVOT, NEXT_SUBARRAY
low = 0          # Índice inferior del sub-arreglo actual
high = 0         # Índice superior del sub-arreglo actual
pivot_index = 0  # Índice del pivote (generalmente high)
store_index = 0  # Índice para el particionamiento (Lomuto: store_index es el índice del próximo elemento < pivote)
i = 0            # Índice para recorrer el sub-arreglo durante la partición (Lomuto: i recorre de low a high-1)

def init(vals):
    global items, n, stack, fase, low, high, pivot_index, store_index, i
    items = list(vals)
    n = len(items)

    # Reinicializar estado
    stack = []
    low = 0
    high = n - 1
    pivot_index = 0
    store_index = 0
    i = 0

    # Si hay más de un elemento, agregamos los límites del arreglo completo a la pila
    if n > 1:
        # Se puede mejorar agregando primero el sub-arreglo más grande para optimizar el espacio de pila (Tail Call Optimization)
        stack.append((0, n - 1))

    fase = "INIT" # Establecer fase inicial

def step():
    global i, n, items, stack, fase, low, high, pivot_index, store_index

    # --- FASE: NEXT_SUBARRAY / INIT ---
    if fase == "INIT" or fase == "NEXT_SUBARRAY":
        # Si la pila está vacía, el algoritmo ha terminado
        if not stack:
            fase = "DONE"
            return {"done": True}

        # Sacar el siguiente sub-arreglo de la pila
        low, high = stack.pop()

        # Si el sub-arreglo tiene 0 o 1 elemento, está ordenado
        if low >= high:
            fase = "NEXT_SUBARRAY" # Ir directamente al siguiente
            return {"low": low, "high": high, "info": "Sub-arreglo de 0/1 elemento, ya ordenado."}

        # Iniciar la partición
        fase = "PARTITION_SETUP"
        # Continuar en la siguiente fase en la misma llamada
        return step()

    # --- FASE: PARTITION_SETUP ---
    elif fase == "PARTITION_SETUP":
        # 1. Elegir el pivote (usamos el último elemento: Lomuto)
        pivot_index = high
        pivot_value = items[pivot_index]

        # 2. Inicializar índices para el particionamiento
        # store_index apunta a la posición del primer elemento >= pivote
        store_index = low
        i = low
        fase = "PARTITIONING"

        # Retornar el pivote elegido para visualización
        return {"a": pivot_index, "info": f"Pivote elegido: {pivot_value} en índice {pivot_index}"}

    # --- FASE: PARTITIONING ---
    elif fase == "PARTITIONING":
        # 3. Recorrer el sub-arreglo (Lomuto: i va de low hasta high-1)
        if i < high:
            a = i # Elemento a comparar
            b = pivot_index # El pivote (high) se puede usar como 'b' de referencia
            swap_occurred = False
            info = ""
            
            # Comparación
            if items[i] < items[pivot_index]:
                # El elemento es menor que el pivote. Intercambiar items[i] con items[store_index]
                # y luego avanzar store_index.
                
                # CORRECCIÓN CLAVE: Eliminar la condición "if i != store_index"
                # y realizar el intercambio incondicionalmente para mover el elemento pequeño.
                
                if i != store_index:
                    items[i], items[store_index] = items[store_index], items[i]
                    swap_occurred = True
                    # El intercambio es entre 'i' y 'store_index'
                    info = f"Intercambio: {items[store_index]} < Pivote"
                    a_return = i
                    b_return = store_index
                else:
                    # No hay intercambio si los índices son iguales, solo se avanza store_index.
                    # El elemento items[i] (que es < pivote) ya está en su lugar.
                    info = f"Comparación: {items[i]} < Pivote (store_index avanza)"
                    a_return = i
                    b_return = pivot_index
                    
                store_index += 1 # store_index SIEMPRE avanza si items[i] < pivote
            
            else:
                # El elemento es mayor o igual que el pivote, solo avanzar i
                info = f"Comparación: {items[i]} >= Pivote"
                a_return = i
                b_return = pivot_index
            
            i += 1 # i SIEMPRE avanza
            
            # Retorno del paso
            return {"a": a_return, "b": b_return, "swap": swap_occurred, "pivot": pivot_index, "info": info}

        # Si i == high, hemos terminado el bucle de particionamiento
        else:
            fase = "SWAP_PIVOT"
            # Continuar en la siguiente fase en la misma llamada
            return step()

    # --- FASE: SWAP_PIVOT ---
    elif fase == "SWAP_PIVOT":
        # 4. Colocar el pivote en su posición final: intercambiar el pivote (high) con items[store_index]
        a = pivot_index # high
        b = store_index
        items[a], items[b] = items[b], items[a]

        # Posición final del pivote
        p = store_index

        # 5. Agregar los sub-arreglos resultantes a la pila
        
        # Estrategia de optimización (para reducir la pila): 
        # Insertar el sub-arreglo MÁS GRANDE primero.

        left_size = p - low
        right_size = high - p

        if left_size > right_size:
            # Primero sub-arreglo IZQUIERDO: low a p-1
            if low < p - 1:
                stack.append((low, p - 1))
            # Luego sub-arreglo DERECHO: p+1 a high
            if p + 1 < high:
                stack.append((p + 1, high))
        else:
             # Primero sub-arreglo DERECHO: p+1 a high
            if p + 1 < high:
                stack.append((p + 1, high))
            # Luego sub-arreglo IZQUIERDO: low a p-1
            if low < p - 1:
                stack.append((low, p - 1))


        fase = "NEXT_SUBARRAY"
        # Retornar el intercambio final del pivote
        return {"a": a, "b": b, "swap": True, "pivot_final": b, "info": f"Pivote colocado en posición final {b}."}

    # --- FASE: DONE ---
    return {"done": True}
