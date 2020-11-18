import sys
import csv
import os
import glob
from Bio import SeqIO
all_targets={}
# for file in sorted(glob.glob("*.domtblout")):
# 	sample=(file.replace(".domtblout",""))
list_domscores=float()
tar=[]
with open("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa_HMM.domtblout",'r') as hmmsearch_file:
	for line in hmmsearch_file:
		target_info=[]
		if not line.startswith("#"):
			linenospace =line.split()
			# targetname=(linenospace[0])
			# tlen=(linenospace[2])
			#number of domains per target
			# if int(linenospace[10]) == 1:
			# if float(linenospace[13]) >= 70:

			# print(linenospace[10])
			target_name=linenospace[0]

			env_start=linenospace[19]
			env_stop=linenospace[20]
		
			target_info.append(env_start)
			target_info.append(env_stop)
			# target_info.append(accuracy)
			# target_info.append(target_start)
			# target_info.append(target_stop)
			# target_info.append(sample)											

			#number of domains per target
			# elif int(linenospace[10]) > 1:
			# 	# if float(linenospace[13]) >= 70:
			# 		target_name=linenospace[0]
			# 		env_start=linenospace[19]
			# 		env_stop=linenospace[20]
				
			# 		target_info.append(env_start)
			# 		target_info.append(env_stop)
					# target_info.append(accuracy)
					# target_info.append(target_start)
					# target_info.append(target_stop)
					# target_info.append(sample)
			# tar.append(target_info)					

			all_targets.setdefault(target_name,[]).append(target_info)
			# else:
			# 	print(target_name)

# print(len(all_targets))
numbPAAR=[]
gotit=[]
gotit2=[]

for k,v in all_targets.items():
	for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa.fasta", "fasta"):
		header = str(seq_record.id)
		sequence = str(seq_record.seq).upper()
		if k in header:
			with open("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa_HMM.fasta", "a+") as output_file:
				output_file.write(">" + header + "\n" + sequence[int(v[0][0]):int(v[0][1])] + "\n")
				gotit.append(header)

for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa.fasta", "fasta"):
	header = str(seq_record.id)
	sequence = str(seq_record.seq).upper()
	if header not in gotit:
		with open("Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_trunc300aa_HMM.fasta", "a+") as output_file:
			output_file.write(">" + header + "\n" + sequence + "\n")
				# gotit.append(header)			


# print(sum(numbPAAR))


