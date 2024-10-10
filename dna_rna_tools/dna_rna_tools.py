def run_dna_rna_tools(*args):
    *sequence, procedure = args

    if procedure == 'transcribe':
        return apply_to_sequences(sequence, transcribe)
    elif procedure == 'reverse':
        return apply_to_sequences(sequence, reverse)
    elif procedure == 'complement':
        return apply_to_sequences(sequence, complement)
    elif procedure == 'reverse_complement':
        return apply_to_sequences(sequence, reverse_complement)
    else:
        return None


def valid_rna(sequence):
    if set(sequence).issubset({'A', 'U', 'G', 'C', 'a', 'u', 'g', 'c'}):
        return True
    else:
        return False


def valid_dna(sequence):
    return set(sequence).issubset({'A', 'T', 'G', 'C', 'a', 't', 'g', 'c'}):

def apply_to_sequences(sequences, procedure):
    return [procedure(seq) for seq in sequences] if sequences else ''


def transcribe(sequence):
    if valid_dna:
        return sequence.replace('T', 'U').replace('t', 'u')
    else:
        print("Your input is not a valid DNA sequence")


def reverse(sequence):
    return sequence[::-1]


def complement(sequence):
    if valid_dna(sequence):
        complements = {"A": "T", "a": "t", "T": "A", "t": "a",
                       "C": "G", "c": "g", "G": "C", "g": "c"}
        return "".join(complements[base] for base in sequence)

    elif valid_rna(sequence):
        complements = {"A": "U", "a": "u", "U": "A", "u": "a",
                       "C": "G", "c": "g", "G": "C", "g": "c"}
        return "".join(complements[base] for base in sequence)
    else:
        print("Invalid sequence")


def reverse_complement(sequence):
    return reverse(complement(sequence))
