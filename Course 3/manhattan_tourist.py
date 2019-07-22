def obtain_longest_path_recursively(weighted_matrix, i, j):
	'''
	Simply replicated, not sure if this function works.
	'''
	if i == 0 and j == 0:
		return 0
	x = -100
	y = -100
	if i > 0:
		x = obtain_longest_path_recursively(weighted_matrix, i-1, j) + weighted_matrix[i-1][j]
	if j > 0:
		y = obtain_longest_path_recursively(weighted_matrix, i, j-1) + weighted_matrix[i][j-1]

	return max(x, y)


def obtain_longest_path_dp(number_of_rows, number_of_columns, vertical_edges_matrix, horizontal_edges_matrix):
	#Initiating a 2D weighted matrix with all values=0.
	weighted_matrix = [[0 for a in range(number_of_columns+1)] for b in range(number_of_rows+1)]
	
	#Initializing the first column.
	for idx, row in enumerate(weighted_matrix[1:]):
		weighted_matrix[idx+1][0] = weighted_matrix[idx][0] + vertical_edges_matrix[idx][0]

	#Initializing the first row.
	for idx, row in enumerate(weighted_matrix[0][1:]):
		weighted_matrix[0][idx+1] = weighted_matrix[0][idx] + vertical_edges_matrix[0][idx]
	'''
	for i in weighted_matrix:
		print(i)
	'''
	for row_index, row in enumerate(weighted_matrix):
		for columne_index, value in enumerate(row):
			if row_index == 0 or columne_index == 0:
				continue
			weighted_matrix[row_index][columne_index] = max((weighted_matrix[row_index-1][columne_index] 
														+ vertical_edges_matrix[row_index-1][columne_index]), 
														(weighted_matrix[row_index][columne_index-1] 
														+ horizontal_edges_matrix[row_index][columne_index-1]))
	'''
	for i in weighted_matrix:
		print(i)
	'''

	return weighted_matrix[number_of_rows][number_of_columns]


def store_manhattan_graph(number_of_rows, number_of_columns, raw_vertical_edges_matrix, raw_horizontal_edges_matrix):
	vertical_edges_matrix = []
	horizontal_edges_matrix = []
	for row in raw_vertical_edges_matrix:
		vertical_edges_matrix.append([int(i) for i in row.split(' ')])

	for row in raw_horizontal_edges_matrix:
		horizontal_edges_matrix.append([int(i) for i in row.split(' ')])

	return vertical_edges_matrix, horizontal_edges_matrix

if __name__ == '__main__':
	'''
	Most weighted path is also called the longest path. 
	'''
	with open('sample_data.txt') as f:
		number_of_rows, number_of_columns = f.readline().strip('\n').split(' ')
		raw_matrix = f.read()

	raw_vertical_edges_matrix, raw_horizontal_edges_matrix = raw_matrix.split('-')
	vertical_edges_matrix, horizontal_edges_matrix = store_manhattan_graph(int(number_of_rows), int(number_of_columns), 
		raw_vertical_edges_matrix.strip('\n').split('\n'), 
		raw_horizontal_edges_matrix.strip('\n').split('\n'))
	#print(len(vertical_edges_matrix))
	#print(len(horizontal_edges_matrix))

	longest_path = obtain_longest_path_dp(int(number_of_rows), int(number_of_columns), 
		vertical_edges_matrix, horizontal_edges_matrix)


	print(longest_path)



