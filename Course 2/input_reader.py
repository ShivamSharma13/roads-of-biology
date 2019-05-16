def one_line_reader(file_name):
	with open(file_name, 'r') as f:
		text = f.read()
	return text


def two_line_reader(file_name):
	with open(file_name, 'r') as f:
		text = f.read()

	split = text.split("\n")
	return split[0], split[1]