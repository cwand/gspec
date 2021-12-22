# type: ignore

import gspec
import pydicom
import tempfile


def read_mediso(fp: str) -> gspec.gspectrum:

	spectrum = gspec.gspectrum()  # This will contain our resulting spectrum

	ds = pydicom.dcmread(fp)

	spectrum.count_time = ds[0x0018, 0x1242].value  # Acquisition time in ms
	spectrum.count_time_units = 'ms'

	spectrum.energy_units = 'keV'

	file = tempfile.SpooledTemporaryFile()
	file.write(ds[0x0009, 0x10e6].value)  # This is where Mediso-private tags are

	# Read data from virtual DICOM file
	med_ds = pydicom.dcmread(file, force=True)
	# med_ds now contains all Mediso-private tags
	file.close()

	# Tag (0040,a730) contains a sequence of two items:
	# One item containing info about the detectors
	# One item containing info about recorded spectrum
	x = med_ds[0x0040, 0xa730]

	# The contained information is given for each item in the sequence in the tag
	# (0040,a043)>[Sequence item 0]>(0008,0100)
	# We find the index of the item containing spectrum information
	spectrum_index = -1
	for idx, sq_item in enumerate(x):
		idx_info = sq_item[0x0040, 0xa043]
		idx_info = idx_info[0]
		if idx_info[0x0008, 0x0100].value == "Spectrums":
			spectrum_index = idx

	x = x[spectrum_index]  # x is now the item in the sequence containing spectrums

	# The recorded spectrum is saved in a single item sequence under the tag
	# (0040,a730)
	x = x[0x0040, 0xa730]
	x = x[0]

	# Under the tag (0040,a730) is a sequence containing three things:
	# The spectrum (Spectrum cps by keV) <- What we want
	# Information about the head
	# Information about the frameID
	x = x[0x0040, 0xa730]
	# The contained information is given for each item in the sequence in the tag
	# (0040,a043)>[Sequence item 0]>(0008,0100)
	# We find the index of the item containing spectrum information
	spectrum_index = -1
	for idx, sq_item in enumerate(x):
		idx_info = sq_item[0x0040, 0xa043]
		idx_info = idx_info[0]
		if idx_info[0x0008, 0x0100].value == "Spectrum cps by keV":
			spectrum_index = idx

	x = x[spectrum_index]  # x is now the item containing the spectrum

	# The spectrum is saved in the tag (0009,10ea) in utf-8 encoded byte format
	x = x[0x0009, 0x10ea].value
	s = x.decode('utf-8')
	# s now contains the spectrum as a string
	# with columns [Energy(keV)  Countrate(cps)]

	# Read the spectrum string line by line
	bins = s.split('\n')

	return spectrum
