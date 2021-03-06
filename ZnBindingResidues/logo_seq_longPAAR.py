import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logomaker
"""
To generate sequence logos for the long PAAR sequences

Requires: 
Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_mafft_trim_fix.fasta - FASTA file of aligned, trimmed long PAAR sequences

Creates: 
ZN_SHORTPAAR_100-200.svg - SVG file for sequence logo

"""
crp_sites_df = pd.read_csv('Full_fasta_60aa_PA0093_query_6iterations_renamed_tmhmm_phobius_expasy_more100_prePAAR_mafft_trim_fix.fasta', comment='>', names=['site'])
crp_sites_df.head()
crp_sites_df.reset_index(inplace=True, drop=True)
# Location of amino acid residues to analyze
crp_sites_list = crp_sites_df['site'].str[0:100]
# Number of sequences to analyze
crp_sites_list[0:1765]

crp_counts_df =logomaker.alignment_to_matrix(sequences=crp_sites_list, to_type='counts', characters_to_ignore="X-U.")

# INFORMATION MATRIX
info_mat = logomaker.transform_matrix(crp_counts_df, from_type='counts', to_type='information')
# crp_logo = logomaker.Logo(info_mat,shade_below=.5,fade_below=.5,color_scheme='charge',font_name='Arial Rounded MT Bold', figsize=(140,3))


# NORMALIZE
normalized_mat = logomaker.transform_matrix(info_mat,normalize_values=True)
crp_logo = logomaker.Logo(normalized_mat,shade_below=.5,fade_below=.5,color_scheme={'C': 'blue','H': 'blue', 'E': 'green', 'D': 'green'},font_name='Arial Rounded MT Bold', figsize=(300,3),fade_probabilities=True)

crp_logo.style_spines(visible=False)
crp_logo.style_spines(spines=['left', 'bottom'], visible=True)
crp_logo.style_xticks(rotation=90, fmt='%d', anchor=0)


crp_logo.fig.show()
#Name of SVG sequence logo
crp_logo.fig.savefig(fname="ZN_LONGPAAR_1-100.svg", format="svg")
