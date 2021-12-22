import unittest
import gspec
from gspec import dcm


class TestMediso(unittest.TestCase):

	def test_meas_time(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(s.count_time, 300000)
		self.assertEqual(s.count_time_units, 'ms')

	def test_energy_units(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(s.energy_units, 'keV')

	def test_date(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(1+1,0)
