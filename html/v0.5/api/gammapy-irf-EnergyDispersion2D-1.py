import matplotlib.pyplot as plt
from gammapy.irf import EnergyDispersion2D
filename = '$GAMMAPY_EXTRA/test_datasets/irf/hess/pa/hess_edisp_2d_023523.fits.gz'
edisp = EnergyDispersion2D.read(filename, hdu='ENERGY DISPERSION')
edisp.plot_migration()
plt.xlim(0, 4)