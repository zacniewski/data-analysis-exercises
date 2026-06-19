# Obróbka i Analiza Danych - Teoria i Praktyka

Repozytorium stanowi kompleksowy kurs do przedmiotu "Obróbka i analiza danych". Obejmuje 8 godzin wykładów oraz 15 godzin laboratoriów.

## 📚 Program Kursu

### Wykłady (8h)
1. **[Wykład 1: Wprowadzenie i NumPy](lectures/lecture_1.md)** - Podstawy analizy, środowisko pracy i fundament obliczeniowy.
2. **[Wykład 2: Pozyskiwanie danych](lectures/lecture_2.md)** - Formaty plików, API oraz Web Scraping.
3. **[Wykład 3: Przetwarzanie w Pandas](lectures/lecture_3.md)** - EDA, czyszczenie i transformacje danych.
4. **[Wykład 4: Wizualizacja](lectures/lecture_4.md)** - Komunikacja wyników i dobre praktyki prezentacji danych.
5. **[Wykład 5: Excel i JSON](lectures/lecture_5.md)** - Praca z arkuszami kalkulacyjnymi i API.
6. **[Wykład 6: Web Scraping](lectures/lecture_6.md)** - Zaawansowane techniki pobierania danych z WWW.
7. **[Wykład 7: Szeregi czasowe](lectures/lecture_7.md)** - Analiza danych w czasie.
8. **[Wykład 8: Podsumowanie](lectures/lecture_8.md)** - Dobre praktyki i cykl życia projektu.

### Laboratoria (15h)
1. **[Lab 1: Fundamenty](labs/lab_1.md)** - Konfiguracja i NumPy.
2. **[Lab 2: Dane z WWW](labs/lab_2.md)** - Scraping i praca z plikami CSV/JSON/Excel.
3. **[Lab 3: Eksploracja](labs/lab_3.md)** - Podstawy Pandas i analiza EDA.
4. **[Lab 4: Transformacje](labs/lab_4.md)** - Czyszczenie danych i agregacje.
5. **[Lab 5: Wizualizacja](labs/lab_5.md)** - Wykresy w Matplotlib i Seaborn.
6. **[Lab 6: Excel](labs/lab_6.md)** - openpyxl i Pandas w arkuszach.
7. **[Lab 7: JSON & API](labs/lab_7.md)** - Integracja z usługami zewnętrznymi.
8. **[Lab 8: Scraper](labs/lab_8.md)** - Budowa własnego narzędzia do pozyskiwania danych.
9. **[Lab 9: Czas](labs/lab_9.md)** - Analiza szeregów czasowych.
10. **[Lab 10: Projekt](labs/lab_10.md)** - Kompleksowa analiza dużego zbioru danych.

---

## 🛠️ Struktura projektu
- `lectures/` - materiały teoretyczne (Markdown).
- `labs/` - instrukcje do zajęć laboratoryjnych.
- `data/` - zbiory danych do ćwiczeń.
- `scripts/` - gotowe przykłady w Pythonie.
- `docs/` - dokumentacja bibliotek.
- `notebooks/` - interaktywne notatniki.

## 🚀 Instalacja i konfiguracja

### Środowisko wirtualne
Zaleca się korzystanie ze środowiska wirtualnego.

```shell
# Tworzenie środowiska wirtualnego
# Można uzyć 'cmd' (zawsze działa) lub 'powershell' (czasem buntuje się w PyCharmie)
python -m venv my_env

# Aktywacja (Windows)
my_env\Scripts\activate

# lub (Windows)
cd my_env
cd Scripts
activate
cd ..
cd ..

# Nazwa środowiska wirtualnego (my_env w tym przypadku) powinna zostać wyświetlona w nawiasach okrągłych.

# Aktywacja (Linux/macOS)
source my_env/bin/activate

# Instalacja zależności
pip install -r requirements.txt  

# deaktywacja środowiska wirtualnego
deactivate
```

> Używając PyCharma do tworzenia nowego projektu, często zachodzi sytuacja, że PyCharm tworzy automatycznie środowisko wirtualne o nazwie `.venv` i je aktywuje.  
> Wtedy można, zamiast tworzyć środowisko wirtualne `my_env` skorzystać z już gotowego środowiska `.venv`  
> Można też (druga opcja) deaktywować środowisko `.venv` za pomocą komendy `deactivate` i utworzyć własne ww. środowisko.

## Uruchamianie skryptów

Aby uruchomić wybrany skrypt, należy użyć polecenia `python` (lub `python3` na systemach Linux/macOS) wraz ze ścieżką do pliku:

```shell
# jesteśmy w folderze z naszym projektem
# nie wchodzimy do folderu `scripts`
.
├── data
├── docs
├── images
├── my_env
├── notebooks
├── README.md
├── requirements.txt
├── scripts
└── tasks

# Przykład uruchomienia skryptu, który znajduje się w katalogu `scripts`
python scripts/pandas1.py
```

### Czego się spodziewać?
Po uruchomieniu skryptu możesz spodziewać się:
- Wyświetlenia danych lub wyników analizy bezpośrednio w konsoli.
- Utworzenia lub zaktualizowania plików w katalogu `data/` (w przypadku skryptów zapisujących dane). Każdy skrypt powinien wygenerować plik zawierający słowo **'Nazwisko'** w swojej nazwie.
- Wygenerowania wykresów w nowym oknie lub zapisania ich jako obrazy w katalogu `images/`.
- Wykonania operacji scrapingowych i pobrania danych ze stron internetowych.

## Zawartość
- **Scraping**: Skrypty do pobierania danych ze stron internetowych (`scripts/scraping*.py`).
- **Pandas**: Przykłady obróbki danych przy użyciu biblioteki Pandas (`scripts/pandas*.py`).
- **NumPy**: Podstawowe operacje na tablicach (`scripts/numpy*.py`).
- **Wizualizacja**: Skrypty generujące wykresy (`scripts/plot*.py`).

## Przydatne linki
- [Dokumentacja lokalna (Markdown)](docs/)
    - [NumPy](docs/numpy.md)
    - [Pandas](docs/pandas.md)
    - [Matplotlib](docs/matplotlib.md)
    - [Inne (Requests, BeautifulSoup)](docs/others.md)
- [Hands-On Data Preprocessing in Python](https://github.com/PacktPublishing/Hands-On-Data-Preprocessing-in-Python/tree/main) - kod źródłowy do książki.
- [Analityk.edu.pl](https://www.youtube.com/@Analitykedupl/videos) - kanał YT oraz ich [repozytorium](https://github.com/AnalitykEduPL/Najwazniejsze-biblioteki-Python/tree/master).
- [Python Pandas Mega Tutorial](https://analityk.edu.pl/python-pandas-mega-tutorial/) - świetne źródło wiedzy o Pandas.
- [Kaggle Learn](https://www.kaggle.com/learn) - kursy z zakresu Data Science.
- **Dokumentacja (startery)**:
    - [NumPy Beginner's Guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
    - [Matplotlib Quick Start](https://matplotlib.org/stable/users/explain/quick_start.html)
    - [Web Scraping Tutorial](https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/)

