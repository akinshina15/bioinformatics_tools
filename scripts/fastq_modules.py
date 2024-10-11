import os

wd = os.path.dirname('test.fastq')
file_path = os.path.join(wd, 'test.fastq')


def read_fastq_to_dict(file_path):
    """
    This function reads a FastQ file and converts it into a dictionary format
    where its key is a seq_id, and values are a tuple of sequence and quality.
    After running the output will be prepared for using with
    "filter_fastq.py" function
    """
    fastq_dict = {}

    with open(file_path, 'r') as file:
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
