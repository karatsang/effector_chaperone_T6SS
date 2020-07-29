import sys
import csv
import os
import glob
from Bio import SeqIO
TMlist=[]
TMdict={}
with open("phobius_result.txt",'r') as hmmsearch_file:
	for line in hmmsearch_file:
		target_info=[]
		if line.startswith("ID"):
			linenospace =line.split()
			ID = linenospace[1]
		if line.startswith("FT"):
			linenospace =line.split()
			if linenospace[1] == "TRANSMEM":
				TMlist.append(ID)
				TMdict.setdefault(ID,[]).append(linenospace)
				# print(TMlist)

for k,v in TMdict.items():
	if len(v)==1:
		for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm.fasta", "fasta"):
			fasta_header = str(seq_record.id)
			fasta_sequence = str(seq_record.seq).upper()
			if k==fasta_header:
				with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_phobius.fasta", "a+") as output_file:
					output_file.write(">1reg" + fasta_header + "\n" + fasta_sequence + "\n")
	if len(v)==2:
		if int(v[1][3]) - int(v[0][3]) < 25:
			for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm.fasta", "fasta"):
				fasta_header = str(seq_record.id)
				fasta_sequence = str(seq_record.seq).upper()
				if k==fasta_header:
					with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_phobius.fasta", "a+") as output_file:
						output_file.write(">1reg" + fasta_header + "\n" + fasta_sequence + "\n")
		if int(v[1][3]) - int(v[0][3]) > 25:
			for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm.fasta", "fasta"):
				fasta_header = str(seq_record.id)
				fasta_sequence = str(seq_record.seq).upper()
				if k==fasta_header:
					with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_phobius.fasta", "a+") as output_file:
						output_file.write(">2reg" + fasta_header + "\n" + fasta_sequence + "\n")
	if len(v)==3:
		if int(v[2][3]) - int(v[1][3]) > 25:
			for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm.fasta", "fasta"):
				fasta_header = str(seq_record.id)
				fasta_sequence = str(seq_record.seq).upper()
				if k==fasta_header:
					with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_phobius.fasta", "a+") as output_file:
						output_file.write(">2reg" + fasta_header + "\n" + fasta_sequence + "\n")

	if len(v)==4:
		if int(v[2][3]) - int(v[1][3]) > 25:
			for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm.fasta", "fasta"):
				fasta_header = str(seq_record.id)
				fasta_sequence = str(seq_record.seq).upper()
				if k==fasta_header:
					with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_phobius.fasta", "a+") as output_file:
						output_file.write(">2reg" + fasta_header + "\n" + fasta_sequence + "\n")
	if len(v)==5:
		if int(v[2][3]) - int(v[1][3]) > 25:
			for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm.fasta", "fasta"):
				fasta_header = str(seq_record.id)
				fasta_sequence = str(seq_record.seq).upper()
				if k==fasta_header:
					with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_phobius.fasta", "a+") as output_file:
						output_file.write(">2reg" + fasta_header + "\n" + fasta_sequence + "\n")
for seq_record in SeqIO.parse("notm_3reg_tmhmm_seq.fasta", "fasta"):
	fasta_header = str(seq_record.id)
	fasta_sequence = str(seq_record.seq).upper()
	if fasta_header not in TMdict:
		with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_tmhmm_NOphobius.fasta", "a+") as output_file:
			output_file.write(">" + fasta_header + "\n" + fasta_sequence + "\n")
# 	else:
# 		print(fasta_header)
# 		print(fasta_header)
# 		with open("first300aa_strictfilter_more100aa_last150aa_70_PAAR_phobius.fasta", "a+") as output_file:
# 			output_file.write(">" + fasta_header + "\n" + fasta_sequence + "\n")
