import os


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    """
    Converts multiple-line FASTA file into single-line format
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


def parse_blast_output(input_file, output_file):
    """
    
    """

    with open(input_file, "r") as file, open(output_file, "w") as out_file:
        values = set()

        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("Sequences producing significant alignments:"):
                continue
            if line == "":
                continue
            if "Description" in line:
                next_line = lines[i + 1].strip()
                parts = next_line.split()
                protein = ' '.join(parts[:-10])
                values.add(protein)

        sorted_values = sorted(values)

        for value in sorted_values:
            out_file.write(value + "\n")
