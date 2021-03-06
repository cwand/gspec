from typing import DefaultDict
from collections import defaultdict
from typing import List
from typing import Tuple
import numpy as np
import numpy.typing as npt
from datetime import date


class gspectrum:

	energy_units: str
	count_time: float
	count_time_units: str
	meas_date: date
	spectrum_data: DefaultDict[int, float]

	def __init__(self) -> None: ...
	def get_counts(self, energies: List[int]) -> float: ...
	def get_rate(self, energies: List[int]) -> float: ...
	def set_counts(self, energy: int, counts: float) -> None: ...
	def add_spectrum(self,
		spec: 'gspectrum',
		factor: float = ...,
		force: bool = ...
	) -> None: ...
	def print_txt(self, fp: str, force: bool = ...) -> None: ...

def import_txt(fp: str) -> gspectrum: ...
def import_numpy(data: npt.NDArray[np.float_],
	count_time: float = ..., count_time_units: str = ...,
	energy_units: str = ...
) -> gspectrum: ...

def plot(
	spectrum: gspectrum, spectrum_string: str = ...,
	windows: List[Tuple[float,float]] = ...,
	bkg: gspectrum = ..., bkg_string: str = ...,
	title: str = ...) -> None: ...


def read_mediso(fp: str) -> gspectrum: ...
