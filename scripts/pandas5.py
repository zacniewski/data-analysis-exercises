import pandas as pd

# Wczytywanie danych z pliku CSV z określonym separatorem i kodowaniem
films = pd.read_csv('data/film.csv', sep=';', encoding="ISO-8859-1")

print("Pierwsze 5 filmów przed czyszczeniem:")
print(films.head())

# Kasujemy pierwszy wiersz (często zawiera on błędne dane lub dodatkowe nagłówki)
films = films.drop(0)

# Kasujemy kolumnę '*Image', która nie jest potrzebna do analizy
films = films.drop(columns=['*Image'])

print("\nPierwsze 5 filmów po usunięciu niepotrzebnych danych:")
print(films.head())

# Sprawdzanie typów danych w kolumnach
print("\nTypy danych w kolumnach:")
print(films.dtypes)

# Konwersja kolumny 'Length' na typ numeryczny (z tekstu na liczbę)
films.Length = pd.to_numeric(films.Length)

# Obliczanie średniej długości filmu
print(f"\nŚrednia długość filmu: {films.Length.mean():.2f} minut")

# Funkcja konwertująca tekstowe 'Yes'/'No' na wartości logiczne True/False
def zamien(wartosc):
    if wartosc == 'No':
        return False
    if wartosc == 'Yes':
        return True
    return None

# Zastosowanie konwersji na kolumnie 'Awards'
films.Awards = films.Awards.apply(zamien)

print("\nTypy danych po konwersji Awards:")
print(films.dtypes)

# Dodatkowe ćwiczenie: Ile filmów zdobyło nagrody?
nagrodzone = films[films.Awards == True].shape[0]
print(f"\nLiczba filmów z nagrodami: {nagrodzone}")

# Zapisanie oczyszczonych danych do pliku z Nazwiskiem
films.to_csv("scripts/Nazwisko_pandas5.csv", index=False)