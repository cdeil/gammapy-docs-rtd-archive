import matplotlib.pyplot as plt
from gammapy.irf import EnergyDispersion2D
from gammapy.utils.energy import EnergyBounds
filename = '$GAMMAPY_EXTRA/test_datasets/irf/hess/pa/hess_edisp_2d_023523.fits.gz'
edisp = EnergyDispersion2D.read(filename, hdu='ENERGY DISPERSION')
e_axis = EnergyBounds.equal_log_spacing(0.1,20,60, 'TeV')
rmf = edisp.to_energy_dispersion('1.2 deg', e_reco = e_axis, e_true = e_axis)
rmf.plot_matrix()
plt.loglog()