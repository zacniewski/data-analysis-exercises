# Inne biblioteki

W projekcie wykorzystywane są również biblioteki do pobierania i przetwarzania danych z internetu.

## Requests
Biblioteka służąca do wykonywania zapytań HTTP w sposób prosty i czytelny dla człowieka.

### Przykład
```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
# print(response.json())
```

## BeautifulSoup4
Biblioteka do wyciągania danych z plików HTML i XML (Web Scraping).

### Przykład
```python
from bs4 import BeautifulSoup

html_doc = "<html><head><title>Test</title></head><body><p>Witaj!</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)
```

## Dokumentacja
- [Requests Documentation](https://requests.readthedocs.io/)
- [BeautifulSoup4 Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
