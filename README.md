# Bioinformatics tools

Welcome! Here you will find a small set of tools for you **nucleic acid** sequence analysis.

### Download

Run
~~~bash
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
Mind the *types* of input into the function when running. 

*N.B.* The function in this script works only when the modules in `scripts` are in the same direcroty as the script. Do not move nor delete the module.

### Usage

Run 
~~~
filter_fastq.py
~~~

enter your sequence_id, sequence, Phred score in the format of dict.

