
def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta=None) -> None:
    """
    Converts multiple-line FASTA file into single-line format and creates
    a new output file if no output file is given
    """
    if output_fasta is None:
        output_fasta = input_fasta.rsplit(".", 1)[0] + "_one_line.fasta"

    with open(input_fasta, "r") as file, open(output_fasta, "w") as out_file:
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


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    This function parses BLAST results from a BLAST search text file into
    a new file that contains only the top hit protein name results
    for each query in the original file.
    """

    with open(input_file, "r") as file, open(output_file, "w") as out_file:
        values: set[str] = set()

        lines: list[str] = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("Sequences producing significant alignments:"):
                continue
            if line == "":
                continue
            if "Description" in line:
                next_line: str = lines[i + 1].strip()
                parts: list[str] = next_line.split()
                protein: str = ' '.join(parts[:-10])
                values.add(protein)

        sorted_values: list[str] = sorted(values)

        for value in sorted_values:
            out_file.write(value + "\n")
