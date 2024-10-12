# Bioinformatics tools

Welcome! Here you will find a small set of tools for you **nucleic acid** sequence analysis.

### Download

Run
~~~
git clone https://github.com/akinshina15/bioinformatics_tools
cd bioinformatics_tools
~~~

## DNA and RNA tools

These tools in function `run_dna_rna_tools` will let you perform *in silico* conversion of any given sequence that is either DNA or RNA

### Usage

Run 
~~~
python dna_rna_tools.py
~~~

and enter you sequence, followed by one of the actions: `transcribe` , `reverse`, `complement` , `reverse_complement`

## Filter FastQ

This tool will filter off the sequences in your FASTQ file that are below your desired standards. You may state your quality threshold, the boundaries for the length of sequence and its GC-content. Otherwise, the parameters are set to default.

*N.B.* The function in this script works only when the modules in `scripts` are in the same direcroty as the script. Do not move nor delete the module.

### Usage

Run 
~~~
python filter_fastq.py
~~~

Put your FastQ file in the same directory as the tool and run the function to obtain filtered reads.


##  Bioligical files processor

The file `bio_files_processor.py` contains the following functions:

 1. `convert_multiline_fasta_to_oneline`

This function reads a multi-line FASTA file and converts it into a single line format for easier handling and analysis. It outputs the result into a new FASTA file, and if no output filename is provided, it automatically generates one.

Parameters:
`input_fasta`: The path to the input FASTA file.
`output_fasta` (optional): The path for the output file. If not specified, a new filename is created automatically.

#### Usage

~~~
convert_multiline_fasta_to_oneline("input_sequences.fasta")
~~~

This will create a file named `input_sequences_one_line.fasta` in the same directory.

 2. `parse_blast_output`

This function parses BLAST results from a BLAST search text file into a new file that contains only the top hit protein name results for each query stated the original BLAST file.

Parameters
`input_file`: The path to the input BLAST results file.
`output_file`: The path for the output file containing the top hit protein names.

#### Usage

~~~
parse_blast_output("blast_results.txt", "top_hits.txt")
~~~

Dependencies:
python3


*Please be aware these tools undergo testing and are subject to fixes and changes.*

Enjoy!
