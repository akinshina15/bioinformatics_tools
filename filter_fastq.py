from scripts.seq_quality_check import gc_content, calculate_average_quality


def filter_fastq(seqs: dict[str, tuple[str, str]],
                 gc_bounds: tuple[float, float],
                 length_bounds: tuple[int, int],
                 quality_threshold: int) -> dict[str, tuple]:

    if isinstance(gc_bounds, float):
        gc_bounds = (0, gc_bounds)

    if isinstance(length_bounds, int):
        length_bounds = (0, length_bounds)

        filtered_seqs = {}

        for name, (sequence, enc_quality) in seqs.items():
            length = len(sequence) 
            gc = gc_content(sequence)
            avg_quality = calculate_average_quality(enc_quality)

            if (length_bounds[0] <= length <= length_bounds[1] and
                    gc_bounds[0] <= gc <= gc_bounds[1] and
                    avg_quality >= quality_threshold):
                filtered_seqs[name] = (sequence, enc_quality)

        return filtered_seqs
