import unittest
import gspec
import gspec.dcm
import datetime


class TestMediso(unittest.TestCase):

	def test_meas_time(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(s.count_time, 300)
		self.assertEqual(s.count_time_units, 's')

	def test_energy_units(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(s.energy_units, 'keV')

	def test_date(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(s.meas_date, datetime.date(2021, 10, 13))

	def test_spec_data(self):
		self.assertEqual(0, 1 + 1)
