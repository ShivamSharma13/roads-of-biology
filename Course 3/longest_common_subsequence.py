'''
Sample Input:
AACCTTGG
ACACTGTGA

Sample Output:
AACTGG
'''
def sequence_from_sink_to_source(backtrack_matrix, i, j, sequence_1):
	'''
	Function which traces the nodes from which the longest_path (highest weighted) came from. 
	'''
	seq = ''
	while i>0 and j>0:
		if backtrack_matrix[i][j] == 'diag':
			seq = sequence_1[i-1] + seq
			i -= 1
			j -= 1
			continue
		if backtrack_matrix[i][j] == 'down':
			i -= 1
			continue
		if backtrack_matrix[i][j] == 'righ':
			j -= 1
			continue
	return seq

def obtain_longest_path(vertical_edges_matrix, horizontal_edges_matrix, diagonal_edges_matrix, weighted_matrix, backtrack_matrix):
	'''
	To find the maximum weight possible for sink node.
	'''
	for row_idx, row in enumerate(weighted_matrix):
		for column_idx, column in enumerate(row):
			if row_idx == 0 or column_idx == 0:
				continue
			
			
			down = weighted_matrix[row_idx-1][column_idx] + vertical_edges_matrix[row_idx-1][column_idx]
			right = weighted_matrix[row_idx][column_idx-1] + horizontal_edges_matrix[row_idx][column_idx-1]
			diagonal = weighted_matrix[row_idx-1][column_idx-1] + diagonal_edges_matrix[row_idx-1][column_idx-1]
			weighted_matrix[row_idx][column_idx] = max(down, right, diagonal)

			if down>=right and down>=diagonal:
				backtrack_matrix[row_idx][column_idx] = 'down'
			elif right>=down and right>=diagonal:
				backtrack_matrix[row_idx][column_idx] = 'righ'
			elif diagonal>=right and diagonal>=down:
				backtrack_matrix[row_idx][column_idx] = 'diag'

	'''
	for i in weighted_matrix:
		print(i)
	'''
	return weighted_matrix, backtrack_matrix


def generate_edges_matrices_from_sequences(sequence_1, sequence_2):
	vertical_edges_matrix = [[0]*(len(sequence_2)+1)]*len(sequence_1)
	horizontal_edges_matrix = [[0]*len(sequence_2)]*(len(sequence_1)+1)
	diagonal_edges_matrix = []
	for nt in sequence_1:
		diagonal_edges_matrix.append([1 if nt == i else 0 for i in sequence_2])
	
	return vertical_edges_matrix, horizontal_edges_matrix, diagonal_edges_matrix



if __name__ == "__main__":
	sequence_1 = 'TACGTCTATTACTCTTTAGAAGAGGATGTAATGAATCAAGCGGGCGAGCCATTTTTTACGCTGCTGGATACCTGCGCAGCCGACGGGGGCTGGGTTAACGAATTTCCTGCACTGGTCAAGGAAACGCCGAAGCCGTGGACGAGAGTACCAGGAGGGGTTGCATCGTATCGATTTCCGCGCACCTGCCTGCGCCTTACGCGTGGTACCATAGTGTCCTGTACTGAAATATTCACTTAATACAGTCGCATACCAACGAGAGTCGCTTCATAGTCGGTGGCCTGTCTCTTAGTATTAATTGCTCTGTAAGCCTGGTGGACATACTAGTGATCACCATGTTCAACTGAAGAGGCTCATGTCTGGACACATATCCGACATGGAAAAAAAAAAGGTGCATAAAAATAATCCCGGATGTCGCCTCTTAATGAATCGCGGCGCCGCGATGGGCGTCAGTCTGTAGCCTTTGCCCGAAAGCATAGACCCTCAACGGAGCTGCCGCCTTGGTTGGCAGGTGGATGGAGAAAGCAGTAAGAACAAATCCTATCTTCGGACGCCGGACGGAGGAAGTACGTCCGTTCTTTTTGGCCTCAGGAAGCACCGGGATTAATTTATGTAGGTGTAACGGAACTCTCGCGGCACTGTTTCCAAGCGTCCCCTCGCTATGTGCTTGCTGTCGCGGGAAATCGTCATGGTTAAGCCCCTCTACTTCCCTCTTCTGATGGAGAGCTCCGAGGGTACTATAAGCGGGGTCTAATTGTGTTGTATGCACACTCCGGCGAACTGCATTTCGGATGGCATTTCCACAGGTGCGCAGTCTAACACCTTTTAATCTACTA'
	sequence_2 = 'TACCTTCTCAGGGCTCGAGGACCGAAAAGTGCTCTGATTCTTGAACCTACTCTGAATCCTTGGATACGATCCAGGCGAGTATCGTAGTACAGGCCGTGATACAAAGAAAGACTGTCGCCAGCGATTATCTTTAAATCCACCGTGACCTGGCAGACAGAGCCGGATCCGCTCCGTACGCTCAAACGTTAATGTGAGTTAATTGGTCTAACGAGTGTTAATCGAACGACTGGGGAGCCTCTTATACTTTGGACTCGTCGAGTCTATATGAGATCCGGGCTGATCTGTGTGTCATCATGCTAGGATGAGGTGGTGTGCCAGGCGGTGTGTTCAGGGGTCCCACGTTGCTAGCTAATTGTCTGCCTGTTGTACACCAAACGATTTGGACACACGTGGAACCGGCCCTCGTAAAATCGAAAGGAGCCAGCTATGTGGAACGCTCAGGGGAGCCGTTCATCTACTCAAAGTACCAGGGTTAACAGTATCGTGATGGTGTATGCGTAAAGTGCGACGTAAGCGTAAACGGTCTTAATCTGCACGATTAGGAACCTATCTAACCGGCGGCCAACAACACGAACCTCGCCACGCTAGGCTGCTGTACACTTGAATTCCCGTGCGCGGTGTGAACTGCTTGAACGCGGAATGCAACGTACCGTGGTGTCGGAACGACATAGCTACTGACAGCAGGTATTCCTAGGCCCATTTCATAGGCTGACTTACTCTTCCGGCTCCGCATCCAGGAATCGGCGGGGGGTCGCGCTTTGTGAATTTACAATGATGACGTCTCGGAGCTGTAAATGTACTTCAACAAGATACACTGTGATATCGCCGCTTTTACTAGCGCCGAATCAAAAGGCAGGGTCGGTCGAATGTGGATTTATCCGCGGCGAGTATCTGGAGCGTGATATAGACCACCAGCTCGCTAGCAACCAAATCCAGTGGTGTACGCTTCTATTCGTGAGTTGTGACATCCC'
	weighted_matrix = [[0 for i in range(len(sequence_2)+1)] for j in range(len(sequence_1)+1)]

	#'unkn' stands for unknown: certain values (at the edge of weight matrix) would not Backtrack to any value.
	backtrack_matrix = [['unkn' for i in range(len(sequence_2)+1)] for j in range(len(sequence_1)+1)]


	vertical_edges_matrix, horizontal_edges_matrix, diagonal_edges_matrix = generate_edges_matrices_from_sequences(sequence_1, 
																			sequence_2)
	weighted_matrix, backtrack_matrix = obtain_longest_path(vertical_edges_matrix, 
															horizontal_edges_matrix, 
															diagonal_edges_matrix, 
															weighted_matrix, 
															backtrack_matrix)
	'''
	print(weighted_matrix)
	for i in backtrack_matrix:
		print(i)
	'''
	lcs_sequence = sequence_from_sink_to_source(backtrack_matrix, len(sequence_1), len(sequence_2), sequence_1)
	print(lcs_sequence)








