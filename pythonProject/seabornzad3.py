import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')

df['Legendary'] = df['Legendary'].replace({False: 'Zwykły', True: 'Legendarny'})


procent = df['Legendary'].value_counts()


kolory = sns.color_palette("pastel")[0:2]

plt.figure(figsize=(6, 6))
plt.pie(procent, labels=procent.index, autopct='%1.f%%', colors=kolory)


plt.title('Procent legendarnych pokemonów')

plt.tight_layout()
plt.show()
