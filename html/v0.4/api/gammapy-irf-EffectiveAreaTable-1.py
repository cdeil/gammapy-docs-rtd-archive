import matplotlib.pyplot as plt
from gammapy.irf import EffectiveAreaTable
from gammapy.datasets import gammapy_extra
filename = gammapy_extra.filename('datasets/hess-crab4_pha/ogip_data/arf_run23523.fits')
arf = EffectiveAreaTable.read(filename)
arf.plot(show_safe_energy=True)
plt.show()