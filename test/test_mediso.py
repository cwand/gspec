import unittest
import gspec
from gspec import dcm
from pathlib import Path
import numpy as np


class TestMediso(unittest.TestCase):

	def test_meas_time(self):
		s = gspec.dcm.read_mediso('test/00000001.dcm')
		self.assertEqual(s.count_time, 300)
		self.assertEqual(s.count_time_units, 's')
