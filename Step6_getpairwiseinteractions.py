import pandas as pd

file = open("/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/matching_paths_step5.path","r")
input_string = file.read()
print(input_string)

    
def split_interactions(input_string):
    # Split the interactions by lines
    interactions = input_string.strip().split('\n')
    
    pairwise_interactions = []
    
    for interaction in interactions:
        # Replace inhibition (-|) with a unique separator to process separately
        interaction = interaction.replace('->', ' -> ').replace('-|', ' -| ')
        
        # Split by spaces
        parts = interaction.split()
        
        for i in range(0, len(parts) - 2, 2):
            # Pair the gene with its interaction type
            pairwise_interactions.append(f'{parts[i]} {parts[i+1]} {parts[i+2]}')

    return '\n'.join(pairwise_interactions)



# Call the function
output = split_interactions(input_string)
print(output)



output_file = open("/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/pairwise_interactions.txt", "w")
output_file.write(output)
output_file.close()

