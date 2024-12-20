import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 


Ny = np.random.normal(0, 1, size=(200,))
Nx = np.random.normal(0, 1, size=(200,))

Y = Ny
X = Y ** 2 + Nx

sns.scatterplot(x=X,y=Y)
plt.show()

