from cyclo_peptide_sequencing import generate_theoritical_spectrum, dalton_mass, reverse_dalton_mass
from input_reader import one_line_reader

amino_acid_masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def number_of_linear_peptides(n):
	sum = 0
	while n > 0:
		sum += n
		n -= 1
	return sum + 1



def mass(peptide):
	total_mass = 0
	peptide_in_list = peptide.split('-')
	for el in peptide_in_list:
		if el == '':
			continue
		total_mass += int(el)
	return total_mass



def generate_numeric_theoritical_spectrum(peptide, linear = True):
	dalton_mass_list = peptide.split('-')
	dalton_mass_to_protein_list = [reverse_dalton_mass[str(i)] for i in dalton_mass_list]
	theoritical_spectrum = generate_theoritical_spectrum(''.join(dalton_mass_to_protein_list), linear)
	#print(theoritical_spectrum)
	return [str(i) for i in theoritical_spectrum]



def expand(candidate_peptides, i):
	expansion_list = []
	dump = list(candidate_peptides)
	candidate_peptides = set()
	for peptide in dump:
		candidate_peptides.update([peptide + '-' + str(amino_acid_mass) if peptide is not '' else str(amino_acid_mass) for amino_acid_mass in amino_acid_masses])
	
	#Flush the set.
	if '' in candidate_peptides:
		candidate_peptides.discard('')
	
	return candidate_peptides



def if_consistent(peptide, spectrum):
	linear_theoritical_spectrum = generate_numeric_theoritical_spectrum(peptide)
	for el in linear_theoritical_spectrum:
		if el in spectrum:
			continue
		else:
			return False
	#print('Returned True')
	return True


def cyclopeptide_sequencing(spectrum):
	candidate_peptides = set([''])
	final_peptides = []
	i = 1
	while len(candidate_peptides):
		#print(candidate_peptides)

		candidate_peptides = expand(candidate_peptides, i)
		
		for peptide in list(candidate_peptides):
			if str(mass(peptide)) == spectrum[-1]:
				
				if peptide not in final_peptides:
					final_peptides.append(peptide)
				candidate_peptides.discard(peptide)
			elif not if_consistent(peptide, spectrum):
				candidate_peptides.discard(peptide)

		i += 1
	return final_peptides
		


if __name__ == '__main__':
	'''
	n = 11264
	number_of_linear_peptides = number_of_linear_peptides(n)
	print(number_of_linear_peptides)
	'''
	cyclo_spectrum = one_line_reader('dataset_203_7.txt')
	final_peptides = cyclopeptide_sequencing(cyclo_spectrum.split(' '))
	print(' '.join(final_peptides))







