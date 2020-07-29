import sys
import csv
import os
import glob
from Bio import SeqIO
all_targets={}
# for file in sorted(glob.glob("*.domtblout")):
# 	sample=(file.replace(".domtblout",""))
list_domscores=float()

with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_PAAR_4.domtblout",'r') as hmmsearch_file:
	for line in hmmsearch_file:
		target_info=[]
		if not line.startswith("#"):
			linenospace =line.split()
			# targetname=(linenospace[0])
			# tlen=(linenospace[2])
			#number of domains per target
			if int(linenospace[10]) == 1:
				if float(linenospace[13]) >= 40:

					# print(linenospace[10])
					target_name=linenospace[0]
					seq_evalue=linenospace[6]
					seq_score=linenospace[7]
					dom_ievalue=linenospace[12]
					dom_score=linenospace[13]
					# accuracy=linenospace[21]
					# target_start=(linenospace[23])
					# target_stop=(linenospace[25])
					# target_info.append(target_name)
					target_info.append(seq_evalue)
					target_info.append(seq_score)					
					target_info.append(dom_ievalue)
					target_info.append(dom_score)
					# target_info.append(accuracy)
					# target_info.append(target_start)
					# target_info.append(target_stop)
					# target_info.append(sample)											

			#number of domains per target
			elif int(linenospace[10]) > 1:
				if float(linenospace[13]) >= 40:
					# print(linenospace[10])
					target_name=linenospace[0]
					seq_evalue=linenospace[6]
					seq_score=linenospace[7]
					dom_ievalue=linenospace[12]
					dom_score=linenospace[13]
					# accuracy=linenospace[21]
					# target_start=(linenospace[23])
					# target_stop=(linenospace[25])
					# target_info.append(target_name)
					target_info.append(seq_evalue)
					target_info.append(seq_score)					
					target_info.append(dom_ievalue)
					target_info.append(dom_score)
					# target_info.append(accuracy)
					# target_info.append(target_start)
					# target_info.append(target_stop)
					# target_info.append(sample)										


			if (target_info):
				all_targets.setdefault(target_name,[]).append(target_info)

# print(all_targets)
# print(len(all_targets))
numbPAAR=[]
gotit=[]
gotit2=[]
# all_targets_domcount={}
for k,v in all_targets.items():
	numbPAAR.append(len(v))
	for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_NOPAAR_3.fasta", "fasta"):
		header = str(seq_record.id)
		sequence = str(seq_record.seq).upper()

		if k in header:
			with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_PAAR_4.fasta", "a+") as output_file:
				output_file.write(">" + header + "\n" + sequence + "\n")
				gotit.append(header)
for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_NOPAAR_3.fasta", "fasta"):
	header = str(seq_record.id)
	sequence = str(seq_record.seq).upper()
	if header not in gotit:
		if header not in gotit2:
			with open("Full_fasta_60aa_PA0093_query_6iterations_species_more100_CDHIT95_NOPAAR_4.fasta", "a+") as output_file:
				output_file.write(">" + header + "\n" + sequence + "\n")
				gotit2.append(header)

print(sum(numbPAAR))


