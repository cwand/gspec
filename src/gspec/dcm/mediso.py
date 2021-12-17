import gspec
import pydicom
import tempfile
import numpy as np

def read_mediso(fp: str) -> gspec.gspectrum:

	ds = pydicom.dcmread(fp)
	file = tempfile.SpooledTemporaryFile()
	file.write(ds[0x0009,0x10e6].value)

	# Read data from virtual DICOM file
	med_ds = pydicom.dcmread(file,force=True) # type: ignore
	file.close()

	x = med_ds[0x0040,0xa730]
	x = x[1]
	x = x[0x0040,0xa730] # type: ignore
	x = x[0]
	x = x[0x0040,0xa730] # type: ignore
	x = x[2]
	x = x[0x0009,0x10ea].value # type: ignore
	s = x.decode('utf-8') # type: ignore
	#print(s)



	return gspec.gspectrum()
