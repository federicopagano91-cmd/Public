import time
import random
from sort_bubble import init as init_bubble, step as step_bubble
from sort_insertion import init as init_insertion, step as step_insertion
from sort_selection import init as init_selection, step as step_selection

def run_algorithm(init_func, step_func, data):
    init_func(list(data))
    swaps = 0
    start_time = time.perf_counter()  # <- cambio aquí

    while True:
        result = step_func()
        if result.get("swap"):
            swaps += 1
        if result.get("done"):
            break

    end_time = time.perf_counter()  # <- y aquí
    return swaps, end_time - start_time

if __name__ == "__main__":
    num_barras = 60  # más grande para que se note el tiempo
    max_val = 1000
    data = [random.randint(1, max_val) for _ in range(num_barras)]

    # Bubble Sort
    bubble_swaps, bubble_time = run_algorithm(init_bubble, step_bubble, data)
    print(f"Bubble Sort - Swaps: {bubble_swaps}, Tiempo: {bubble_time:.6f} s")

    # Insertion Sort
    insertion_swaps, insertion_time = run_algorithm(init_insertion, step_insertion, data)
    print(f"Insertion Sort - Swaps: {insertion_swaps}, Tiempo: {insertion_time:.6f} s")

    # Selection Sort
    selection_swaps, selection_time = run_algorithm(init_selection, step_selection, data)
    print(f"Selection Sort - Swaps: {selection_swaps}, Tiempo: {selection_time:.6f} s")

