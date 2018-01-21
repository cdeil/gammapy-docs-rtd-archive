from gammapy.image import colormap_milagro
vmin, vmax, vtransition = -5, 15, 5
cmap = colormap_milagro(vmin=vmin, vmax=vmax, vtransition=vtransition)

# This is how to plot a colorbar only with matplotlib
# http://matplotlib.org/examples/api/colorbar_only.html
import matplotlib.pyplot as plt
from matplotlib.colorbar import ColorbarBase
from matplotlib.colors import Normalize
norm = Normalize(vmin, vmax)
fig = plt.figure(figsize=(8, 1))
fig.add_axes([0.05, 0.3, 0.9, 0.6])
ColorbarBase(plt.gca(), cmap, norm, orientation='horizontal')
plt.show()