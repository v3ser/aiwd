import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,31,0.1)
y = -np.sin(x)
y1 = np.sin(x) + 2

plt.plot(x, y, label = 'sin(x)')
plt.plot(x, y1, label = 'sin(x)')

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x),sin(x)')
plt.legend()
plt.show()
