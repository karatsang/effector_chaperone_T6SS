import sys
import csv
import os
import glob
import ast
from Bio import SeqIO
import re

"""

To identify short PAAR sequences, we downloaded all Pfam database's PAAR motif sequences, then only included those with ONE PAAR motif architecture. Pfam's database was accessed in June 2020.

Requires the following files:
PF05488_full_length_sequences.fasta - FASTA file with all sequences from Pfam database (PAAR motif (PF05488), http://pfam.xfam.org/family/PF05488#tabview=tab1)
shortPAAR_motif.tsv - TSV file with IDs of sequences that only contain one PAAR motif architecture from the Pfam database

Creates:
shortPAAR_PF05488_full_length_sequences.fasta

"""


with open("shortPAAR_PF05488_full_length_sequences_prePAAR_less250aa.fasta", 'r') as eff_file:
	for seq_record in SeqIO.parse(eff_file, "fasta"):
		header=str(seq_record.id)
		sequence = str(seq_record.seq).upper()
		with open("shortPAAR_PF05488_full_length_sequences_prePAAR_less250aa_20.fasta", "a+") as output_file:
			output_file.write(">"+ header + "\n" + sequence[19::] + "\n")
