import numpy as np
from gammapy.morphology import Sphere2D
import matplotlib.pyplot as plt

sphere = Sphere2D(amplitude=100., x_0=25., y_0=25.,
                r_0=20.)
y, x = np.mgrid[0:50, 0:50]
plt.imshow(sphere(x, y), origin='lower', interpolation='none')
plt.xlabel('x (pix)')
plt.ylabel('y (pix)')
plt.colorbar(label='Brightness (A.U.)')
plt.grid(False)
plt.show()