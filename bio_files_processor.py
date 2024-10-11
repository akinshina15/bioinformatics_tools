def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    """
    Converts multiple-line FASTA file into single-line format
    """
    if output_fasta is None:
        output_fasta = input_fasta.rsplit(".", 1)[0] + "_one_line.fasta"

    with open(input_fasta, "r") as file, open(output_fasta) as out_file:
        sequence_id = None
        sequence = ""

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_id is not None:
                    out_file.write(f"{sequence_id}\n{sequence}\n")
                sequence_id = line
                sequence = ""
            else:
                sequence += line
