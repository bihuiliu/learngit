#1/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt

a = np.linspace(1,100,20)
b = [x**2 for x in range(20)]

x = plt.figure()
plt.plot(a,b,c='red')
plt.show()
