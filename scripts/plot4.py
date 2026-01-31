import matplotlib.pyplot as plt
import numpy as np

# Generowanie danych do wykresu liniowego
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 0.5 * np.cos(x)

# Tworzenie obiektu figury i osi
fig, ax1 = plt.subplots(figsize=(10, 6))

# 1. Wypełnianie obszaru między liniami (fill_between)
# Metoda ta pozwala na wizualizację zakresów lub niepewności
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='green', alpha=0.3, label='Sin > Cos')
ax1.fill_between(x, y1, y2, where=(y1 <= y2), color='red', alpha=0.3, label='Cos > Sin')

# Rysowanie głównych linii
ax1.plot(x, y1, color='blue', label='Sinus (x)')
ax1.set_xlabel('Czas / Odległość')
ax1.set_ylabel('Amplituda Sinusa', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# 2. Druga oś Y (twinx)
# Pozwala na nałożenie dwóch różnych skal na jeden wykres
ax2 = ax1.twinx()
y3 = np.exp(x / 3)
ax2.plot(x, y3, color='black', linestyle='--', label='Eksponenta')
ax2.set_ylabel('Wartość Eksponenty', color='black')

# 3. Adnotacje (annotate)
# Dodawanie opisów w konkretnych punktach wykresu ze strzałkami
max_idx = np.argmax(y1)
ax1.annotate('Maksimum lokalne', 
             xy=(x[max_idx], y1[max_idx]), 
             xytext=(x[max_idx]+1, y1[max_idx]+0.5),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)

# 4. Legenda dla obu osi
# Musimy pobrać uchwyty i etykiety z obu osi, aby połączyć je w jednej legendzie
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Tytuł i siatka
plt.title('Zaawansowane techniki: Fill_between, Twinx i Annotate')
ax1.grid(True, linestyle=':', alpha=0.6)

# Zapis i wyświetlenie
plt.savefig("scripts/Nazwisko_plot4.png")
plt.show()
