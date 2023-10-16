import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0., 1., 0.1)

plt.xkcd()

plt.plot(x, x, 'v-', x, x**2, 'x-', x, x**3, 'o-')

plt.savefig('functions.pdf')
plt.show()
