with open('dataset_197_3.txt', 'r') as f:
	whole_text = f.read()

input_variables = whole_text.split('\n')

n = int(input_variables[0])
text = input_variables[1]

no_of_windows = len(text) - n + 1

for i in range(no_of_windows):
	print(text[i:(i+n)])