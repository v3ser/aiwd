import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Tworzenie figury i osi 3D
fig = plt.figure(figsize=(15, 12))
ax = fig.add_subplot(111, projection='3d')

# Generowanie danych
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Lista wybranych kolorystyk
colormaps = ['viridis', 'coolwarm', 'plasma', 'inferno', 'cividis']

# Tworzenie subplots dla różnych kolorystyk
for i, cmap_name in enumerate(colormaps, 1):
    ax = fig.add_subplot(2, 3, i, projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cmap_name, linewidth=0, antialiased=False)
    ax.set_title(f"Colormap: {cmap_name}")
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()
