
def process_text():
	with open('test_dataset.txt', 'r') as f:
		text = f.read()

	input_strings = text.split('\n')

	#removing any empty strings.
	input_strings = list(filter(None, input_strings))

def create_graph(input_strings):
	unique_k_minus_1_mers = {}
	output = []
	for input_string in input_strings:
		unique_k_minus_1_mers[input_string[:-1]] = []
		unique_k_minus_1_mers[input_string[1:]] = []

	for input_string in input_strings:
		unique_k_minus_1_mers[input_string[:-1]].append(input_string[1:])

	for key, value in unique_k_minus_1_mers.items():
		if len(value) > 0:
			#print(key + ' -> ' + ','.join(value))
			
			output.append(key + ' -> ' + ','.join(value))

	return output

if __name__ == '__main__':
	input_strings = process_text()
	create_graph(input_strings)