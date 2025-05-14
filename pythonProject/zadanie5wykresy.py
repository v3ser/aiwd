import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris.data', header= None)

print(df)

plt.scatter('sepal length','sepal width' , data=df)
plt.show()