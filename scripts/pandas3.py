import pandas as pd

miasta = pd.read_csv('data/worldcities.csv')

# print(miasta.info())
# print(miasta.population.describe())
# print(miasta.isnull().sum())

# sprawdzenie ilości duplikatów
# print(miasta.duplicated().sum())

print(miasta.country.unique())
