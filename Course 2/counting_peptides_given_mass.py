reduced_dalton_mass = {'G': 57,
					'A': 71,
					'S': 87,
					'P': 97,
					'V': 99,
					'T': 101,
					'C': 103,
					'I': 113,
					#'L': 113,
					'N': 114,
					'D': 115,
					'K': 128,
					#'Q': 128,
					'E': 129,
					'M': 131,
					'H': 137,
					'F': 147,
					'R': 156,
					'Y': 163,
					'W': 186,}

amino_acids = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
silly_list = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
silly_list_dict = {i:1 for i in silly_list}
useless = {}

levels = {}

check = 270
silly_list_dict[check] = 1

counter = 0

def create_tree():
	global counter
	'''
	The Dynamic programming problem. Couldn't do it.
	'''

	'''
	idx = 0
	while len(silly_list):
		idx += 1
		print(idx, silly_list_dict[check])
		if silly_list_dict[check] > 15000:
			return
		mass = silly_list.pop()
		
		for amino_acid_mass in amino_acid_masses:
			new_mass = mass + amino_acid_mass
			if new_mass > check:
				continue
			if new_mass
			silly_list.append(new_mass)
			try:
				silly_list_dict[new_mass] += 1
			except KeyError:
				silly_list_dict[new_mass] = 1
	'''
	
	while True:
		if len(all_possibles) > 2:
			return
		 


if __name__ == '__main__':
	create_tree()
	for el in all_possibles:
		print(len(el))
	












