import pandas as pd

# Original list with duplicates
interactions = [
    "Rigi -> Mavs",
    "Mavs -> Casp8",
    "Casp8 -> Bid",
    "Rigi -| Traf3",
    "Traf3 -| Map3k14",
    "Map3k14 -> Stat3",
    "Stat3 -> Pim3",
    "Rigi -> Ikbke",
    "Ikbke -> Traf2",
    "Traf2 -> Ripk3",
    "Ripk3 -> Mlkl",
    "Rigi -> Tbk1",
    "Tbk1 -> Rela",
    "Rela -> Mapk14",
    "Mapk14 -> Max",
    "Rigi -> Mavs",
    "Mavs -> Casp8",
    "Casp8 -> Casp3"
]

# Removing duplicates by converting to a set and then back to a list
interactions_unique = list(set(interactions))

# Sorting the list for better readability (optional)
interactions_unique.sort()

# Output the unique interactions
#print(interactions_unique)

#pairwise_int = pd.read_csv("/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/pairwise_interactions.csv", index_col=False)
#print(f"Printing Pairwise_int head': \n {pairwise_int.head(10)}")

#pairwise_int_list = list(pairwise_int)
#print(f"Printing pairwise as a list : \n {pairwise_int_list}")

#pairwise_int_set = set(pairwise_int)
#print(f"Printing the Set: \n {pairwise_int_set}")

# Open the file in read mode
lines = []
lines2 = []

with open("/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/pairwise_interactions.txt", 'r') as file: 
    for line in file:
        lines.append(line.strip())
        #print(lines)

lines_set = set(lines)
#print(lines_set)

lines_list = list(lines_set)
print(lines_list)


output = "/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/pairwise_interactions_unique.txt"
with open(output, "w") as out:
    for line in lines_list:
        out.write(line + '\n')




        

