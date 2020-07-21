import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logomaker

"""
To generate sequence logos for the short PAAR sequences

Requires: 
shortPAAR_PF05488_full_length_sequences_prePAAR_mafft_trim_fix.fasta - FASTA file of aligned, trimmed short PAAR sequences

Creates: 
ZN_SHORTPAAR_100-200.svg - SVG file for sequence logo

"""

crp_sites_df = pd.read_csv('shortPAAR_PF05488_full_length_sequences_prePAAR_mafft_trim_fix.fasta', comment='>', names=['site'])
crp_sites_df.head()
crp_sites_df.reset_index(inplace=True, drop=True)
# Location of amino acid residues to analyze
crp_sites_list = crp_sites_df['site'].str[100:200]
# Number of sequences to analyze
crp_sites_list[0:564]

crp_counts_df =logomaker.alignment_to_matrix(sequences=crp_sites_list, to_type='counts', characters_to_ignore="X-U.")

# INFORMATION MATRIX
info_mat = logomaker.transform_matrix(crp_counts_df, from_type='counts', to_type='information')

# NORMALIZE
normalized_mat = logomaker.transform_matrix(info_mat,normalize_values=True)
crp_logo = logomaker.Logo(normalized_mat,shade_below=.5,fade_below=.5,color_scheme={'C': 'blue','H': 'blue', 'E': 'green', 'D': 'green'},font_name='Arial Rounded MT Bold', figsize=(300,3),fade_probabilities=True)

crp_logo.style_spines(visible=False)
crp_logo.style_spines(spines=['left', 'bottom'], visible=True)
crp_logo.style_xticks(rotation=90, fmt='%d', anchor=0)


crp_logo.fig.show()
#Name of SVG sequence logo
crp_logo.fig.savefig(fname="ZN_SHORTPAAR_100-200.svg", format="svg")
