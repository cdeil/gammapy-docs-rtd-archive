from gammapy.image import SkyMap
from gammapy.datasets import load_poisson_stats_image

f = load_poisson_stats_image(return_filenames=True)
counts = SkyMap.read(f)
counts.name = 'Counts'
counts.show()