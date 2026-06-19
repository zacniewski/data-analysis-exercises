# Wykład 5: Praca z formatami Excel i JSON

W analizie danych rzadko ograniczamy się do plików CSV. Często musimy współpracować z biznesem (Excel) lub systemami IT (JSON/API).

## 1. Excel w Pythonie

Pliki Excel (.xlsx) mają złożoną strukturę (wiele arkuszy, formatowanie, formuły). Do ich obsługi najczęściej używamy dwóch bibliotek:

### openpyxl
Służy do niskopoziomowej manipulacji plikami Excel. Pozwala na:
- Tworzenie nowych arkuszy.
- Edycję konkretnych komórek.
- Dodawanie styli i wykresów bezpośrednio do pliku Excel.

```python
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws['A1'] = "Dane"
wb.save("wynik.xlsx")
```

### Pandas (read_excel / to_excel)
Najszybszy sposób na wczytanie danych z Excela do DataFrame.
```python
import pandas as pd
df = pd.read_excel('dane.xlsx', sheet_name='Arkusz1')
```

## 2. JSON i API

JSON (JavaScript Object Notation) to standard wymiany danych w internecie. Jest lekki i czytelny dla ludzi.

### Struktura JSON
Przypomina słowniki (dict) i listy (list) w Pythonie.
```json
{
  "uzytkownik": "Jan",
  "zainteresowania": ["python", "data science"]
}
```

### Biblioteka requests
Służy do pobierania danych z API (Application Programming Interface).

```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json() # Konwersja JSON na słownik Pythona
```

## 3. Dlaczego warto znać te formaty?
1. **Automatyzacja raportów**: Możesz generować setki plików Excel w sekundy.
2. **Dane w czasie rzeczywistym**: API pozwala na pobieranie aktualnych kursów walut, pogody czy danych giełdowych.
3. **Integracja**: JSON jest mostem między Pythonem a innymi technologiami (web, mobile).
