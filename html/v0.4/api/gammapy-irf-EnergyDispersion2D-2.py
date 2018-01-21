import matplotlib.pyplot as plt
import numpy as np
from gammapy.irf import EnergyDispersion2D
from gammapy.utils.energy import Energy
from astropy.coordinates import Angle
filename = '$GAMMAPY_EXTRA/test_datasets/irf/hess/pa/hess_edisp_2d_023523.fits.gz'
edisp = EnergyDispersion2D.read(filename, hdu='ENERGY DISPERSION')
migra = np.linspace(0.1,2,80)
e_true = Energy.equal_log_spacing(0.13,60,60,'TeV')
offset = Angle([0.554], 'deg')
edisp.plot_bias(offset=offset, e_true=e_true, migra=migra)
plt.xscale('log')