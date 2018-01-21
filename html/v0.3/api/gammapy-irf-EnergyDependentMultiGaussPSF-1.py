import matplotlib.pyplot as plt
from gammapy.irf import EnergyDependentMultiGaussPSF
from gammapy.datasets import load_psf_fits_table
psf = EnergyDependentMultiGaussPSF.from_fits(load_psf_fits_table())
psf.plot_containment(0.68, show_save_energy=False)
plt.show()