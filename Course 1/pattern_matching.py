def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    length = len(Pattern)
    for idx, char in enumerate(Genome):
        if Pattern[0] == char:
            if Pattern[1:] == Genome[idx+1:idx+length]:
                positions.append(idx)
        else:
            pass
    return positions

# On the following line, a variable called Text that is equal to the oriC region from T petrophila
Text = "aactctatacctcctttttgtcgaatttgtgtgatttatagagaaaatcttattaactgaaactaaaatggtaggtttggtggtaggttttgtgtacattttgtagtatctgatttttaattacataccgtatattgtattaaattgacgaacaattgcatggaattgaatatatgcaaaacaaacctaccaccaaactctgtattgaccattttaggacaacttcagggtggtaggtttctgaagctctcatcaatagactattttagtctttacaaacaatattaccgttcagattcaagattctacaacgctgttttaatgggcgttgcagaaaacttaccacctaaaatccagtatccaagccgatttcagagaaacctaccacttacctaccacttacctaccacccgggtggtaagttgcagacattattaaaaacctcatcagaagcttgttcaaaaatttcaatactcgaaacctaccacctgcgtcccctattatttactactactaataatagcagtataattgatctga"

# On the following line, a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.
count_1 = len(PatternMatching("ATGATCAAG" , Text))

# On the following line, a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text. 
count_2 = len(PatternMatching("CTTGATCAT" , Text))


# Finally, sum of count_1 and count_2
print(count_1 + count_2)