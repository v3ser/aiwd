import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1,31,0.1)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y, label = 'sin(x)')
plt.plot(x, y1, label = 'cos(x)')

plt.xlabel('x')
plt.ylabel('funkcje trygonometryczne')
plt.title('Wykres sin(x) i cos(x)')
plt.legend()
plt.show()
