import pandas as pd

films = pd.read_csv('film.csv', sep=';', encoding = "ISO-8859-1")

#print(films.head())

# Kasujemy pierwszy wiersz
films = films.drop(0)

# Kasujemy ostatnią kolumnę
films = films.drop(columns=['*Image'])

# print(films.head())

print(films.dtypes)

films.Length = pd.to_numeric(films.Length)
print(films.Length.mean())


def zamien(wartosc):
    if wartosc == 'No': return False
    if wartosc == 'Yes': return True


films.Awards = films.Awards.apply(zamien)
print(films.dtypes)