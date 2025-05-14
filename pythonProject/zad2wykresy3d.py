import matplotlib.pyplot as plt
import numpy as np

# Ustawiamy seed by wyniki były powtarzalne
np.random.seed(19680801)

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

# Lista kolorów i znaczników
styles = [
    ('r', 'o', -50, -25),
    ('b', '^', -40, -10),
    ('g', 's', -60, -30),
    ('m', 'x', -45, -15),
    ('c', 'D', -35, -5)
]

# Generowanie i rysowanie 5 serii punktów
for c, m, zlow, zhigh in styles:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m, label=f'{c}-{m}')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.legend()
plt.show()
