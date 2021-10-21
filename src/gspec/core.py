from typing import DefaultDict
from collections import defaultdict
from typing import List


class spectrum:

	def __init__(self):
		self.energy_units = 'keV'
		self.spectrum_data: DefaultDict[int, float] = defaultdict(float)

		self.count_time = 0.0
		self.count_time_units = 's'

	# Get the total number of counts in a specified window of the spectrum
	def get_counts(self, energies: List[int]):
		sum = 0.0
		for e in energies:
			sum += self.spectrum_data[e]

		return sum

	# Set the number of counts in a specified bin of the spectrum
	def set_counts(self, energy: int, counts: float):
		self.spectrum_data[energy] = counts

	def subtract_spectrum(self, spec='spectrum'):
		if self.count_time != spec.count_time:
			msg = "Different count_time values (" + str(self.count_time)
			msg += " vs " + str(spec.count_time) + "). "
			msg += "Set force=True to enforce subtraction."
			raise ValueError(msg)
		for e, c in spec.spectrum_data.items():
			self.spectrum_data[e] -= c
