import gspec

def try_plot_a() -> None:

	s = gspec.import_txt('test/spec_a2h6.txt')
	b = gspec.import_txt('test/spec_a2h6.txt')
	b.add_spectrum(s, -0.7)
	gspec.plot(s, spectrum_string="Test spectrum",
		windows=[(60, 100), (140, 160)],
		bkg=b, bkg_string="Test background",
		title="Test A")


if __name__ == "__main__":
	try_plot_a()
