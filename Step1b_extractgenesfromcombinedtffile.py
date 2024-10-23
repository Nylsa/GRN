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
    'Il18', 'Tp53', 'Acin1', 'Aifm1', 'Alkbh7', 'Apaf1', 
    'Atraid', 'Aven', 'Bad', 'Bak1', 'Bax', 'Bbc3', 'Bcap31', 'Bcl10',
    'Bcl2', 'Bcl2a1', 'Bcl2l1', 'Bcl2l10', 'Bcl2l11', 'Bcl2l2', 'Becn1', 
    'Bid', 'Bik', 'Birc2', 'Birc3', 'Birc5', 'Birc6', 'Birc7', 'Bnip3', 
    'Bnip3l', 'Bok', 'Casp1', 'Casp14', 'Casp2', 'Casp3', 'Casp4', 'Casp5', 
    'Casp6', 'Casp7', 'Casp8', 'Casp9', 'Ccar2', 'Cd40lg', 'Cdip1', 'Cflar', 
    'Cox4i1', 'Ctsb', 'Ctsd', 'Cxcr4', 'Cycs', 'Dap', 'Dapk1', 'Dapk3', 'Daxx', 
    'Dffa', 'Diablo', 'Dido1', 'Dnaja3', 'Dyrk1b', 'Ei24', 'Eif4g2', 'Endog', 
    'Fadd', 'Faf1', 'Faim', 'Fas', 'Faslg', 'Gdf15', 'Gimap5', 'Gsdmd', 'Gzma', 
    'Gzmb', 'H2bc3', 'Hipk2', 'Htatip2', 'Htra2', 'Lgals1', 'Lmna', 
    'Lmnb1', 'Lmnb2', 'Malt1', 'Map3k5', 'Max', 'Mcl1', 'Mff', 'Mlkl', 'Mlx', 
    'Mnda', 'Mxd1', 'Myc', 'Mycn', 'Ndrg1', 'Ndrg2', 'Ndrg3', 'Ndrg4', 'Nlrp1', 
    'Nod1', 'Nol3', 'Nqo1', 'Nr4a1', 'Nuak2', 'Opa1', 'Panx1', 'Parp1', 'Pawr', 
    'Pdcd4', 'Pdcd6ip', 'Pea15', 'Phlda3', 'Pik3c3', 'Pim1', 'Pim2', 'Pim3', 'Pir', 
    'Pmaip1', 'Psip1', 'Ptpn11', 'Ptrh2', 'Ripk1', 'Ripk2', 'Ripk3', 'Rubcn', 
    'Serpinb5', 'Sfn', 'Sh3glb1', 'Sirt1', 'Siva1', 'Slk', 'Smpd2', 'Sptan1', 'Stk17b', 
    'Stk24', 'Stk3', 'Stk4', 'Tank', 'Tax1bp1', 'Tfap2a', 'Tfap2b', 'Tfap2c', 'Tfeb', 
    'Tia1', 'Tial1', 'Tigar', 'Tmpo', 'Tnf', 'Tnfaip3', 'Tnfrsf10a', 'Tnfrsf10b', 
    'Tnfrsf10c', 'Tnfrsf10d', 'Tnfrsf11a', 'Tnfrsf12a', 'Tnfrsf1a', 'Tnfrsf1b', 
    'Tnfrsf21', 'Tnfrsf25', 'Tnfrsf6b', 'Tnfsf10', 'Tnfsf11', 'Tnfsf12', 'Tradd', 
    'Traf1', 'Traf2', 'Traf3', 'Traf4', 'Traf5', 'Traf6', 'Txn', 'Tymp', 'Unc5b', 
    'Uri1', 'Usp10', 'Vdac1', 'Wwox', 'Xaf1', 'Xiap', 'Ywhab', 'Ywhae', 'Ywhag', 
    'Ywhah', 'Ywhaq', 'Ywhaz', 'Yy1', 'Zc3hc1'
]

# Filter the dataframe to only include rows where 'target_genesymbol' or 'source_genesymbol' is in the list of genes of interest
filtered_df = df[(df['target_genesymbol'].isin(geneofinterest)) | (df['source_genesymbol'].isin(geneofinterest))]

# Save the filtered data to a new file
filtered_df.to_csv('/home/nylsachammartin/Documents/projects/GeneRegNetworks/GRN/outputdata/Step1b_filtered_genes_either_nylsa.csv', index=False)

print("Filtered data saved.")
