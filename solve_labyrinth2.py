import random
import heapq
from sympy import primerange

MOD = 101
SIZE = 10

def encrypt(n, a, b):
    return (a * n + b) % MOD

def decrypt(e, a, b):
    """Desencripta un valor usando el inverso modular de 'a' en Z_101."""
    a_inv = pow(a, -1, MOD)  # Inverso modular de 'a' mod 101
    return (a_inv * (e - b)) % MOD

def generate(size):
    """Genera una matriz 10x10 con valores entre 0 y 9, con (0,0) fijo en 0."""
    grid = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]
    grid[0][0] = 0
    return grid

def build_encrypted_grid(grid, a, b):
    """Cifra la matriz usando la función (a * n + b) % 101."""
    return [[encrypt(grid[y][x], a, b) for x in range(SIZE)] for y in range(SIZE)]

def decrypt_grid(enc_grid, a, b):
    """Descifra la matriz cifrada."""
    return [[decrypt(enc_grid[y][x], a, b) for x in range(SIZE)] for y in range(SIZE)]

def find_min_xor_path(grid):
    """Usa Dijkstra para encontrar el camino con menor XOR acumulado."""
    pq = [(0, 0, 0)]  # (XOR acumulado, fila, columna)
    best_xor = {(0, 0): 0}
    
    while pq:
        curr_xor, y, x = heapq.heappop(pq)
        
        if (y, x) == (SIZE - 1, SIZE - 1):
            return curr_xor  # Retorna el menor XOR al final

        for dy, dx in [(1, 0), (0, 1)]:  # Solo mover abajo o derecha
            ny, nx = y + dy, x + dx
            if 0 <= ny < SIZE and 0 <= nx < SIZE:
                new_xor = curr_xor ^ grid[ny][nx]
                if (ny, nx) not in best_xor or new_xor < best_xor[(ny, nx)]:
                    best_xor[(ny, nx)] = new_xor
                    heapq.heappush(pq, (new_xor, ny, nx))

# Ejemplo de generación y resolución
random.seed(42)  # Para reproducibilidad

# Generamos la matriz original y la ciframos
original_grid = generate(SIZE)
a = random.choice(list(primerange(2, 12)))
b = random.randint(0, 100)
encrypted_grid = build_encrypted_grid(original_grid, a, b)

# Desciframos la matriz
decrypted_grid = decrypt_grid(encrypted_grid, a, b)

# Buscamos el camino óptimo
min_xor = find_min_xor_path(decrypted_grid)

print("Matriz Original:")
for row in original_grid:
    print(row)

print("\nMatriz Cifrada:")
for row in encrypted_grid:
    print(row)

print("\nMatriz Descifrada:")
for row in decrypted_grid:
    print(row)

print("\nMínimo XOR posible:", min_xor)
