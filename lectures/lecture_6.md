# Wykład 6: Zaawansowany Web Scraping

Web Scraping to technika pobierania danych bezpośrednio ze stron internetowych poprzez analizę ich kodu HTML.

## 1. Struktura dokumentu HTML
Każda strona to drzewo znaczników (tags). Kluczowe dla nas to:
- `<div>`, `<span>`: kontenery na dane.
- `<a>`: linki (atrybut `href`).
- `<table>`, `<tr>`, `<td>`: dane tabelaryczne.
- `class`, `id`: atrybuty pozwalające precyzyjnie namierzyć element.

## 2. Biblioteka BeautifulSoup
Pozwala "przeszukiwać" pobrany kod HTML.

```python
from bs4 import BeautifulSoup
import requests

res = requests.get("https://example.com")
soup = BeautifulSoup(res.text, 'html.parser')

# Znajdź wszystkie nagłówki h2
headers = soup.find_all('h2')
for h in headers:
    print(h.text)
```

## 3. Wyzwania w Scrapingu
1. **Dynamiczna zawartość**: Jeśli strona ładuje dane przez JavaScript, `requests` ich nie zobaczy (rozwiązanie: Selenium/Playwright).
2. **Blokady**: Serwery mogą blokować boty (rozwiązanie: User-Agent headers, opóźnienia, proxy).
3. **Prawo i etyka**: Zawsze sprawdzaj plik `robots.txt` danej domeny.

## 4. Przetwarzanie pobranych danych
Dane ze scrapingu są zazwyczaj "brudne" (zawierają białe znaki, tagi HTML). 
- Używamy metod `.strip()`, `.replace()`.
- Wyniki zapisujemy do CSV, Excela lub wprost do DataFrame w Pandas.
