import pandas as pd
import matplotlib.pyplot as plt

# Wczytywanie danych z pliku CSV
# Używamy r'' (raw string) lub '/' dla ścieżek w Windows/Unix
df = pd.read_csv('data/Countries.csv')

# Wyświetlanie statystyk opisowych (średnia, min, max itp.) dla kolumn numerycznych
print("Podstawowe statystyki:")
print(df.describe())

# Wyświetlanie pierwszych 5 wierszy
print("\nPierwsze 5 wierszy (head):")
print(df.head())

# Wyświetlanie ostatnich 5 wierszy
print("\nOstatnie 5 wierszy (tail):")
print(df.tail())

# Wybieranie konkretnych kolumn
print("\nKolumny Country i Population:")
print(df[['Country', 'Population']])

# Wybieranie zakresu wierszy i kolumn za pomocą indeksów (iloc)
# [wiersze od:do, kolumny od:do]
print("\niloc[0:3, 2:4] - wiersze 0-2, kolumny 2-3:")
print(df.iloc[0:3, 2:4])

# Wybieranie danych za pomocą nazw etykiet (loc)
print("\nloc[0:3, ['Country', 'Region']] - wiersze o indeksach 0-3 i wybrane kolumny:")
print(df.loc[0:3, ['Country', 'Region', 'GDP']])

# Tworzenie kopii fragmentu ramki danych
df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()

# Operacje na kolumnach - zamiana jednostek (dzielenie populacji przez milion)
df_pop['Population'] /= 1_000_000

# Dodawanie nowej kolumny z domyślną wartością
df_pop['Nowa kolumna'] = 1

# Zmiana nazwy kolumny
df_pop = df_pop.rename(columns={"Nowa kolumna": "Inna Nazwa"})
print("\ndf_pop po zmianach (populacja w mln i nowa kolumna):")
print(df_pop.head())

# Iteracja po wierszach (iterrows) - dostęp do indeksu i wiersza
print("\nIteracja iterrows - kraje z populacją > 100 mln:")
for index, row in df_pop.iterrows():
    if row['Population'] > 100:
        df_pop.loc[index, 'Size'] = 'Big'
        print(f"Kraj: {row['Country']}, Rozmiar: {df_pop.loc[index, 'Size']}")

# Właściwości DataFrame
print(f"\nKształt tabeli (wiersze, kolumny): {df_pop.shape}")

# Iteracja za pomocą itertuples - szybsza alternatywa dla iterrows
print("\nIteracja itertuples - kraje z populacją > 200 mln:")
for row in df_pop.itertuples():
    if row.Population > 200:
        print(f"Index: {row.Index}, Kraj: {row.Country}, Populacja: {row.Population:.2f} mln")

# Filtrowanie danych
print("\nFiltrowanie - kraje z populacją dokładnie 147.365352 mln:")
print(df_pop[df_pop.Population == 147.365352])

print("\nFiltrowanie złożone - populacja między 100 a 150 mln:")
print(df_pop[(df_pop['Population'] > 100) & (df_pop['Population'] < 150)])

# Podstawowe agregacje
print("\nAgregacje dla całej kolumny Population [mln]:")
print(f"Suma: {df_pop['Population'].sum():.2f}")
print(f"Maksimum: {df_pop['Population'].max():.2f}")
print(f"Minimum: {df_pop['Population'].min():.2f}")
print(f"Średnia: {df_pop['Population'].mean():.2f}")

# Praca z tekstem - filtrowanie po regionie (użycie strip() do usunięcia spacji)
print("\nKraje w regionie NORTHERN AMERICA:")
for index, row in df_pop.iterrows():
    if row['Region'].strip() == 'NORTHERN AMERICA':
        print(f"{row['Country']}: {row['Population']:.2f} mln")

# Grupowanie danych (Group By) i wyliczanie statystyk dla regionów
print("\nStatystyki populacji pogrupowane według Regionu:")
print(df_pop.groupby('Region')['Population'].agg(['size', 'sum', 'min', 'max', 'mean']))

# Zapisywanie do formatu JSON
df_pop.to_json("scripts/Nazwisko_pandas2.json")
print("\nZapisano dane do pliku scripts/Nazwisko_pandas2.json")

# Wykres kołowy sumy populacji na region
df_pop.groupby('Region')['Population'].sum().plot(kind='pie', figsize=(10, 10))
plt.title("Suma populacji na region")
plt.ylabel('')  # Ukrycie etykiety osi Y
plt.show()