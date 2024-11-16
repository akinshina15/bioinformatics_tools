def count_gc(sequence: str) -> float:
    """
    This function calculates the sequence GC content in percent.
    Simply feed the sequence and see how GC-rich it is!
    """
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    gc_total = len(sequence)

    if gc_total == 0:
        return 0.0
    return (gc_count / gc_total) * 100


def ascii_to_phred(phred_str: str) -> list:
    """This function converts a string with encoded quality positions
    into a list of numbers
    """
    return [ord(char) - 33 for char in phred_str]


def calculate_average_quality(enc_quality: str) -> float:
    """ " This function converts Phred quality score into ASCII format
    and returns its value
    """
    quality_scores = ascii_to_phred(enc_quality)

    if not quality_scores:
        return 0.0

    average_quality = sum(quality_scores) / len(quality_scores)
    return average_quality
