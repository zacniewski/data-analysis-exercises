# Importujemy klasę Workbook oraz klasy do tworzenia wykresów.
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

# Tworzymy nowy skoroszyt.
wb = Workbook()
ws = wb.active
ws.title = "Wykresy"

# 1. Przygotowanie danych do wykresu.
# Nagłówki i dane sprzedaży.
rows = [
    ("Miesiąc", "Sprzedaż"),
    ("Styczeń", 1500),
    ("Luty", 2300),
    ("Marzec", 1800),
    ("Kwiecień", 2100),
    ("Maj", 2500)
]

# Dodajemy dane do arkusza.
for row in rows:
    ws.append(row)

# 2. Tworzenie wykresu słupkowego (BarChart).
chart = BarChart()
chart.type = "col" # Wykres kolumnowy
chart.style = 10    # Predefiniowany styl wykresu
chart.title = "Wyniki sprzedaży w I półroczu"
chart.y_axis.title = "Wartość (PLN)"
chart.x_axis.title = "Miesiąc"

# 3. Definiowanie zakresu danych dla wykresu.
# Dane znajdują się w kolumnie 2 (Sprzedaż), od wiersza 2 do 6.
data = Reference(ws, min_col=2, min_row=1, max_row=6, max_col=2)
# Kategorie (osie X) znajdują się w kolumnie 1, od wiersza 2 do 6.
cats = Reference(ws, min_col=1, min_row=2, max_row=6)

# Dodajemy dane i kategorie do wykresu.
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

# 4. Dodanie wykresu do arkusza.
# Wykres zostanie umieszczony z lewym górnym rogiem w komórce D2.
ws.add_chart(chart, "D2")

# Zapisujemy skoroszyt.
wb.save("scripts/Nazwisko_excel4.xlsx")
