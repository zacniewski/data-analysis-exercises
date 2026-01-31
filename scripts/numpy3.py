import numpy as np

# Tworzenie tablic do demonstracji operacji matematycznych
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("--- Operacje arytmetyczne (wykonywane element po elemencie) ---")
# Dodawanie tablic
print(f"Dodawanie: {arr1 + arr2 = }")

# Odejmowanie tablic
print(f"Odejmowanie: {arr1 - arr2 = }")

# Mnożenie tablic (to nie jest mnożenie macierzowe, lecz mnożenie odpowiadających sobie elementów)
print(f"Mnożenie: {arr1 * arr2 = }")

# Dzielenie tablic
print(f"Dzielenie: {arr1 / arr2 = }")

# Potęgowanie elementów
print(f"Potęgowanie (arr2^2): {arr2 ** 2 = }")

print("\n--- Funkcje statystyczne i agregujące ---")
data = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Tablica testowa:\n{data}")

# Suma wszystkich elementów
print(f"Suma wszystkich elementów: {np.sum(data)}")

# Średnia wartość
print(f"Średnia: {np.mean(data)}")

# Sumowanie wzdłuż kolumn (axis=0)
print(f"Suma w kolumnach (axis=0): {data.sum(axis=0)}")

# Sumowanie wzdłuż wierszy (axis=1)
print(f"Suma w wierszach (axis=1): {data.sum(axis=1)}")

# Wartość minimalna i maksymalna
print(f"Minimum: {data.min()}, Maksimum: {data.max()}")

# Zapisujemy wyniki do pliku z Nazwiskiem
with open("scripts/Nazwisko_numpy3.txt", "w") as f:
    f.write(f"Suma: {np.sum(data)}\n")
    f.write(f"Srednia: {np.mean(data)}\n")
