import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Importujemy toolkit do 3D (w nowszych wersjach Matplotlib nie jest to zawsze konieczne, 
# ale dobra praktyka przy jawnej definicji osi)
from mpl_toolkits.mplot3d import Axes3D

# Przygotowanie danych do wykresu powierzchniowego (Surface plot)
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Tworzenie figury
fig = plt.figure(figsize=(12, 8))

# 1. Wykres powierzchniowy (Surface plot)
# Używamy rzutowania 3D
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
# plot_surface tworzy kolorową powierzchnię
surf = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax1.set_title('Wykres powierzchniowy 3D')
# Dodanie paska kolorów
fig.colorbar(surf, shrink=0.5, aspect=5, ax=ax1)

# 2. Wykres liniowy 3D (3D Line plot) i punktowy (Scatter)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')

# Parametryczna linia spiralna
z_line = np.linspace(0, 15, 1000)
x_line = np.sin(z_line)
y_line = np.cos(z_line)
ax2.plot3D(x_line, y_line, z_line, 'gray', label='Spirala')

# Losowe punkty w przestrzeni 3D
z_scatter = 15 * np.random.random(100)
x_scatter = np.sin(z_scatter) + 0.1 * np.random.randn(100)
y_scatter = np.cos(z_scatter) + 0.1 * np.random.randn(100)
ax2.scatter3D(x_scatter, y_scatter, z_scatter, c=z_scatter, cmap='Greens', label='Punkty losowe')

ax2.set_title('Wykres liniowy i punktowy 3D')
ax2.legend()

# Dodanie opisów osi dla drugiego wykresu
ax2.set_xlabel('Oś X')
ax2.set_ylabel('Oś Y')
ax2.set_zlabel('Oś Z')

# Globalny tytuł
plt.suptitle('Możliwości Matplotlib: Wykresy Trójwymiarowe (3D)', fontsize=16)

# Zapisanie i wyświetlenie
plt.savefig("scripts/Nazwisko_plot5.png")
plt.show()
