import matplotlib.pyplot as plt
from gammapy.irf import EffectiveAreaTable
from gammapy.datasets import load_arf_fits_table
arf = EffectiveAreaTable.from_fits(load_arf_fits_table())
arf.plot_area_vs_energy(show_save_energy=False)
plt.show()