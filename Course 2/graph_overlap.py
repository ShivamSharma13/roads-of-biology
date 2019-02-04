with open('dataset_198_10.txt', 'r') as f:
	text = f.read()

#input_strings_text = text.split('Output:')[0].split('Input:')[1]
input_strings = text.split('\n')

#removing any empty strings.
input_strings = list(filter(None, input_strings))

output = {string:[] for string in input_strings}

suffix = {string:string[1:] for string in input_strings}
prefix = {string[:-1]:string for string in input_strings}

for string, suffix in suffix.items():
	try:
		output[string].append(prefix[suffix])
	except KeyError:
		pass


for key, value in output.items():
	if len(value) > 0:
		print(key + ' -> ' + ','.join(value))
