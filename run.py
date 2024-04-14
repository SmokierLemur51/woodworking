import argparse

import core.options as options


def main():
	# First parse arguments to see where we are going.
	parser = argparse.ArgumentParser()
	parser.add_argument("a", nargs="?", default="gui")
	args = parser.parse_args()
	command = options.ARGUMENTS[args.a]
	if command:
		command()


if __name__ == "__main__":
	main()