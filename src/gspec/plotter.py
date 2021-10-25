from .spectrum import gspectrum
import matplotlib.pyplot as plt
import numpy as np


def plot(spectrum: gspectrum, spectrum_string: str = "") -> None:

	# Convert spectrum data to numpy data
	min_energy = min(spectrum.spectrum_data.keys())
	print(min_energy)
	print(type(min_energy))
	max_energy = max(spectrum.spectrum_data.keys())
	sz = max_energy - min_energy + 1
	data_array = np.zeros((sz, 2))
	for i in range(0, sz):
		data_array[i, 0] = min_energy + i
		data_array[i, 1] = spectrum.get_counts([min_energy + i])

	plt.plot(data_array[:, 0], data_array[:, 1], label=spectrum_string)

	'''if physics.windows['Ra223'] is None:
		xlist = net_spec.rate_by_kev[:,0]
		ylist = net_spec.rate_by_kev[:,1]
		plt.fill_between(xlist,ylist)
	else:
		for window in physics.windows['Ra223']:
				xlist = np.arange(window[0],window[1]+1,1.0)
				ylist = net_spec.rate_by_kev[window[0]:window[1]+1,1]
				plt.fill_between(xlist,ylist)

		if self.bkg is not None:
			plt.plot(self.bkg.rate_by_kev[:,0],self.bkg.rate_by_kev[:,1],
				linestyle='--',color='0.4',label='background')'''

	plt.legend()
	# plt.xlabel("Energy [keV]")
	# plt.ylabel("Counts")
	# plt.title(self.name)
	plt.show()
