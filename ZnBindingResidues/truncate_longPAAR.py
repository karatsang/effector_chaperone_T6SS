import sys
import csv
import os
import glob
import ast 
from Bio import SeqIO
import re

"""

To truncate any prePAAR sequences to become only 300 amino acids long

Requires the following files:
Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR.fasta

Creates: 
Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa.fasta

"""


with open("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR.fasta", 'r') as eff_file:
	for seq_record in SeqIO.parse(eff_file, "fasta"):
		header=str(seq_record.id)
		sequence = str(seq_record.seq).upper()
		if len(sequence) > 299:
			with open("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa.fasta", "a+") as output_file:
				output_file.write(">"+ header + "\n" + sequence[0:299] + "\n")
		else:
			with open("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa.fasta", "a+") as output_file:			
				output_file.write(">"+ header + "\n" + sequence + "\n")

