# Matplotlib - Visualization with Python

Matplotlib to wszechstronna biblioteka do tworzenia statycznych, animowanych i interaktywnych wizualizacji w Pythonie.

## Możliwości
- Tworzenie wykresów liniowych, słupkowych, kołowych, histogramów itp.
- Pełna kontrola nad stylami, osiami i etykietami.
- Eksport wykresów do różnych formatów (PNG, PDF, SVG).

## Przykłady użycia

### Prosty wykres liniowy
```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, label='Wyniki')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Przykładowy Wykres')
plt.legend()
plt.show()
```

### Wykres słupkowy
```python
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C']
values = [5, 12, 8]

plt.bar(categories, values)
plt.show()
```

## Przypadki użycia
- Prezentacja wyników analizy danych.
- Monitorowanie procesów w czasie rzeczywistym.
- Tworzenie publikacji naukowych i raportów biznesowych.

## Dokumentacja
[Oficjalna dokumentacja Matplotlib](https://matplotlib.org/stable/index.html)
