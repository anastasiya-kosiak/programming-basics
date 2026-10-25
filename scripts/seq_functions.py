def gc_content(seq):
    gc_count = 0
    for base in seq:
        if base == "G" or base == "C":
            gc_count = gc_count + 1
    if len(seq) == 0:
        return 0
    percentage = gc_count / len(seq) * 100
    return round(percentage, 2)


def reverse_complement(seq):
    result = ""
    for base in seq:
        if base == "A":
            completement = "T"
        elif base == "T":
            completement = "A"
        elif base == "G":
            completement = "C"
        elif base == "C":
            completement = "G"
        else:
            completement = "N"
        result = completement + result
    return result


def is_usable(seq, min_length=30):
    if len(seq) < min_length:
        return False
    for base in seq:
        if base == "N":
            return False
    return True

def first_atg(seq):
    for i in range(len(seq) - 2):
        if seq[i] == "A" and seq[i + 1] == "T" and seq[i + 2] == "G":
            return i
    return -1


def test(seq):
    print("Sequence:", seq)
    print("GC content:", gc_content(seq), "%")
    print("Reverse complement:", reverse_complement(seq))
    print("Usable:", is_usable(seq))
    print("First ATG at:", first_atg(seq))


def count_bases(seq):
    counts = {"A": 0, "T": 0, "G": 0, "C": 0, "N": 0}
    for base in seq:
        counts[base] = counts[base] + 1
    return counts


seq1 = "ATGCGCGATATCGCGTAGCTAGCTAGGCATGC"
seq2 = "TTAGGCATGCC"
seq3 = "GATTACANNNGATTACAGATTACAGATTACAGATTACA"
seq4 = "ATGCGCATG";

test(seq1)
test(seq2)
test(seq3)
print(count_bases(seq4))