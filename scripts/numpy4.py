import numpy as np

# Przygotowanie tablicy 2D (macierzy 4x4)
matrix = np.arange(16).reshape(4, 4)
print("Oryginalna macierz 4x4:")
print(matrix)

print("\n--- Wycinanie (Slicing) ---")
# Wycinanie wierszy: wiersze od indeksu 1 do 2 (3 jest wykluczone)
print("Wiersze od 1 do 2:")
print(matrix[1:3])

# Wycinanie konkretnego elementu: wiersz 2, kolumna 3
print(f"Element w wierszu 2, kolumnie 3: {matrix[2, 3]}")

# Wycinanie kolumny: wszystkie wiersze (:), kolumna o indeksie 1
print("Druga kolumna (indeks 1):")
print(matrix[:, 1])

# Wycinanie pod-macierzy: wiersze 0-1 i kolumny 2-3
print("Pod-macierz (wiersze 0-1, kolumny 2-3):")
print(matrix[0:2, 2:4])

print("\n--- Indeksowanie logiczne (Boolean Indexing) ---")
# Tworzenie maski logicznej dla elementów większych niż 10
mask = matrix > 10
print("Maska logiczna (elementy > 10):")
print(mask)

# Wybieranie elementów spełniających warunek
filtered_elements = matrix[matrix > 10]
print(f"Elementy większe niż 10: {filtered_elements}")

# Zastępowanie wartości spełniających warunek
matrix_copy = matrix.copy()
matrix_copy[matrix_copy % 2 == 0] = -1
print("Macierz po zastąpieniu liczb parzystych wartością -1:")
print(matrix_copy)

# Zapisanie macierzy kopii do pliku z Nazwiskiem
np.save("scripts/Nazwisko_numpy4.npy", matrix_copy)
