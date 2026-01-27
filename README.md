# Ćwiczenia z obróbki i analizy danych

Repozytorium zawierające ćwiczenia, skrypty i materiały do nauki obróbki oraz analizy danych w języku Python.

## Spis treści
1. [Struktura projektu](#struktura-projektu)
2. [Instalacja i konfiguracja](#instalacja-i-konfiguracja)
3. [Zawartość](#zawartość)
4. [Przydatne linki](#przydatne-linki)

## Struktura projektu
- `data/` - zbiory danych w formatach CSV i XLSX.
- `images/` - pliki graficzne.
- `notebooks/` - interaktywne notatniki Jupyter Notebook.
- `scripts/` - skrypty Python (scraping, pandas, numpy).
- `tasks/` - zestawy zadań do samodzielnego wykonania.
- `requirements.txt` - lista wymaganych bibliotek.

## Instalacja i konfiguracja

### Środowisko wirtualne
Zaleca się korzystanie ze środowiska wirtualnego.

```shell
# Tworzenie środowiska wirtualnego
python -m venv my_env

# Aktywacja (Windows)
my_env\Scripts\activate

# lub (Windows
cd my_env
cd Scripts
activate
cd ..
cd ..

# Aktywacja (Linux/macOS)
source my_env/bin/activate

# Instalacja zależności
pip install -r requirements.txt
```

## Zawartość
- **Scraping**: Skrypty do pobierania danych ze stron internetowych (`scripts/scraping*.py`).
- **Pandas**: Przykłady obróbki danych przy użyciu biblioteki Pandas (`scripts/pandas*.py`).
- **NumPy**: Podstawowe operacje na tablicach (`scripts/numpy*.py`).
- **Wizualizacja**: Skrypty generujące wykresy (`scripts/plot*.py`).

## Przydatne linki
- [Hands-On Data Preprocessing in Python](https://github.com/PacktPublishing/Hands-On-Data-Preprocessing-in-Python/tree/main) - kod źródłowy do książki.
- [Analityk.edu.pl](https://www.youtube.com/@Analitykedupl/videos) - kanał YT oraz ich [repozytorium](https://github.com/AnalitykEduPL/Najwazniejsze-biblioteki-Python/tree/master).
- [Python Pandas Mega Tutorial](https://analityk.edu.pl/python-pandas-mega-tutorial/) - świetne źródło wiedzy o Pandas.
- [Kaggle Learn](https://www.kaggle.com/learn) - kursy z zakresu Data Science.
- **Dokumentacja (startery)**:
    - [NumPy Beginner's Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
    - [Matplotlib Quick Start](https://matplotlib.org/stable/users/explain/quick_start.html)
    - [Web Scraping Tutorial](https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/)

