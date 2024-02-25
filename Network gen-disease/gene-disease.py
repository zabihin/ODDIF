import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Mocked up data based on the image provided by the user
data = {
    'Name': [
        'Microvascular Complications of Diabetes 1', 'Colorectal Cancer', 'Lung Cancer',
        'Breast Cancer', 'Pancreatic Cancer', 'Glioblastoma'
    ],
    'score': [
        30.223, 15.053, 13.741, 12.291, 12.291,
        12.291
    ]
}

df = pd.DataFrame(data)

# Create a new graph
G = nx.Graph()

# Add the center node 'VFEGA'
G.add_node('VFEGA', size=300, color='red')

# Define color map and normalization for the scores
norm = plt.Normalize(min(df['score']), max(df['score']))
colors = [plt.cm.viridis(norm(score)) for score in df['score']]
thickness = [(score / max(df['score'])) * 10 for score in df['score']]

# Add edges with attributes for color and thickness
for i, row in df.iterrows():
    G.add_edge('VFEGA', row['Name'], weight=thickness[i], color=colors[i])

# Draw the network graph with VFEGA as the center
pos = nx.spring_layout(G)  # Position the nodes using the spring layout

# Extract edge attributes to supply them to nx.draw_networkx_edges
edges = G.edges(data=True)
colors = [edge[2]['color'] for edge in edges]
thickness = [edge[2]['weight'] for edge in edges]

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_size=700)

# Draw edges with varying colors and thickness
nx.draw_networkx_edges(G, pos, edges, width=thickness, edge_color=colors)

# Draw node labels
nx.draw_networkx_labels(G, pos)

# Set plot title and remove axes for a cleaner look
plt.title('Disease Network with VFEGA at the Center')
plt.axis('off')

# Display the graph
plt.show()
