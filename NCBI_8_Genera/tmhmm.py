import sys
import csv
import os
import glob
from Bio import SeqIO

tm={}
with open("tmhmm_result.txt",'r') as hmmsearch_file:
	for line in hmmsearch_file:
		target_info=[]
		if not line.startswith("#"):
			linenospace =line.split()
			# print(linenospace)
			if (linenospace[2]) == "TMhelix":
				tm_distance=[]
				tm_distance.append(linenospace[3])
				tm_distance.append(linenospace[4])
				tm.setdefault(linenospace[0],[]).append(tm_distance)
# tmkeys=[]
# for x in tm.keys():
# 	tmkeys.append(x)
print(tm)
indict=[]
with open("all_effector_wchap_genus_more100aa_CDHIT95.fasta", 'r') as fasta:
	count=0
	for seq_record in SeqIO.parse(fasta, "fasta"):
		sequence = str(seq_record.seq).upper()
		with open("all_effector_wchap_genus_more100aa_CDHIT95_tmhmm.fasta", 'a+') as new_file:
			for key,value in tm.items():
				if str(seq_record.id)[0:250] in key[0:250]:
					indict.append(str(seq_record.id)[0:250])
					if (len(value)) == 1:
						new_file.write(">" + "1reg_" + key + "\n" + sequence + "\n")

					elif len(value) == 2:
						if int(value[1][0]) - int(value[0][1]) <= 25:
							new_file.write(">" + "1reg_" + seq_record.id + "\n" + sequence + "\n")
						elif int(value[1][0]) - int(value[0][1]) > 25:
							new_file.write(">" + "2reg_" + key + "\n" + sequence + "\n")

					elif len(value) == 3:
						if int(value[1][0]) - int(value[0][1]) <= 25:
							if int(value[2][0]) - int(value[1][1]) > 25:
								new_file.write(">" + "2reg_" + key + "\n" + sequence + "\n")
							elif int(value[2][0]) - int(value[1][1]) <= 25:
								new_file.write(">" + "1reg_" + key + "\n" + sequence + "\n")
						elif int(value[2][0]) - int(value[1][1]) <= 25:
							if int(value[1][0]) - int(value[0][1]) > 25:
								new_file.write(">" + "2reg_" + key + "\n" + sequence + "\n")
					elif len(value) == 4:
						if int(value[1][0]) - int(value[0][1]) <= 25:
							if int(value[3][0]) - int(value[2][1]) <= 25:
								new_file.write(">" + "2reg_" + key + "\n" + sequence + "\n")
							elif int(value[3][0]) - int(value[2][1]) > 25:
								new_file.write(">" + "3reg_" + key + "\n" + sequence + "\n")
							else:
								print(tm[seq_record.id])
					elif len(value) == 5:
						if int(value[1][0]) - int(value[0][1]) <= 25:
							if int(value[2][0]) - int(value[1][1]) <= 25:
								if int(value[3][0]) - int(value[2][1]) > 25:
									if int(value[4][0]) - int(value[3][1]) <= 25:
										new_file.write(">" + "2reg_" + seq_record.id + "\n" + sequence + "\n")
with open("all_effector_wchap_genus_more100aa_CDHIT95.fasta", 'r') as fasta:
	count=0
	for seq_record in SeqIO.parse(fasta, "fasta"):
		sequence = str(seq_record.seq).upper()
		with open("all_effector_wchap_genus_more100aa_CDHIT95_tmhmm.fasta", 'a+') as new_file:
			if str(seq_record.id)[0:250] not in indict:
				new_file.write(">" + "notm_" + seq_record.id + "\n" + sequence + "\n")
				# else:
				# 	print(seq_record.id)
				# 	new_file.write(">" + "notm_" + seq_record.id + "\n" + sequence + "\n")
			# pass

# with open("one_effector_rmgap20_species_rmredun_mafft_rmgap20_pseudo.fasta", 'r') as fasta:
# 	for seq_record in SeqIO.parse(fasta, "fasta"):
# 		sequence = str(seq_record.seq).upper()
# 		# for k,v in tm.items():
# 		if seq_record.id in tm.keys():
# 			# print(tm[seq_record.id])
# 			with open("one_effector_rmgap20_species_rmredun_mafft_rmgap20_pseudo_tmhmm2.fasta", 'a+') as new_file:
# 				if len(tm[seq_record.id]) ==4:
# 					if int(tm[seq_record.id][1][1]) < 102:
# 						if int(tm[seq_record.id][3][1]) > 102:
# 							new_file.write(">" + "tse6_" + seq_record.id + "\n" + sequence + "\n")
# 				if len(tm[seq_record.id]) == 1:
# 					new_file.write(">" + "1tm_" + seq_record.id + "\n" + sequence + "\n")
# 				else:
# 					new_file.write(">" + "othertm_" + seq_record.id + "\n" + sequence + "\n")
