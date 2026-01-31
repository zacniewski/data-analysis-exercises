import matplotlib.pyplot as plt
import numpy as np

# Przygotowanie danych do różnych typów wykresów
kategorie = ['A', 'B', 'C', 'D', 'E']
wartosci = [23, 45, 12, 67, 34]
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Tworzymy nową figurę z trzema podwykresami w jednym rzędzie
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# 1. Wykres słupkowy (Bar chart)
# Pokazuje porównanie wartości w różnych kategoriach
ax1.bar(kategorie, wartosci, color='skyblue', edgecolor='navy')
ax1.set_title('Wykres słupkowy')
ax1.set_xlabel('Kategorie')
ax1.set_ylabel('Wartości')

# 2. Wykres punktowy (Scatter plot) z kolorami i rozmiarami
# Pokazuje korelacje między zmiennymi oraz dodatkowe wymiary za pomocą koloru i wielkości punktu
scatter = ax2.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.5, cmap='viridis')
ax2.set_title('Wykres punktowy (Scatter)')
ax2.set_xlabel('Oś X')
ax2.set_ylabel('Oś Y')
# Dodanie paska kolorów (colorbar) dla wykresu punktowego
fig.colorbar(scatter, ax=ax2, label='Intensywność')

# 3. Wykres kołowy (Pie chart)
# Pokazuje udział procentowy poszczególnych elementów w całości
ax3.pie(wartosci, labels=kategorie, autopct='%1.1f%%', startangle=140, explode=(0, 0.1, 0, 0, 0), shadow=True)
ax3.set_title('Wykres kołowy')

# Dodanie głównego tytułu dla całej figury
plt.suptitle('Możliwości Matplotlib: Różne typy wykresów 2D', fontsize=16)

# Automatyczne dostosowanie układu, aby elementy na siebie nie nachodziły
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Zapisanie wykresu do pliku
plt.savefig("scripts/Nazwisko_plot3.png")

# Wyświetlenie okna z wykresami
plt.show()
