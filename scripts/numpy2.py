import numpy as np
import matplotlib.pyplot as plt

# Importowanie modułu io z biblioteki scikit-image do wczytywania obrazów
from skimage import io

# Wczytywanie obrazu z pliku lokalnego
# Funkcja io.imread zwraca obraz jako tablicę NumPy (ndarray)
# Każdy piksel jest reprezentowany przez wartości kolorów (np. RGB)
pic = np.array(io.imread('images/fire.jpeg'))

# Wyświetlanie obrazu przy użyciu biblioteki matplotlib
# plt.imshow potrafi interpretować tablice NumPy jako dane wizualne
plt.imshow(pic)

# Wyświetlenie okna z wykresem/obrazem
plt.show()

# Zapisanie obrazu do pliku z Nazwiskiem
io.imsave("scripts/Nazwisko_numpy2.png", pic)
