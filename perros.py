import numpy as np
import matplotlib.pyplot as plt

labradores = 300
corrientes = 300

lab_alt = 28 + 4 * np.random.randn(labradores)
corr_atl = 24 + 4 * np.random.randn(corrientes)

plt.hist([lab_alt,corr_atl], stacked=True,color = ['r','b'])
plt.show()