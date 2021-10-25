import gspec
import sys


def try_plot_a() -> None:

	s = gspec.import_txt('test/spec_a2h6.txt')
	gspec.plot(s)


if __name__ == "__main__":
	if sys.argv[1] == "a":
		try_plot_a()
		exit()
