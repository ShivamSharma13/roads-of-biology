from input_reader import one_line_reader


dalton_mass = {'G': 57,
				'A': 71,
				'S': 87,
				'P': 97,
				'V': 99,
				'T': 101,
				'C': 103,
				'I': 113,
				'L': 113,
				'N': 114,
				'D': 115,
				'K': 128,
				'Q': 128,
				'E': 129,
				'M': 131,
				'H': 137,
				'F': 147,
				'R': 156,
				'Y': 163,
				'W': 186,}

reverse_dalton_mass = {'57' : 'G', 
						'71':'A',
						'87' : 'S', 
						'97' : 'P',
						'99' : 'V',
						'101' : 'T',
						'103' : 'C',
						'113' : 'L',
						'114' : 'N',
						'115' : 'D',
						'128' : 'K',
						'129' : 'E',
						'131' : 'M',
						'137' : 'H',
						'147' : 'F',
						'156' : 'R',
						'163' : 'Y',
						'186' : 'W',}

def generate_theoritical_spectrum(protein_string, linear = False):
	subpeptides = generate_subpeptides(protein_string, linear)
	theoritical_spectrum = {}
	theoritical_spectrum_values = []
	for subpeptide in subpeptides:
		if len(subpeptide) == 1:
			theoritical_spectrum[subpeptide] = dalton_mass[subpeptide]
		elif len(subpeptide) == 2:
			theoritical_spectrum[subpeptide] = dalton_mass[subpeptide[1]] + dalton_mass[subpeptide[0]]
		else: 
			theoritical_spectrum[subpeptide] = theoritical_spectrum[subpeptide[:-1]] + dalton_mass[subpeptide[-1]]
		theoritical_spectrum_values.append(theoritical_spectrum[subpeptide])
	theoritical_spectrum_values.append(0)
	theoritical_spectrum_values.sort()
	return theoritical_spectrum_values

def generate_subpeptides(protein_string, linear = False):
	if linear:
		#Here the circular protein string actually is just the linear string.
		circular_protein_string = protein_string
		length = len(protein_string)
		return [protein_string[i:j+1] for i in range(length) for j in range(i,length)]
	else:
		circular_protein_string = list(protein_string) + list(protein_string[:-1])
		limiter = len(protein_string)
		subpeptides = []
		for window_size in range(1, len(protein_string)):
			iterator = 0
			while iterator < limiter:
				subpeptides.append(''.join(circular_protein_string[iterator:iterator+window_size]))
				iterator+=1
		subpeptides.append(protein_string)
		return subpeptides

if __name__ == '__main__':
	protein_string = one_line_reader('dataset_203_7.txt')
	theoritical_spectrum = generate_theoritical_spectrum(protein_string)
	print(' '.join([str(val) for val in theoritical_spectrum]))
