import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
df = pd.read_csv('Pokemon.csv', encoding='latin1')

# Filtracja danych do regionu Kanto (przyjmujemy, że to pokemony, które mają Type 1 i Type 2, np. "Fire" / "Water")
df_kanto = df  # Zmieniamy to w razie potrzeby, jeśli mamy dane tylko z regionu Kanto.

# Ustawienie wielkości płótna
plt.figure(figsize=(14, 10))

# 1. Wykres słupkowy dla średnich wartości ataku i obrony
plt.subplot(2, 2, 1)
avg_attack_defense = df[['Attack', 'Defense']].mean()
avg_attack_defense.plot(kind='bar', color=['orange', 'blue'])
plt.title('Średni atak i obrona Pokémonów', fontsize=14)
plt.ylabel('Wartość statystyki')
plt.xticks([0, 1], ['Atak', 'Obrona'], rotation=0)

# 2. Wykres kołowy dla rozkładu Type 1
plt.subplot(2, 2, 2)
type1_distribution = df['Type 1'].value_counts()
colors = sns.color_palette("Set3", len(type1_distribution))  # Kolory dla typów
plt.pie(type1_distribution, labels=type1_distribution.index, autopct='%1.1f%%', pctdistance=0.85, colors=colors)
plt.title('Procentowy rozkład Pokémonów według Type 1', fontsize=14)
plt.legend(type1_distribution.index, bbox_to_anchor=(1.1, 0.5))

# 3. Wykres punktowy Sp. Def vs Sp. Atk dla trzech typów (Dragon, Normal, Fire)
plt.subplot(2, 2, 3)
sns.scatterplot(data=df[df['Type 1'].isin(['Dragon', 'Normal', 'Fire'])],
                x='Sp. Atk', y='Sp. Def', hue='Type 1', palette='deep')
plt.title('Sp. Def vs Sp. Atk dla typów: Dragon, Normal, Fire', fontsize=14)
plt.xlabel('Specjalny Atak (Sp. Atk)')
plt.ylabel('Specjalna Obrona (Sp. Def)')
plt.legend(title='Typ', loc='upper left')

# 4. Wykres boxplot dla prędkości Speed dla trzech typów (Dragon, Normal, Fire)
plt.subplot(2, 2, 4)
sns.boxplot(data=df[df['Type 1'].isin(['Dragon', 'Normal', 'Fire'])], x='Type 1', y='Speed', palette='deep')
plt.title('Rozkład prędkości (Speed) dla typów: Dragon, Normal, Fire', fontsize=14)
plt.xlabel('Typ')
plt.ylabel('Prędkość (Speed)')

# Nadanie tytułu płótnu
plt.suptitle('Analiza statystyk pokemonów regionu Kanto', fontsize=16)

# Dostosowanie wykresów
plt.tight_layout()
plt.subplots_adjust(top=0.9)  # Dostosowanie dla tytułu

# Zapisanie wykresu do pliku PNG
plt.savefig('pokemon_analysis_kanto.png')

# Wyświetlenie wykresu
plt.show()
