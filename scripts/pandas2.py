import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scripts\Countries.csv')

print(df.describe())
# print(df.head())
# print(df.tail())

# print(df[['Country', 'Population']])
# print(df.iloc[0:3, 2:4])
# print(df.loc[0:3, ['Country', 'Region', 'GDP']])

df_pop = df[['Country', 'Region', 'Population', 'Phones per 1000']].copy()
# print(df_pop)
# print(df_pop.describe())

df_pop['Population'] /= 1_000_000
# print(df_pop['Population'])

df_pop['Nowa kolumna'] = 1
# print(df_pop.head())


df_pop = df_pop.rename(columns={"Nowa kolumna": "Inna Nazwa"})
# print(df_pop.head())

'''
for index, row in df_pop.iterrows():
    if row['Population'] > 100:
        df_pop.loc[index, 'Size'] = 'Big'
        print(row['Country'], df_pop.loc[index, 'Size'])
'''
# print(df_pop.shape)
# print(df_pop.iloc[15:20, 1:6])

"""
for row in df_pop.itertuples():
    if row.Population > 200:
        print(row.Index, row.Country, row.Population)
"""
# print(df_pop[df_pop.Population == 147.365352])
# print(df_pop[df_pop['Population'] == 147.365352])

# print(df_pop[(df_pop['Population'] > 100) & (df_pop['Population'] < 150)])

print(df_pop['Population'].sum())
print(df_pop['Population'].max())
print(df_pop['Population'].min())
print(df_pop['Population'].mean())

# print(df_pop[df_pop['Population'] == 147.365352])
# print(df_pop.iloc[22:24, 0:6])

# print(df_pop[df_pop['Region'].strip() == 'NORTHERN AMERICA'])
'''
for index, row in df_pop.iterrows():
    if row['Region'].strip() == 'NORTHERN AMERICA':
        print(row['Country'], df_pop.loc[index, 'Population'])
'''

'''
print("\n\nRozmiar:\n")
print(df_pop.groupby('Region')['Population'].size())

print("\n\nSuma: \n")
print(df_pop.groupby('Region')['Population'].sum())

print("\n\nMinimum:\n")
print(df_pop.groupby('Region')['Population'].min())

print("\n\nMaximum: \n")
print(df_pop.groupby('Region')['Population'].max())
'''

'''
print("\n\nŚrednia:\n")
print(df_pop.groupby('Region')['Population'].mean())
'''
df_pop.to_json("df_pop.json")

print(df_pop.groupby('Region')['Population'].agg([min, max, sum, 'mean', 'size']) )
df_pop.groupby('Region')['Population'].sum().plot(kind='pie')
plt.show()