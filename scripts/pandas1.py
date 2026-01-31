import pandas as pd

# Tworzenie serii danych (Series) - jednowymiarowa tablica z etykietami
a = pd.Series([-1, 1, 3, 5, 7])
# Nadawanie własnych nazw indeksom
a.index = ["Pierwsza", "Druga", "Trzecia", "Czwarta", "Piąta"]

print("Seria danych 'a':")
print(a)
# Wyświetlenie podstawowych statystyk opisowych dla serii (liczba elementów, średnia, odchylenie std itp.)
print("\nStatystyki opisowe serii 'a':")
print(a.describe())

# Tworzenie ramki danych (DataFrame) z listy list
b = [["Ania", 24], ["Michał", 9], ["Darek", 40], ["Ewa", 43]]
df_b = pd.DataFrame(b)
# Nadanie nazw kolumnom
df_b.columns = ["Imię", "Wiek"]
print("\nRamka danych df_b (Imię i Wiek):")
print(df_b)

# Tworzenie ramki danych ze słownika
c = {
    "Imię": ["Ewa", "Michał", "Krzysiek", "Kasia", "Lucja"],
    "Miasto": ["Warszawa", "Kraków", "Gdańsk", "Poznań", "Łódź"],
}
df_c = pd.DataFrame(c)
print("\nRamka danych df_c (Imię i Miasto):")
print(df_c)

# Łączenie ramek danych (Merging)

# Merge (domyślnie 'inner' join) - bierze tylko te rekordy, których klucz (Imię) występuje w obu tabelach
print("\nMerge (Inner Join) - tylko części wspólne:")
print(pd.merge(df_b, df_c, on='Imię'))

# Left Join - wszystkie rekordy z lewej tabeli (df_b) i pasujące z prawej (df_c)
print("\nLeft Join - wszystkie z df_b + dopasowania z df_c:")
print(pd.merge(df_b, df_c, on='Imię', how='left'))

# Right Join - wszystkie rekordy z prawej tabeli (df_c) i pasujące z lewej (df_b)
print("\nRight Join - wszystkie z df_c + dopasowania z df_b:")
print(pd.merge(df_b, df_c, on='Imię', how='right'))

# Outer Join - wszystkie rekordy z obu tabel, uzupełnia brakujące dane wartościami NaN
print("\nOuter Join - suma wszystkich rekordów:")
df_outer = pd.merge(df_b, df_c, on='Imię', how='outer')
print(df_outer)

# Zapisanie wyniku połączenia do pliku z Nazwiskiem
df_outer.to_csv("scripts/Nazwisko_pandas1.csv", index=False)
