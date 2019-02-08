'''
A method to assemble a genome, since the String Reconstruction Problem reduces to 
finding an Eulerian path in the de Bruijn graph generated from reads.


Input: An integer k followed by a list of k-mers Patterns.
	 Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

Sample Input:
	4
	CTTA
	ACCA
	TACC
	GGCT
	GCTT
	TTAC

Sample Output:
	GGCTTACCA
'''

from de_bruijn_from_kmers import create_graph
from eulerian_path import *

def process_input():
	with open('test_dataset.txt' , 'r') as f:
		text = f.read()

	input_strings = text.split('\n')

	#removing any empty strings.
	input_strings = list(filter(None, input_strings))

	de_bruijn_graph_strings = create_graph(input_strings[1:])

	graph = {}

	for de_bruijn_graph_string in de_bruijn_graph_strings:
		input_string_line = de_bruijn_graph_string.split(' -> ')
		graph[input_string_line[0]] = input_string_line[-1].split(',')

	return graph

if __name__ == '__main__':
	graph = process_input()
	start, end = find_start_end_nodes(graph)
	path = traverse_graph(graph, str(start), str(end))
	print(''.join([path[0]] + [line[-1] for idx, line in enumerate(path) if idx != 0]))















