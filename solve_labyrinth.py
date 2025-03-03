from sympy import mod_inverse

# Función para descifrar un valor
def decrypt(c, a_inv):
    return (c * a_inv) % 101

# Función para encontrar la ruta óptima
def find_optimal_path(grid):
    from heapq import heappush, heappop

    # Tamaño de la matriz
    size = len(grid)

    # Cola de prioridad: (xor_acumulado, x, y, ruta)
    heap = [(grid[0][0], 0, 0, [])]
    visited = set()

    while heap:
        xor, x, y, path = heappop(heap)

        # Si llegamos a la esquina inferior derecha
        if x == size - 1 and y == size - 1:
            return path

        # Si ya visitamos esta celda, la ignoramos
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Moverse hacia abajo (S)
        if x + 1 < size:
            new_xor = xor ^ grid[x + 1][y]
            heappush(heap, (new_xor, x + 1, y, path + ['S']))

        # Moverse hacia la derecha (D)
        if y + 1 < size:
            new_xor = xor ^ grid[x][y + 1]
            heappush(heap, (new_xor, x, y + 1, path + ['D']))

    return None

# Función principal
def main():
    print("Pega la matriz (10x10) aquí. Deja una línea en blanco para terminar:")
    grid = []
    for _ in range(10):
        line = input().strip()
        if not line:
            break
        # Si la línea comienza con "Pa", ignorar "Pa" y tomar los siguientes 10 valores
        if line.startswith("Pa"):
            row = [int(cell) for cell in line.split()[1:11]]  # Tomar los siguientes 10 valores
        else:
            row = [int(cell) for cell in line.split()[:10]]  # Tomar los primeros 10 valores
        grid.append(row)

    # Verificar el tamaño de la matriz
    if len(grid) != 10 or any(len(row) != 10 for row in grid):
        print("Error: La matriz no tiene el tamaño esperado (10x10).")
        print(f"Matriz obtenida: {len(grid)}x{len(grid[0]) if grid else 0}")
        return

    # Descifrar la matriz
    a = 7  # Asumimos que a = 7 (basado en el valor en (0, 1))
    a_inv = mod_inverse(a, 101)
    decrypted_grid = [[decrypt(c, a_inv) for c in row] for row in grid]

    print("\nMatriz descifrada:")
    for row in decrypted_grid:
        print(row)

    # Encontrar la ruta óptima
    path = find_optimal_path(decrypted_grid)
    if path:
        print("\nRuta óptima:", path)
    else:
        print("\nNo se encontró una ruta óptima.")

# Ejecutar el script
if __name__ == "__main__":
    main()