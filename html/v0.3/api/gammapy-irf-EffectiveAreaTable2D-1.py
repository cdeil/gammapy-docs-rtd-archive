import matplotlib.pyplot as plt
from gammapy.irf import EffectiveAreaTable2D
from gammapy.datasets import load_aeff2D_fits_table
aeff2D = EffectiveAreaTable2D.from_fits(load_aeff2D_fits_table())
aeff2D.plot_energy_dependence()
plt.loglog()
plt.xlim(0.8, 100)
plt.ylim(2E4, 2E6)