def gc_content(sequence):
    """ This function calculates the sequence GC content in percent.
    Simply feed the sequence and see how GC-rich it is! """
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    gc_total = len(sequence)

    if gc_total == 0:
        return 0.0
    return (gc_count / gc_total) * 100
