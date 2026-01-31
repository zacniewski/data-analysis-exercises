import numpy as np

print("--- Zmiana kształtu (Reshaping) ---")
# Tworzymy tablicę 12-elementową
arr = np.arange(12)
print(f"Oryginalna tablica (1D): {arr}")

# Zmiana kształtu na 3x4
reshaped_3x4 = arr.reshape(3, 4)
print("Zmiana na 3x4:")
print(reshaped_3x4)

# Zmiana kształtu na 2x2x3 (3D)
reshaped_3d = arr.reshape(2, 2, 3)
print("Zmiana na 2x2x3 (3D):")
print(reshaped_3d)

print("\n--- Mechanizm Broadcastingu (Rozgłaszania) ---")
# Broadcasting pozwala na operacje między tablicami o różnych kształtach
# NumPy automatycznie "rozciąga" mniejszą tablicę tak, by pasowała do większej
matrix = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
print(f"Macierz:\n{matrix}")
print(f"Skalar: {scalar}")
# Skalar 10 zostanie dodany do każdego elementu macierzy
print(f"Macierz + skalar:\n{matrix + scalar}")

row_vector = np.array([100, 200, 300])
# Wiersz [100, 200, 300] zostanie dodany do każdego wiersza macierzy
print(f"Dodanie wektora wierszowego {row_vector} do macierzy:")
print(matrix + row_vector)

print("\n--- Łączenie tablic (Concatenation) ---")
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# Łączenie w pionie (axis=0)
concat_v = np.concatenate((a, b), axis=0)
print("Połączenie pionowe (concatenate axis=0):")
print(concat_v)

# Łączenie w poziomie (axis=1) - b musi być odpowiedniego kształtu (transpozycja)
b_transposed = b.T # Zmiana [5,6] (1x2) na [[5],[6]] (2x1)
concat_h = np.concatenate((a, b_transposed), axis=1)
print("Połączenie poziome (concatenate axis=1):")
print(concat_h)

# Zapisanie wyniku łączenia do pliku z Nazwiskiem
np.savez("scripts/Nazwisko_numpy5.npz", pionowo=concat_v, poziomo=concat_h)
