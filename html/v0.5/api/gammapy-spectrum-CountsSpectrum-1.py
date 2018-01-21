from gammapy.spectrum import CountsSpectrum
import numpy as np
import astropy.units as u

ebounds = np.logspace(0,1,11) * u.TeV
counts = np.arange(10) * u.ct
spec = CountsSpectrum(data=counts, energy=ebounds)
spec.plot(show_poisson_errors=True)