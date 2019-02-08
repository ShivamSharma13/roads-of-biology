import random

def process_test_dataset():
	with open('test_dataset.txt' , 'r') as f:
		text = f.read()

	input_strings = text.split('\n')

	graph = {}

	for input_string in input_strings:
		input_string_line = input_string.split(' -> ')
		graph[input_string_line[0]] = input_string_line[-1].split(',')

	return graph

def traverse_graph(graph):
	'''
	Directed Graph stored as:
	{
		'0': ['3'], 
		'1': ['0'], 
		'2': ['1', '6'], 
		'3': ['2'], 
		'4': ['2'], 
		'5': ['4'], 
		'6': ['5', '8'], 
		'7': ['9'], 
		'8': ['7'], 
		'9': ['6']
	}

	'''
	cycle = []
	no_of_edges = len([terminal_node for values in list(graph.values()) for terminal_node in values])

	#Randomly select a node from the graph.
	first_node = random.choice(list(graph.keys()))

	current_node = first_node
	node_with_additional_edges = None
	while True:
		#print('cycle: ' + str(cycle))
		if len(cycle) > no_of_edges and not node_with_additional_edges:
			break
		cycle.append(current_node)
		previous_node = current_node
		#print('current_node: ' + str(current_node))

		try:
			current_node = graph[previous_node].pop()
		except IndexError:
			#print('cycle: ' + str(cycle))
			#print('graph: ' + str(graph))
			#print('more edges: ' + str(node_with_additional_edges))
			if not node_with_additional_edges:
				return cycle
			cycle = rearrange_cycle(cycle, node_with_additional_edges)
			current_node = node_with_additional_edges
			#print('rearrange_cycle: ' + str(cycle))

		
		node_with_additional_edges = get_node_with_additional_edges(graph, cycle)
		#print('more edges: ' + str(node_with_additional_edges))


def reset_graph():
	return process_test_dataset()


def get_node_with_additional_edges(graph, cycle):
	for el in cycle[1:]:
		if len(graph[el]) > 0:
			return el

def rearrange_cycle(cycle, center_el):
	cycle.pop()
	index = cycle.index(center_el)
	return cycle[index:] + cycle[:index]

if __name__ == '__main__':
	i = 1000
	'''
	while i > 0:
		i -= 1
		graph = process_test_dataset()
		#print(graph)
		
		print("->".join(traverse_graph(graph)))
	'''
	graph = process_test_dataset()
	#print(graph)
	print("->".join(traverse_graph(graph)))
	











