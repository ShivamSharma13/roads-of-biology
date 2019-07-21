import numpy as np

min_number_coins_required = 1000000
coin_seq = []
memorizer = {'0' : 0}

def recursive_change_top_bottom(amount, change, possibles):
	if amount == 0:
		return True
	if amount < 0:
		return False
	
	for c in change:
		possibles.append(c)
		result = recursive_change_top_bottom((amount - c), change, possibles)
		
		if result == True:
			'''
			Handling the python list reference issue,
			and checking if the possible combination is already present in the output.
			'''
			target = list(possibles)
			target.sort()
			if target not in coin_seq:
				coin_seq.append(target)
			possibles.pop()
		
		if result == False:
			possibles.pop() 
		
		'''
		print('After recursion, result = {} ----'.format(result), 
			'Amount = {} ---- '.format(amount), 
			'Possible List = {} ---- '.format(possibles),   
			'Outputs = {}'.format(coin_seq))
		'''

	#For loop has ended. All possible nodes have been traversed at this level.
	#Going a level up, by returning False.
	return False


def recursive_change_bottom_top(total_money, amount, change, possibles):
	global min_number_coins_required
	if amount == total_money:
		return True
	elif amount > total_money:
		return False

	for c in change:
		possibles.append(c)
		result = recursive_change_bottom_top(total_money, amount+c, change, possibles)		
		if result == True:

			if len(possibles) < min_number_coins_required:
				min_number_coins_required = len(possibles)
				memorizer[str(amount)] = min_number_coins_required
			possibles.pop()
		
		if result == False:
			possibles.pop() 
		
		'''
		print('After recursion, result = {} ----'.format(result), 
			'Amount = {} ---- '.format(amount), 
			'Possible List = {} ---- '.format(possibles),   
			'Outputs = {}'.format(coin_seq))
		'''
	#For loop has ended. All possible nodes have been traversed at this level.
	#Going a level up, by returning False.
	return False			


def recursive_change_dynamic_programming(amount_in_recursion_stack, change):
	if amount_in_recursion_stack < 0:
		#Amount has gone negative, so no way out. Abort!!
		return None
	if str(amount_in_recursion_stack) in memorizer:
		return memorizer[str(amount_in_recursion_stack)]
	
	#Result is set to very high number, so as to see which m(amount_in_recursion_stack - c) is the smallest.
	result = 10000000
	for c in change:
		possible = recursive_change_dynamic_programming(amount_in_recursion_stack-c, change)
		if possible is not None and possible < result:
			result = possible

	#Storing the result into memorizer.
	memorizer[str(amount_in_recursion_stack)] = result + 1
	
	return result + 1


if __name__ == '__main__':
	total_money = 19165
	start_amount = 0
	change = [22,21,5,3,1]
	#recursive_change_top_bottom(total_money, amount, change, [])
	#recursive_change_bottom_top(total_money, start_amount, change, [])	
	recursive_change_dynamic_programming(total_money, change)
	print(memorizer[str(total_money)])
	#print(min_number_coins_required)


