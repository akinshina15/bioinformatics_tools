from scripts.seq_quality_check import count_gc, calculate_average_quality
from scripts.fastq_modules import read_fastq_to_dict

"""
This function will filter your sequences in a given FastQ file
according to the settings provided.
You may set the bounds for GC content, sequence length
as well as the the quality threshold.
"""

seqs = read_fastq_to_dict()


def filter_fastq(seqs: dict[str, tuple[str, str]],
                 gc_bounds: tuple[float, float] = (0, 100),
                 length_bounds: tuple[int, int] = (0, 2**32),
                 quality_threshold: int = 0) -> dict[str, tuple]:

    if not isinstance(gc_bounds, tuple):
        gc_bounds = (0.0, float(gc_bounds))
    if not isinstance(length_bounds, tuple):
        length_bounds = (0, int(length_bounds))

    filtered_seqs = {}

    for seq_id, (sequence, quality) in seqs.items():
        length = len(sequence)
        gc = count_gc(sequence)
        avg_quality = calculate_average_quality(quality)

        if (length_bounds[0] <= length <= length_bounds[1] and
                gc_bounds[0] <= gc <= gc_bounds[1] and
                avg_quality >= quality_threshold):
            filtered_seqs[seq_id] = (sequence, quality)

    return filtered_seqs
