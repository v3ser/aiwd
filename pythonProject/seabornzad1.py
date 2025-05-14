import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Pokemon.csv', index_col=0, encoding='latin')  # zamień na ścieżkę do swojego pliku

czy_nan = df[df["Type 2"].isnull()]
plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(data=czy_nan, x="Attack", y="Defense", hue="Stage", palette="viridis")
sns.move_legend(scatter, "upper left", bbox_to_anchor=(1, 1))
plt.title("Zależność ataku od obrony pokemonów o jednym typie dla 3 różnych ewolucji", fontsize=14)
plt.xlabel("Atak")
plt.ylabel("Obrona")
plt.tight_layout()
plt.show()
