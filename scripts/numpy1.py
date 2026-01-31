import numpy as np

# Tworzenie tablicy jednowymiarowej bezpośrednio z listy
# np.array() konwertuje listę Pythona na obiekt ndarray
a = np.array([1, 3, 5, 7])
print(f"{a=}")

# Tworzenie tablicy o określonym zakresie wartości (od 0 do 3)
# np.arange(n) działa podobnie do range(), zwracając tablicę od 0 do n-1
b = np.arange(4)
print(f"{b=}")

# Tworzenie tablicy z określonym początkiem, końcem i krokiem
# np.arange(start, stop, step) - generuje wartości od 2 do 9 z krokiem 1
numpy_arange = np.arange(2, 10, 1)
print(f"{numpy_arange=}")

# Tworzenie tablicy z liniowo rozłożonymi wartościami
# np.linspace(start, stop, num) - generuje 'num' równomiernie rozłożonych punktów w przedziale [start, stop]
numpy_linspace = np.linspace(0, 10, 6)
print(f"{numpy_linspace=}")

# Zapisujemy tablicę do pliku z Nazwiskiem
np.savetxt("scripts/Nazwisko_numpy1.txt", numpy_linspace)

