from gammapy.utils.testing import data_manager
import matplotlib.pyplot as plt

dm = data_manager()
ds = dm['hess-crab4-hd-hap-prod2']
aeff2D = ds.obs(obs_id=23523).aeff
aeff2D.plot_energy_dependence()