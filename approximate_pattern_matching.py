def ApproximatePatternCount(Pattern, Text, d):
    positions = [] # initializing list of positions
    n = len(Text)
    l = len(Pattern)
    for i in range(n-l+1):
        if HammingDistance(Text[i:i+l], Pattern, d):
            positions.append(i)
    return len(positions)


# Hamming distance function.
def HammingDistance(p, q, limit):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    if distance <= limit:
        return True
    else:
        return False


in_string = 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
core_pattern = 'GTGCCG'
limit = 3

result = ApproximatePatternCount(core_pattern, in_string, limit)
print(result)