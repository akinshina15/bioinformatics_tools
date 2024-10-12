import os

file_path = os.path.join(os.getcdw(), "*.fastq")


def read_fastq_to_dict(file_path):
    """
    This function reads a FastQ file and converts it into a dictionary format
    where its key is a seq_id, and values are a tuple of its sequence and quality.

    After running the output will be prepared for using with
    "filter_fastq.py" function
    """
    fastq_dict = {}

    with open(file_path, "r") as file:
        while True:
            seq_id = file.readline().strip()
            if not seq_id:
                break

        sequence = file.readline().strip()
        file.readline()
        quality = file.readline().strip()
        seq_id = seq_id[1:]
        fastq_dict[seq_id] = [sequence, quality]

    return fastq_dict


def write_filtered_fastq(sequences, output_fastq):
    """
    This function writes filtered FastQ sequences into a new FastQ file
    and creates a directory if it does not exist yet
    """
    filtered_dir = "filtered"
    if not os.path.exists(filtered_dir):
        os.makedirs(filtered_dir)

    output_file_path = os.path.join(filtered_dir, output_fastq)

    if os.path.exists(output_file_path):
        confirm = input(
            f"File '{output_file_path}' already exists. Do you wish to re-write it? (y/n)"
        )
        if confirm.lower() != "y":
            print("Writing canceled")
            return

    with open(output_file_path, "w") as fastq_file:
        for seq_id, (sequence, quality) in sequences.items():
            fastq_file.write(f"@{seq_id}\n")
            fastq_file.write(f"{sequence}\n")
            fastq_file.write("+\n")
            fastq_file.write(f"{quality}\n")
