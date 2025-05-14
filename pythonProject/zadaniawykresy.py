import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,21)
y = 1/x

plt.plot(x,y, label ='f(x) = 1/x')
plt.axis([0,len(x),0,1])
plt.title('Prosty wykres')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()