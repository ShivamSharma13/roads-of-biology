# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
def Count(Motifs):
	k = len(Motifs[0])
	count = {symbol:[0]*k for symbol in "ACGT"}
	for row in Motifs:
			 for idx, char in enumerate(row):
				 count[char][idx] += 1
	return count

def Profile(Motifs):
	t = len(Motifs)
	k = len(Motifs[0])
	profile = {symbol:[0]*k for symbol in "ACGT"}
	for row in Motifs:
		for idx, char in enumerate(row):
			profile[char][idx] += (1/t)
	return profile

def Score(Motifs):
	score = 0
	t = len(Motifs)
	k = len(Motifs[0])
	count = Count(Motifs)
	for i in range(k):
		max_c = 0
		for symbol in "ATGC":
			if count[symbol][i] > max_c:
				max_c = count[symbol][i]
		score += (t - max_c)
	return score

def Consensus(Motifs):
	k = len(Motifs[0])
	count = Count(Motifs)
	consensus = ""
	for j in range(k):
		current_max = 0
		frequentSymbol = ""
		for symbol in "ACGT":
			if count[symbol][j] > current_max:
				current_max = count[symbol][j]
				frequentSymbol = symbol
		consensus += frequentSymbol
	return consensus

# Then copy your ProfileMostProbableKmer(Text, k, Profile) and Pr(Text, Profile) functions here.

def Pr(Text, Profile):
	'''
	Input: 
		ACGGGGATTACC
		0.2 0.2 0.0 0.0 0.0 0.0 0.9 0.1 0.1 0.1 0.3 0.0
		0.1 0.6 0.0 0.0 0.0 0.0 0.0 0.4 0.1 0.2 0.4 0.6
		0.0 0.0 1.0 1.0 0.9 0.9 0.1 0.0 0.0 0.0 0.0 0.0
		0.7 0.2 0.0 0.0 0.1 0.1 0.0 0.5 0.8 0.7 0.3 0.4

	Output:
		0.0008398080000000002
	'''

	#Find probability 
	product = 1
	for idx, char in enumerate(Text):
		product *= Profile[char][idx]
	return product

def ProfileMostProbableKmer(text, k, profile):
	'''
	Input:
		ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
		5
		0.2 0.2 0.3 0.2 0.3
		0.4 0.3 0.1 0.5 0.1
		0.3 0.3 0.5 0.2 0.4
		0.1 0.2 0.1 0.1 0.2

	Output:
		CCGAG

	Profile:
		{'A': [0.2, 0.2, 0.3, 0.2, 0.3], 
		'C': [0.4, 0.3, 0.1, 0.5, 0.1], 
		'G': [0.3, 0.3, 0.5, 0.2, 0.4], 
		'T': [0.1, 0.2, 0.1, 0.1, 0.2]}

	'''
	no_of_windows = len(text) - k + 1
	
	#CAGCG taken as default from a specific test case; no relevance as such.
	#Probability must be set to -1 and not 0, as it'll break the tie cases.
	#max_prob = ['CAGCG', -1]
	
	max_prob = ['', -1]
	


	for i in range(no_of_windows):
		prob = Pr(text[i:i+k], profile)
		if prob > max_prob[1]:
			max_prob[0] = text[i:i+k] 
			max_prob[1] = prob
	   
	return max_prob[0]
	

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearch(Dna, k, t):
	BestMotifs = []
	
	#Set the first k-mers of all dna strings as default for BestMotif.
	for i in range(0, t):
		BestMotifs.append(Dna[i][0:k])

	#Iterating over 1st DNA string, trying to see which other k-mer matches the best. 
	#Greedy Approach.
	n = len(Dna[0])
	for i in range(n-k+1):
		Motifs = []
		#Add k-mer from first string.
		Motifs.append(Dna[0][i:i+k])
	   
		#Starting from 1, becuase first is already added above.
		for j in range(1, t):
			P = Profile(Motifs[0:j])
			Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
	
		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs
