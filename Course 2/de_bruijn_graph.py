with open('dataset_199_6.txt', 'r') as f:
	text = f.read()

input_strings = text.split('\n')

#removing any empty strings.
input_strings = list(filter(None, input_strings))

#k = int(input_strings[0])
k = int(input_strings[0]) - 1

input_string_text = input_strings[1]

kmers = [input_string_text[i:i+k] for i in range(len(input_string_text) - k + 1)]
#k_minus_1_mers = [input_string_text[i:i+k-1] for i in range(len(input_string_text) - k + 2)]

output = {kmer:[] for kmer in kmers}

for idx in range(len(kmers) - 1):
	output[kmers[idx]].append(kmers[idx+1])

for key, value in output.items():
	if len(value) > 0:
		print(key + ' -> ' + ','.join(value))