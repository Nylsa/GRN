import pandas as pd

lines = []

# Open the file from Step6
with open("/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/pairwise_interactions.txt", 'r') as file: 
    for line in file:
        lines.append(line.strip())
        #print(lines)

# Create a set of the lines list to remove all duplicates.
lines_set = set(lines)

# Redo a list out of the now unique lines.
lines_list = list(lines_set)
print(lines_list)

# Save file
output = "/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/pairwise_interactions_unique.txt"
with open(output, "w") as out:
    for line in lines_list:
        out.write(line + '\n')