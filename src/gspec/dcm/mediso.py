import gspec
import pydicom
import tempfile
import numpy as np

def read_mediso(fp: str) -> gspec.gspectrum:

	ds = pydicom.dcmread(fp)
	file = tempfile.SpooledTemporaryFile()
	file.write(ds[0x0009,0x10e6].value)

	# Read data from virtual DICOM file
	med_ds = pydicom.dcmread(file,force=True)
	file.close()

	x = med_ds[0x0040,0xa730]
	y = x[1]
	z = y[0x0040,0xa730]
	a = z[0]
	b = a[0x0040,0xa730]
	c = b[2]
	d = c[0x0009,0x10ea].value
	s = d.decode('utf-8')
	print(s)



	return 0.0
