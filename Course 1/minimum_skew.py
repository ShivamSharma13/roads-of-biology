def MinimumSkew(Genome):
    positions = [] # output variable
    skew = SkewArray(Genome)
    min_i = min(skew)
    while True:
        if min_i in skew:
            index = skew.index(min_i)
            positions.append(index)
            skew.__delitem__(index)
        else:
            break            
    return positions

operations = {'C' : -1, 'A' : 0, 'T' : 0, 'G' : 1}
def SkewArray(Genome):
    '''
    skew[0] = 0, pattern's 1st character--at pattern[0]--has its skew at skew[1].
    '''
    skew = [0,]
    for idx, char in enumerate(Genome):
        result = operations[char] + skew[idx]
        skew.append(result)
    return skew


genome = 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
result = MinimumSkew(genome)
print(result)