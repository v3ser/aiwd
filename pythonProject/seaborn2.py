import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')
print(df.head(4))
zgrupowane = df.groupby("Type 1")["Defense"].mean()
print(zgrupowane)
df["Średnia obrona wg. Typu 1"] = df["Type 1"].map(zgrupowane)
print(df)
df['Ulubiony'] = df.apply(lambda row: 'Tak' if 'Rock' in [row['Type 1'], row['Type 2']] else 'Nie', axis=1)
df['Dwa typy'] = df['Type 1'] + '-' + df['Type 2'].fillna('')
print(df[['Name','Type 1', 'Type 2', 'Total', 'HP', 'Dwa typy']].head(4))
print(f"Liczba wierszy w zbiorze danych {len(df)}")
bez_legendarnych = df[df["Legendary"] == False]
print(f"Liczba wierszy w zbiorze danych po usunięciu legendarnych {len(zgrupowane)}")
bez_typu2 = df[df["Type 2"].isna()]
print(f"Liczba pokemonow ktore nie maja typu 2 \n {bez_typu2}")
bez_typu2.to_csv('modified_pokemon.csv', index=False)
plt.figure(figsize=(14, 10))
plt.suptitle("Analiza statystyk pokemonów regionu Kanto", fontsize= 14)
#Wykres 1
plt.subplot(2,2,1)
srednia_atak_obrona = df[["Attack","Defense"]].mean()
plt.bar(srednia_atak_obrona.index,srednia_atak_obrona.values, color=['orange', 'blue'])
plt.title('Średnie wartości ataku i obrony', fontsize=14)
plt.ylabel('Średnia')
plt.xticks([0, 1], ['Attack', 'Defense'], rotation=0)
#Wykres 2
plt.subplot(2,2,2)
procentowy_rozklad = df["Type 1"].value_counts()
plt.pie(procentowy_rozklad, autopct='%1.1f%%', pctdistance=1.1)
plt.title('Procentowy rozkład pokemonow danego typu', fontsize=14)
plt.legend(procentowy_rozklad.index, loc="center right",bbox_to_anchor=(1.4, 0.5))
plt.show()
#Wykres 3
plt.subplot(2,2,3)