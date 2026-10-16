sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]
lengths = []
long_sequences = []
counter_ATG = 0
CODON_LENGTH = 3

for seq in sequences:
    C = seq.count("C")
    G = seq.count("G")
    GC = G + C
    percent_GC = GC/len(seq) * 100
    print("GC content - ", round(percent_GC, 2))
    print(seq, len(seq))
    lengths.append(len(seq))
    if seq.startswith("ATG"):
        counter_ATG = counter_ATG + 1
    if len (seq) > 5:
        long_sequences.append(seq)

print(sum(lengths) / len(lengths))
print(counter_ATG)
print(*long_sequences)

print("******")
longest_sequence = sequences[lengths.index(max(lengths))]
for i in range(0, len(longest_sequence), CODON_LENGTH):
    print(longest_sequence[i:i+CODON_LENGTH])

