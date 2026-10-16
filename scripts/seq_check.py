seq = "ATGAAATTTAAAATTTGCGTGCGTGACGTACGTTAACGTACGTTAACGTACGTTAAA"

C = seq.count("C")
G = seq.count("G")
GC = G + C
percent_GC = GC/len(seq) * 100

if len(seq) < 30:
    print("too short")
elif "N" in seq:
    print("contain unknown bases")
elif seq.startswith("ATG") and len(seq) % 3 == 0:
    print("possible ORF")
elif percent_GC > 60:
    print("GC rich")
elif percent_GC < 40:
    print("AT rich")
else:
    print("balanced")





