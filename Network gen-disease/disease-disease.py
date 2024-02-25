


import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go


gene_to_diseases = {
    "VEGFA": [
        ("Microvascular Complications of Diabetes 1", 30.223),
        ("Colorectal Cancer", 15.053),
        ("Lung Cancer", 13.741),
    ]
}

# Connections of "Microvascular Complications of Diabetes 1" to other diseases and genes
microvascular_complications_related = [
    ("Microvascular Complications of Diabetes 1","background diabetic retinopathy", 32.9, ["VCAM1", "ICAM1", "CCL2", "ANGPT2"]),
    ("Microvascular Complications of Diabetes 1","macular holes", 31.7, ["TGFB2", "SERPINF1", "FGF2", "CXCL8", "CCL2", "ANGPT2"]),
    ("Microvascular Complications of Diabetes 1","renal fibrosis", 31.6, ["TIMP1", "TGFB2", "MMP9", "HGF", "FGF2", "CCN2"]),
    ("Microvascular Complications of Diabetes 1","rubeosis iridis", 31.6, ["SERPINF1", "FLT1"]),
    ("Microvascular Complications of Diabetes 1","glomerulonephritis", 31.6, ["VCAM1", "ICAM1", "CCN2", "CCL2"]),
    ("Microvascular Complications of Diabetes 1","vitreous detachment", 31.4, ["TGFB2", "GFAP", "FGF2"]),
    ("Microvascular Complications of Diabetes 1","retinal ischemia", 31.3, ["VEGFA", "ICAM1", "GFAP", "FGF2", "CCL2"]),
    ("Microvascular Complications of Diabetes 1","endophthalmitis", 31.3, ["ICAM1", "FLT1", "CXCL8"]),
    ("Microvascular Complications of Diabetes 1","retinal vascular disease", 31.1, ["VEGFA", "SERPINF1", "ICAM1", "FLT1", "FGF2", "CCN2"]),
    ("Microvascular Complications of Diabetes 1","uveitis", 31.0, ["TGFB2", "SERPINF1", "ICAM1", "CXCL8", "CCL2"]),
]

# Connections of "Colorectal Cancer" to other diseases and genes
colorectal_cancer_related = [
    ("Colorectal Cancer","lynch syndrome", 35.1, ["TP53", "PIK3CA", "NRAS", "MLH3", "CTNNB1", "BRAF"]),
    ("Colorectal Cancer","colonic benign neoplasm", 34.1, ["TP53", "PIK3CA", "NRAS", "CTNNB1", "BRAF", "AXIN2"]),
    ("Colorectal Cancer","adenoma", 34.0, ["TP53", "PIK3CA", "CTNNB1", "BRAF", "AXIN2", "APC"]),
    ("Colorectal Cancer","familial adenomatous polyposis", 34.0, ["TP53", "MCC", "CTNNB1", "BRAF", "BAX", "AXIN2"]),
    ("Colorectal Cancer","cowden syndrome", 33.9, ["TP53", "PIK3CA", "NRAS", "MLH3", "FLCN", "FGFR3"]),
    ("Colorectal Cancer","rectal benign neoplasm", 33.9, ["TP53", "PIK3CA", "NRAS", "CTNNB1", "BRAF"]),
    ("Colorectal Cancer","adenocarcinoma", 33.7, ["TP53", "PIK3CA", "FGFR3", "CTNNB1", "BRAF", "BAX"]),
    ("Colorectal Cancer","hepatocellular carcinoma", 33.7, ["TP53", "PIK3CA", "PDGFRL", "NRAS", "EP300", "DLC1"]),
    ("Colorectal Cancer","endometrial cancer", 33.7, ["TP53", "PIK3CA", "NRAS", "MLH3", "FGFR3", "CTNNB1"]),
    ("Colorectal Cancer","colorectal adenocarcinoma", 33.5, ["TP53", "PIK3CA", "NRAS", "CTNNB1", "BRAF", "AKT1"]),
]

lung_cancer_related = [
    ("Lung Cancer","lung cancer susceptibility 3", 35.4, ["TP53", "RB1", "PRKN", "PIK3CA", "NRAS", "MAP2K1"]),
    ("Lung Cancer","small cell cancer of the lung", 34.7, ["TP53", "RB1", "PIK3CA", "EGFR", "AKT1"]),
    ("Lung Cancer","adenocarcinoma of the lung", 34.4, ["TP53", "RB1", "PIK3CA", "MAP2K1", "KRAS", "ERBB2"]),
    ("Lung Cancer","squamous cell carcinoma of the lung", 34.2, ["TP53", "RB1", "PIK3CA", "NRAS", "KRAS", "FASLG"]),
    ("Lung Cancer","lung squamous cell carcinoma", 34.2, ["TP53", "RB1", "PIK3CA", "KRAS", "EGFR", "BRAF"]),
    ("Lung Cancer","breast cancer", 33.9, ["TP53", "SLC22A18", "RB1", "PIK3CA", "MAP2K1", "KRAS"]),
    ("Lung Cancer","colorectal cancer", 33.8, ["TP53", "RB1", "PPP2R1B", "PIK3CA", "NRAS", "MAP2K1"]),
    ("Lung Cancer","hepatocellular carcinoma", 33.7, ["TP53", "RB1", "PPP2R1B", "PIK3CA", "NRAS", "MAP2K1"]),
    ("Lung Cancer","gastric cancer", 33.7, ["TP53", "RB1", "PIK3CA", "NRAS", "MAP2K1", "KRAS"]),
    ("Lung Cancer","peripheral nervous system disease", 33.6, ["TP53", "PRKN", "NRAS", "KRAS", "FASLG", "ERBB2"]),
]

G = nx.Graph()

# Add nodes and edges for the gene to diseases connections
for gene, diseases in gene_to_diseases.items():
    for disease, score in diseases:
        G.add_node(gene, type='gene', label=gene)
        G.add_node(disease, type='disease', label=disease)
        G.add_edge(gene, disease, weight=score, label="{:.2f}".format(score))

# Add nodes and edges for the diseases to related diseases and genes
all_related = microvascular_complications_related + colorectal_cancer_related + lung_cancer_related
for original_disease, related_disease, score, genes in all_related:
    G.add_node(related_disease, type='disease', label=related_disease)
    G.add_edge(original_disease, related_disease, weight=score, label="{:.2f}".format(score))
    for gene in genes:
        G.add_node(gene, type='gene', label=gene)
        G.add_edge(gene, related_disease, weight=score, label="{:.2f}".format(score))

pos = nx.spring_layout(G)

# For each edge, make an edge_trace, append to list
edge_trace = []
for edge in G.edges():
    char_1 = edge[0]
    char_2 = edge[1]
    
    x0, y0 = pos[char_1]
    x1, y1 = pos[char_2]
    
    trace = go.Scatter(x=[x0, x1, None], y=[y0, y1, None],
                       line=dict(width=0.5, color='#888'),
                       hoverinfo='none',
                       mode='lines')
    
    edge_trace.append(trace)

# For each node, make a node_trace, append to list
node_trace = go.Scatter(x=[], y=[], text=[], textposition="top center",
                        textfont=dict(family="sans serif", size=18, color="LightSeaGreen"),
                        mode='markers+text', hoverinfo='text',
                        marker=dict(showscale=False, color=[], size=10, colorscale='Viridis',
                                    line=dict(width=2)))

for node in G.nodes():
    x, y = pos[node]
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])
    
    # Add node name to the hover text
    node_trace['text'] += tuple(['<b>' + node + '</b>'])
    
    # Color node points by the type of node
    if G.nodes[node]['type'] == 'gene':
        node_trace['marker']['color'] += tuple(['rgba(255, 0, 0, .8)'])  # Red for genes
    else:
        node_trace['marker']['color'] += tuple(['rgba(0, 0, 255, .8)'])  # Blue for diseases

# Create figure
fig = go.Figure(data=edge_trace + [node_trace],
                layout=go.Layout(title='<br>Gene-Disease Network', titlefont_size=16,
                                 showlegend=False, hovermode='closest',
                                 margin=dict(b=20,l=5,r=5,t=40),
                                 annotations=[ dict(text="Python code powered by Plotly", showarrow=False,
                                                    xref="paper", yref="paper", x=0.005, y=-0.002)],
                                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

# Show figure
fig.show()