import pandas as pd

# Load the data
df = pd.read_csv('/home/nylsachammartin/Documents/Clean-start/combinedTFandSignaling.csv')

# List of genes of interest
geneofinterest = [
    'Cdc20b', 'E2f7', 'Foxn4', 'Hes6', 'Plk4', 'Ccno', 'Cep78', 'Deup1', 
    'Rsph1', 'C20orf85', 'C9orf24', 'Foxj1', 'Spef2', 'Pifo', 'Sntn', 
    'Dnaaf1', 'Krt5', 'Serpinb3', 'Krt15', 'Krt17', 'Tp63', 'Dst', 
    'Bcam', 'Dsg3', 'Tns4', 'Cy2pf1', 'Psca', 'Ald1a3', 'Ikbkb', 
    'Rela', 'Il6', 'Il8', 'Il1', 'Tnf', 'Cxcl10', 'Tgfa', 'Tgfb', 
    'Stat3', 'Stat6', 'Nlrp1b', 'Nlrp5', 'Nlrp3', 'Nlrp12', 'Nlrp10',
    'Il18', 'Tp53', 'Bax', 'Bcl10',
    'Bcl2', 'Casp1', 'Casp14', 'Casp2', 'Casp3', 'Casp4', 'Casp5', 
    'Casp6', 'Casp7', 'Casp8', 'Casp9', 'Max', 'Mcl1', 'Myc', 'Mycn', 'Ndrg1', 'Ndrg2', 'Ndrg3', 'Ndrg4', 'Nlrp1', 
    'Nod1', 'Nol3', 'Ripk1', 'Ripk2', 'Ripk3', 'Rubcn', 
    'Serpinb5', 'Sfn', 'Sh3glb1', 'Siva1', 'Stk17b', 
    'Stk24', 'Stk3', 'Stk4', 'Tank', 'Tax1bp1', 'Tnf'
]    

print(len(geneofinterest))

# Filter the dataframe to only include rows where 'target_genesymbol' or 'source_genesymbol' is in the list of genes of interest
filtered_df = df[(df['target_genesymbol'].isin(geneofinterest)) | (df['source_genesymbol'].isin(geneofinterest))]

# Save the filtered data to a new file
filtered_df.to_csv('/home/nylsachammartin/Documents/projects/GeneRegNetworks/GRN/outputdata/Step1b_filtered_genes_either_nylsa_reduced_b.csv', index=False)

print("Filtered data saved.")
