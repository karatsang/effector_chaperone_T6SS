#Run in directory with fastas

import sys
import csv
import os
import glob
import ast 
from Bio import SeqIO
import re
from collections import Counter
import glob


print("FIRST 100 AA")

unique_fasta_seq=[]
unique_fasta_header=[]
for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species.fasta", "fasta"):
	fasta_header = str(seq_record.id)
	fasta_sequence = str(seq_record.seq).upper()
	if len(fasta_sequence)>100:
 		with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100.fasta", "a+") as output_file:
 			output_file.write(">" + fasta_header + "\n" + fasta_sequence + "\n")
