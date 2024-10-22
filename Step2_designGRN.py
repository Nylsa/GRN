import pandas as pd
import networkx as nx

# Load the CSV files with verbose output
print("Loading CSV files...")
combined_df = pd.read_csv('/home/nylsachammartin/Documents/Clean-start/combinedTFandSignaling.csv')
filtered_df = pd.read_csv('/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/matching_paths_17102024.csv')
print(f"Loaded {len(combined_df)} rows from 'combinedTFandSignaling.csv'")
print(f"Loaded {len(filtered_df)} rows from 'matching_paths_17102024.csv'")

# Extract unique genes from the filtered genes file
filtered_genes = set(filtered_df['source_genesymbol']).union(set(filtered_df['target_genesymbol']))
print(f"Extracted {len(filtered_genes)} unique filtered genes")

# Create a directed graph from the combinedTFandSignaling data
print("Creating a directed graph from the combined data...")
G = nx.DiGraph()

# Add edges to the graph with edge attributes
for _, row in combined_df.iterrows():
    G.add_edge(
        row['source_genesymbol'], 
        row['target_genesymbol'], 
        is_stimulation=row['is_stimulation'], 
        is_inhibition=row['is_inhibition']
    )
print("Graph creation complete. Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Function to find a path between two nodes using BFS (more efficient for path discovery)
def find_path_bfs(graph, start_gene, end_gene):
    try:
        return nx.shortest_path(graph, source=start_gene, target=end_gene)
    except nx.NetworkXNoPath:
        return None

# Function to get the type of interaction between two genes
def get_interaction_type(graph, source, target):
    edge_data = graph.get_edge_data(source, target)
    if edge_data['is_stimulation'] == 1:
        return "->"
    elif edge_data['is_inhibition'] == 1:
        return "-|"
    else:
        return "->"  # Default to "->" if none specified, though this shouldn't occur

# Search for paths that involve the filtered genes
print("Searching for paths involving filtered genes...")
unique_paths = set()
checked_pairs = set()
interactions_found = []

for i, gene1 in enumerate(filtered_genes):
    for j, gene2 in enumerate(filtered_genes):
        if gene1 != gene2 and (gene1, gene2) not in checked_pairs:
            checked_pairs.add((gene1, gene2))
            print(f"Checking path from {gene1} to {gene2} ({i+1}/{len(filtered_genes)} and {j+1}/{len(filtered_genes)})...")
            path = find_path_bfs(G, gene1, gene2)
            if path:
                path_tuple = tuple(path)  # Convert path to a tuple for uniqueness
                if path_tuple not in unique_paths:
                    unique_paths.add(path_tuple)
                    # Generate the path string with proper symbols
                    path_str = path[0]
                    for k in range(len(path) - 1):
                        interaction_type = get_interaction_type(G, path[k], path[k + 1])
                        path_str += f" {interaction_type} {path[k + 1]}"
                        # Save the interaction for reporting
                        interactions_found.append({
                            'source_genesymbol': path[k],
                            'target_genesymbol': path[k + 1],
                            'interaction_type': interaction_type
                        })
                    print(f"Unique path found: {path_str}")
                else:
                    print(f"Duplicate path ignored.")
            else:
                print(f"No path found from {gene1} to {gene2}")

# Display the unique paths found
if unique_paths:
    print(f"\nUnique paths found involving the filtered genes:")
    for path in unique_paths:
        path_str = path[0]
        for k in range(len(path) - 1):
            interaction_type = get_interaction_type(G, path[k], path[k + 1])
            path_str += f" {interaction_type} {path[k + 1]}"
        print(path_str)
else:
    print("\nNo unique paths found involving the filtered genes.")

# Save unique path as well
unique_paths_df = pd.DataFrame(unique_paths)

output_unique_paths = '/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/uniquepaths_18102024.csv'
unique_paths_df.to_csv(output_unique_paths, index=False)

# Save the interactions found to a CSV file
interaction_df = pd.DataFrame(interactions_found)
interaction_df = interaction_df.drop_duplicates()  # Ensure no duplicate interactions are saved

output = '/home/nylsachammartin/Documents/projects/GeneRegNetworks/NRP79_GeneRegulatoryNetworks/interactions_found_18102024.csv'
interaction_df.to_csv(output, index=False)
print(f"\nAll interactions found in the paths have been saved to {output}.csv'")
