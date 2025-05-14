import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')

przefiltrowany_df = df[df['Type 1'].isin(['Grass', 'Fire', 'Water'])]

liczba = przefiltrowany_df.groupby('Type 1')['Name'].count().reset_index()
liczba.columns = ['Type 1', 'Count']

pkmn_type_colors = ['#F08030','#78C850', '#6890F0']

plt.figure(figsize=(8, 6))
sns.barplot(data=liczba, x='Type 1',hue='Type 1', y='Count', palette=pkmn_type_colors, legend=False)

plt.title('Liczba pokemonów typu ognistego, trawiastego i wodnego', fontsize=14)
plt.xlabel('Typ pokemona')
plt.ylabel('Liczba')

plt.tight_layout()
plt.show()
