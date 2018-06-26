#Only consider the leaving and arriving characters from the window.
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    extended_genome = Genome + Genome[0:n//2]
    window = extended_genome[0:n//2]
    l = len(window)
    array[0] = PatternCount(symbol, window)
    for i in range(1,n):
        array[i] = array[i-1]
        if extended_genome[i-1] == symbol:
            array[i] = array[i] - 1
        if extended_genome[i-1+l] == symbol:
            array[i] = array[i-1] + 1
            
    return array

def PatternCount(symbol, Genome):
    count = 0 # output variable
    # your code here
    for i in range(len(Genome) - len(symbol) + 1):
        if symbol in Genome[i:i+len(symbol)]:
           count = count + 1
    return count


in_string = 'AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
symbol = 'CC'

result = FasterSymbolArray(in_string, symbol)
print(result)