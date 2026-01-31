import pandas as pd

# Wczytywanie bazy miast świata
miasta = pd.read_csv('data/worldcities.csv')

# Wyświetlanie podstawowych informacji o strukturze danych (liczba kolumn, typy danych, brakujące wartości)
print("Informacje o DataFrame:")
miasta.info()

# Statystyki dla kolumny populacja
print("\nStatystyki populacji:")
print(miasta.population.describe())

# Sprawdzenie liczby brakujących wartości (null) w każdej kolumnie
print("\nLiczba brakujących wartości w kolumnach:")
print(miasta.isnull().sum())

# Sprawdzenie ilości duplikatów w całym zbiorze danych
print(f"\nLiczba duplikowanych wierszy: {miasta.duplicated().sum()}")

# Wyświetlenie unikalnych wartości dla kolumny 'country'
print("\nLista unikalnych państw w zbiorze:")
print(miasta.country.unique())

# Zapisanie unikalnych państw do pliku z Nazwiskiem
pd.Series(miasta.country.unique()).to_csv("scripts/Nazwisko_pandas3.csv", index=False)
