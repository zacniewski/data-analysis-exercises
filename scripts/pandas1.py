import pandas as pd


a = pd.Series([-1, 1, 3, 5, 7])
a.index = ["Pierwsza", "Druga", "Trzecia", "Czwarta", "Piąta"]

print(a)
print(a.describe())

b = [["Ania", 24], ["Michał", 9], ["Darek", 40], ["Ewa", 43]]
df_b = pd.DataFrame(b)
df_b.columns = "Imię", "Wiek"
print(df_b)

c = {
    "Imię": ["Ewa", "Michał", "Krzysiek", "Kasia", "Lucja"],
    "Miasto": ["Warszawa", "Kraków", "Gdańsk", "Poznań", "Łódź"],
}
df_c = pd.DataFrame(c)
print(df_c)

# Merge
# print(pd.merge(df_b, df_c, on='Imię'))

# left Join
# print(pd.merge(df_b, df_c, on='Imię', how='left'))

# right join
# print(pd.merge(df_b, df_c, on='Imię', how='right'))

# outer join
print(pd.merge(df_b, df_c, on='Imię', how='outer'))
