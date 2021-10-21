import unittest
import gspec


class TestSpectrum(unittest.TestCase):

	def test_default_energy_units(self):
		s = gspec.spectrum()
		self.assertEqual(s.energy_units, 'keV')

	def test_default_count_time(self):
		s = gspec.spectrum()
		self.assertEqual(s.count_time, 0.0)
		self.assertEqual(s.count_time_units, 's')

	def test_default_data(self):
		s = gspec.spectrum()
		self.assertEqual(len(s.spectrum_data), 0)

	def test_get_counts_no_data(self):
		s = gspec.spectrum()
		self.assertEqual(s.get_counts([510, 511, 512]), 0)

	def test_set_counts(self):
		s = gspec.spectrum()
		s.set_counts(509, 32.1)
		s.set_counts(510, 10.1)
		s.set_counts(511, 11.1)
		self.assertEqual(s.get_counts([510, 511, 512]), 21.2)

	def test_subtraction(self):
		s1 = gspec.spectrum()
		s1.set_counts(509, 32.1)
		s1.set_counts(510, 10.1)
		s1.set_counts(511, 11.1)

		s2 = gspec.spectrum()
		s2.set_counts(508, 1.0)
		s2.set_counts(509, 1.1)
		s2.set_counts(510, 1.2)

		s1.subtract_spectrum(s2)
		self.assertEqual(s1.get_counts([508]), -1.0)
		self.assertEqual(s1.get_counts([509]), 31.0)
		self.assertEqual(s1.get_counts([510]), 8.9)
		self.assertEqual(s1.get_counts([511]), 11.1)
		self.assertEqual(s1.get_counts([512]), 0.0)

		self.assertEqual(s2.get_counts([508]), 1.0)
		self.assertEqual(s2.get_counts([509]), 1.1)
		self.assertEqual(s2.get_counts([510]), 1.2)
		self.assertEqual(s2.get_counts([511]), 0.0)

	def test_subtraction_error_wrong_count_time(self):
		s1 = gspec.spectrum()
		s1.set_counts(509, 32.1)
		s1.set_counts(510, 10.1)
		s1.set_counts(511, 11.1)
		s1.count_time = 1.0

		s2 = gspec.spectrum()
		s2.set_counts(508, 1.0)
		s2.set_counts(509, 1.1)
		s2.set_counts(510, 1.2)

		self.assertRaises(ValueError, s1.subtract_spectrum, s2)
