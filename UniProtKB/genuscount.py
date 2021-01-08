import sys
import csv
import os
import glob
import ast
from Bio import SeqIO
import re
all_targets={}
from collections import Counter
#removes redundancy of a FASTA file picks a random representative header as the unique sequence
import sys
from Bio import SeqIO
import glob
import sys
import csv
import os
import glob
from Bio import SeqIO
import re
records=[]
listofheaders=[]
headers=[]

for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations.6-fullseq.fasta", "fasta"):
	header = str(seq_record.id)
	sequence = str(seq_record.seq).upper()
	records.append(header)
with open('uniprot-yourlist_M20200405A94466D2655679D1FD8953E075198DA823C4239.tsv', 'r') as filename:
	filename = csv.reader(filename, delimiter='\t')
	for row in filename:
		if row[4] != "Deleted.":
			for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations.6-fullseq.fasta", "fasta"):
				header = str(seq_record.id)
				sequence = str(seq_record.seq).upper()
				if row[0] == header:
					species=re.sub('[\W_]+', '', row[6])
					newlabel=species+"_"+(row[2])
					print(newlabel)
					with open('Full_fasta_60aa_PA0093_query_6iterations_species.fasta', 'a') as newfile:
						newfile.write(">" + newlabel + "\n" + sequence + "\n")


		# for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations.6-fullseq.fasta", "fasta"):
		# 	header = str(seq_record.id)
		# 	sequence = str(seq_record.seq).upper()
		# 	records.append(header)
# for seq_record in SeqIO.parse("Full_fasta_60aa_PA0093_query_6iterations.6-fullseq.fasta", "fasta"):
# 	header = str(seq_record.id)
# 	sequence = str(seq_record.seq).upper()




# for seq_record in SeqIO.parse("first300aa_strictfilter_tmhmm_edit.fasta", "fasta"):
# 	header = str(seq_record.id)
# 	sequence = str(seq_record.seq).upper()
# 	if header in listofheaders:
# 		with open("first300aa_strictfilter_tmhmm_edit_300aa_CD_99_final.fasta", 'a+') as new_file:
# 			new_file.write(">" + header + "\n" + sequence + "\n")
