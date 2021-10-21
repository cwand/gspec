import unittest
import gspec


class TestSpectrum(unittest.TestCase):

	def test_default_energy_units(self):
		s = gspec.spectrum()
		self.assertEqual(s.energy_units, 'keV')
