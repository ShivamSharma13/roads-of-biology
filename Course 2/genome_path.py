with open('dataset_198_3.txt', 'r') as f:
	text = f.read()

genome_path_strings = text.split('\n')

print(''.join([genome_path_strings[0]] + [line[-1] for idx, line in enumerate(genome_path_strings) if idx != 0]))
