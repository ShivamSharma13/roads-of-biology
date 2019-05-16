import re
from input_reader import two_line_reader


codon_to_protein = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
					"UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
					"UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
					"UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
					"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
					"CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
					"CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
					"CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
					"AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
					"ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
					"AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
					"AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
					"GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
					"GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
					"GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
					"GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

def reverse_complementry(dna_string):
	complementry_dict = {'A' : 'U', 'U' : 'A', 'G' : 'C', 'C' : 'G'}
	return "".join([complementry_dict[i] for i in list(dna_string[::-1])])


def fix_rna_string_length(rna_string):
	'''
	This chips off additional nucleotides if they can't completely fall into a codon.
	'''
	length = len(rna_string)
	if length%3 == 0:
		return rna_string
	elif length%3 == 1:
		return rna_string[:-1]
	elif length%3 == 2:
		return rna_string[:-2]


def find_matches(rna_string, protein_string):
	matched_rnas = []
	protein_length = len(protein_string)
	matched_rna_length = protein_length * 3
	for i in range(3):
		edited_rna_string = fix_rna_string_length(rna_string[i:])
		protein_from_edited_rna_string = rna_to_protein(edited_rna_string)
		if protein_string in protein_from_edited_rna_string:

			#Getting all occurances (indices) of the protein substring from edited RNA string.
			matches = [m.start() for m in re.finditer(protein_string, protein_from_edited_rna_string)]
			for match_index in matches:
				
				#Obtaining the original RNA string.
				obtained_rna_substring = edited_rna_string[match_index*3:match_index*3+matched_rna_length]
				matched_rnas.append(obtained_rna_substring)
	
	return matched_rnas
				
			
def rna_to_protein(rna_string):
	return "".join([codon_to_protein[rna_string[i:i+3]] for i in range(len(rna_string))[::3]])


def peptide_encoding(input_dna_string, protein_string):
	'''
	Could be achieved smaller complexity Rabin-Karp or Boyer-Moore algorithm.
	'''
	
	rna_string = input_dna_string.replace('T', 'U')
	matched_strings = find_matches(rna_string, protein_string)
	
	#Checking the same for reversed complementry string.
	reverse_matched_strings = find_matches(reverse_complementry(rna_string), protein_string)
	
	#Adding both while reverting back the reversed complementry string.
	output = [i.replace('U', 'T') for i in matched_strings + [reverse_complementry(i) for i in reverse_matched_strings]]
	print('\n'.join(output))


if __name__ == "__main__":
	#input_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
	#protein = rna_to_protein(rna_string)
	#print(protein)
	input_dna_string, protein_string = two_line_reader("dataset_203_7.txt")
	
	encoder_codon_string = peptide_encoding(input_dna_string, protein_string)
	#print(encoder_codon_string)