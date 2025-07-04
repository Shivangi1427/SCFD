import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# Function to create co-normal product graph
def conormal_product_graph(G, H):
    product_graph = nx.DiGraph()
    
    # Add nodes
    for u in G.nodes():
        for v in H.nodes():
            product_graph.add_node((u, v))
    
    # Add edges based on co-normal product definition
    for u1, u2 in G.edges():
        for v in H.nodes():
            product_graph.add_edge((u1, v), (u2, v))
    
    for v1, v2 in H.edges():
        for u in G.nodes():
            product_graph.add_edge((u, v1), (u, v2))
    
    return product_graph

# Function to simulate burning process
def burn_graph(G, sources, max_steps=20):  # Increased max_steps
    burned = set(sources)  
    new_burned = set(sources)
    history = [set(new_burned)]  
    
    for _ in range(max_steps):
        current_burned = set(new_burned)
        new_burned = set()
        
        # Spread fire to neighbouring nodes
        for node in current_burned:
            for neighbor in G.neighbors(node):
                if neighbor not in burned:
                    new_burned.add(neighbor)
                    burned.add(neighbor)
        
        if not new_burned:  # Stop if no new nodes are burning
            break
        
        history.append(set(burned))  # Track all burned nodes
    
    return history

# Function to compute aborescence tree
def aborescence_number(G):
    root = next(iter(G.nodes))
    directed_tree = nx.bfs_tree(G, root)
    return directed_tree

# Define two directed graphs
G = nx.DiGraph()
G.add_edges_from([
    ('A', 'B'), ('B', 'C'), ('C', 'A'),
    ('A', 'D'), ('D', 'E'), ('E', 'B')
])

H = nx.DiGraph()
H.add_edges_from([
    ('X', 'Y'), ('Y', 'Z'), ('Z', 'W'),
    ('X', 'P'), ('P', 'W')
])

# Create co-normal product graph
product_graph = conormal_product_graph(G, H)

# Compute properties
dominating_set = nx.dominating_set(product_graph)
aborescence_tree = aborescence_number(product_graph)

# Start with more initial burning nodes (e.g., 5 nodes)
sources = list(product_graph.nodes())[:5]  # Increased number of sources
history = burn_graph(product_graph, sources)

# Use circular layout for better readability
pos = nx.circular_layout(product_graph)

# Format labels to remove brackets and quotes
labels = {node: f"{node[0]} {node[1]}" for node in product_graph.nodes()}

# Plot setup
fig, ax = plt.subplots(1, 4, figsize=(20, 5))

# Plot 1: Co-Normal Product Graph
ax[0].set_title("Co-Normal Product Graph")
nx.draw(product_graph, pos, labels=labels, node_size=400, node_color='lightgrey', ax=ax[0], font_size=8)

# Plot 2: Co-Normal Product Graph with Domination Set
ax[1].set_title("Graph with Domination Set")
node_colors = ['lightblue' if node not in dominating_set else 'orange' for node in product_graph.nodes()]
nx.draw(product_graph, pos, labels=labels, node_color=node_colors, node_size=400, ax=ax[1], font_size=8)
for node in dominating_set:
    nx.draw_networkx_nodes(product_graph, pos, nodelist=[node], node_color='orange', node_size=500, ax=ax[1])

# Plot 3: Aborescence Tree
ax[2].set_title("Aborescence Tree")
nx.draw(aborescence_tree, pos, labels=labels, node_size=400, node_color='lightgreen', edge_color='blue', ax=ax[2], font_size=8)

# Burning Animation — Show Currently Burning Nodes
def update(step):
    ax[3].clear()
    ax[3].set_title(f"Burning Number - Step {step + 1}")
    
    # Draw base graph in grey
    nx.draw(product_graph, pos, labels=labels, node_color='lightgrey', node_size=400, ax=ax[3], font_size=8)
    
    if step < len(history):
        burning_nodes = history[step]
        # Highlight currently burning nodes in red
        nx.draw_networkx_nodes(product_graph, pos, nodelist=list(burning_nodes), node_color='red', node_size=400, ax=ax[3])

    # Stop animation when burning completes
    if step == len(history) - 1:
        ani.event_source.stop()

# Create animation
ani = FuncAnimation(fig, update, frames=len(history), repeat=False, interval=800)

plt.tight_layout()
plt.show()