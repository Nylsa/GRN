import pandas as pd

# Read the CSV file
df = pd.read_csv('interactions_found.csv')

# Dictionary to store Boolean functions
boolean_functions = {}

# Process each row in the CSV file
for index, row in df.iterrows():
    source = row['source_genesymbol']
    target = row['target_genesymbol']
    interaction_type = row['interaction_type']

    if interaction_type == '->':
        boolean_functions[target] = source
    elif interaction_type == '-|':
        boolean_functions[target] = f"NOT {source}"

# Collect all unique nodes
nodes = set(df['source_genesymbol']).union(set(df['target_genesymbol']))

# Generate BNet format content
bnet_output = []
bnet_output.append(" ".join(sorted(nodes)))
for target in sorted(boolean_functions):
    bnet_output.append(f"{target}: {boolean_functions[target]}")

# Output the BNet format
bnet_content = "\n".join(bnet_output)
print(bnet_content)

# Optionally, write to a file
with open('output_bnet_file.txt', 'w') as f:
    f.write(bnet_content)
