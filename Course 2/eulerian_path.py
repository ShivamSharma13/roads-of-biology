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

def traverse_graph(graph, start, end):
	graph[end] = [start]
	#print(graph)
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
	first_node = start

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
			#print('more edges (inside): ' + str(node_with_additional_edges))
			if not node_with_additional_edges:
				#===========================Result Obtained==========================#
				'''
				We have found a cycle, but we will rearrange it to be sure.
				Eg:
					cycle: ['3', '4', '6', '7', '8', '9', '6', '3', '0', '2', '1', '3']
								  ^		^
								  End  Start
				Path is there, we just have to rearrange the cycle.
				'''
				end_index_in_cycle = cycle.index(end)
				if start == cycle[end_index_in_cycle + 1]:
					#WHatever may be the case, the last element needs to go because we don't want a Cycle, 
					#and this code runs to yield a Cycle, not a Path. 
					cycle.pop() 
					
					if end is not cycle[-1]:
						#Case where the last node is not present at the end of the list; as shown in the example list above.
						start_index_in_cycle = end_index_in_cycle + 1
						return cycle[start_index_in_cycle:] + cycle[0:end_index_in_cycle+1]
					else:
						#Last node is fortunately present at the end of the list, let's return the Cycle as is.
						return cycle

			
			#================Result Not Found========================#			
			'''
			Now we need to rearrange the whole list: 'Cycle'.
			'''
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


def find_start_end_nodes(graph):
	keys = [key for key in list(graph.keys())]
	values = [value for value_list in list(graph.values()) for value in value_list]
	
	all_nodes = {node:0 for node in keys + values}

	for key, values in graph.items():
		all_nodes[key] += len(values)
		for value in values:
			all_nodes[value] -= 1

	start = max(all_nodes, key = all_nodes.get)
	end = min(all_nodes, key = all_nodes.get)

	return start, end


if __name__ == '__main__':
	i = 1000
	'''
	For Testing Purposes...

	while i > 0:
		i -= 1
		graph = process_test_dataset()
		#print(graph)
		
		print("->".join(traverse_graph(graph)))
	'''
	graph = process_test_dataset()
	start, end = find_start_end_nodes(graph)

	print("->".join(traverse_graph(graph, str(start), str(end))))
	











