import numpy as np

outputs = []

def recursive_change(amount, change, possibles):
	if amount == 0:
		return 1
	if amount < 0:
		return 0
	
	for c in change:
		possibles.append(c)
		result = recursive_change((amount - c), change, possibles)
		
		if result == 1:
			'''
			Handling the python list reference issue,
			and checking if the possible combination is already present in the output.
			'''
			target = list(possibles)
			target.sort()
			if target not in outputs:
				outputs.append(target)
			del target
			possibles.pop()
		
		if result == 0:
			possibles.pop() 
		
		'''
		print('After recursion, result = {} ----'.format(result), 
			'Amount = {} ---- '.format(amount), 
			'Possible List = {} ---- '.format(possibles),   
			'Outputs = {}'.format(outputs))
		'''
	return 0
		
if __name__ == '__main__':
	money = 10
	change = [5,4,1]
	recursive_change(money, change, [])
	for out in outputs:
		print(out, np.array(out).sum())