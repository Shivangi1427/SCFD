
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# Function to create the maximal product graph
import networkx as nx

def maximal_product_graph(G, H):
    product_graph = nx.DiGraph()

    # Add nodes (u, v) where u is in G and v is in H
    for u in G.nodes():
        for v in H.nodes():
            product_graph.add_node((u, v))
    
    # Add edges based on the maximal product graph definition
    for u1, u2 in G.edges():
        for v in H.nodes():
            # Condition 2: (u1, u2) in G, v remains unchanged
            product_graph.add_edge((u1, v), (u2, v))

    for v1, v2 in H.edges():
        for u in G.nodes():
            # Condition 1: (v1, v2) in H, u remains unchanged
            product_graph.add_edge((u, v1), (u, v2))

    for u1, u2 in G.edges():
        for v1, v2 in H.edges():
            # Condition 3: (u1, u2) in G and (v1, v2) in H
            product_graph.add_edge((u1, v1), (u2, v2))

    return product_graph
# Function to simulate burning on the graph
def burn_graph(G, sources, max_steps=10):
    burned = set(sources)
    new_burned = set(sources)
    history = [set(burned)]
    
    for _ in range(max_steps):
        current_burned = set(new_burned)
        new_burned = set()
        for node in current_burned:
            for neighbor in G.neighbors(node):
                if neighbor not in burned:
                    new_burned.add(neighbor)
                    burned.add(neighbor)
        history.append(set(burned))
        if len(burned) == len(G.nodes()):
            break
            
    return history

# Function to compute the aborescence tree
def aborescence_number(G):
    root = next(iter(G.nodes))
    directed_tree = nx.bfs_tree(G, root)
    return directed_tree

# Define the input graphs G and H
G = nx.DiGraph()
G.add_edges_from([
    ('c1', 'c2'), ('c2', 'c3'), ('c3', 'c1'),
    ('c1', 'c4'), ('c4', 'c5'), ('c5', 'c2')
])

H = nx.DiGraph()
H.add_edges_from([
    ('p1', 'p2'), ('p2', 'p3'), ('p3', 'p4'),
    ('p1', 'p5'), ('p5', 'p4')
])

# Create the maximal product graph
product_graph = maximal_product_graph(G, H)

# Compute the dominating set
dominating_set = nx.dominating_set(product_graph)
print("Dominating Set (Maximal Product Graph):", dominating_set)

# Compute the aborescence tree
aborescence_tree = aborescence_number(product_graph)
print("Aborescence Tree:", list(aborescence_tree.edges()))

# Simulate burning on the graph
sources = [list(product_graph.nodes())[0]]
history = burn_graph(product_graph, sources)

# Compute the layout for visualization
pos = nx.spring_layout(product_graph, k=1.5, iterations=50)

# Create the figure and subplots
fig, ax = plt.subplots(1, 4, figsize=(20, 5))

# Plot 1: Maximal Product Graph
ax[0].set_title("Maximal Product Graph")
nx.draw(product_graph, pos, with_labels=False, ax=ax[0], node_color='lightgrey', node_size=800)
nx.draw_networkx_labels(product_graph, pos, labels={node: f"{node[0]} {node[1]}" for node in product_graph.nodes()}, font_size=8, ax=ax[0])

# Plot 2: Maximal Product Graph with Dominating Set
ax[1].set_title("Maximal Product Graph with Domination Set")
node_colors = ['lightblue' if node not in dominating_set else 'orange' for node in product_graph.nodes()]
nx.draw(product_graph, pos, with_labels=False, node_color=node_colors, node_size=800, ax=ax[1])
nx.draw_networkx_labels(product_graph, pos, labels={node: f"{node[0]} {node[1]}" for node in product_graph.nodes()}, font_size=8, ax=ax[1])
for node in dominating_set:
    nx.draw_networkx_nodes(product_graph, pos, nodelist=[node], node_color='orange', node_size=1000, ax=ax[1])

# Plot 3: Aborescence Tree
ax[2].set_title("Aborescence Tree")
nx.draw(aborescence_tree, pos, with_labels=False, ax=ax[2], node_color='lightgreen', node_size=1000, edge_color='blue')
nx.draw_networkx_labels(aborescence_tree, pos, labels={node: f"{node[0]} {node[1]}" for node in aborescence_tree.nodes()}, font_size=8, ax=ax[2])

# Plot 4: Burning Number Animation
def update(step):
    ax[3].clear()
    ax[3].set_title(f"Burning Number (Maximal) - Step {step}")
    nx.draw(product_graph, pos, ax=ax[3], node_color='lightgrey', with_labels=False, node_size=1000)
    nx.draw_networkx_nodes(product_graph, pos, nodelist=history[step], node_color='red', ax=ax[3])
    nx.draw_networkx_labels(product_graph, pos, labels={node: f"{node[0]} {node[1]}" for node in product_graph.nodes()}, font_size=8, ax=ax[3])

ani = FuncAnimation(fig, update, frames=len(history), repeat=False, interval=1000)

plt.tight_layout()
plt.show()