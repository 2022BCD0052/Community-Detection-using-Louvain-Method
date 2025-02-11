# 2022BCD0052S
import networkx as nx
import matplotlib.pyplot as plt
import community.community_louvain as community_louvain

class CommunityDetection:
    def __init__(self, nodes, edges):
        self.G = nx.Graph()
        self.G.add_nodes_from(nodes)
        self.G.add_edges_from(edges)
        self.partition = None

    def detect_communities(self):
        self.partition = community_louvain.best_partition(self.G)
        print("\nCommunities Detected (Louvain Method):")
        for node, community in self.partition.items():
            print(f"Node {node}: Community {community}")

    def visualize_graph(self):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.G, k=0.5)
        node_colors = [self.partition[node] for node in self.G.nodes]
        
        nx.draw(
            self.G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.jet,
            node_size=2500, font_size=10, font_color="black", edge_color="gray"
        )
        plt.title("Network with Communities Detected (Louvain Method)")
        plt.show()

if __name__ == "__main__":
    nodes = ["Amit", "Rohan", "Priya", "Sneha", "Rahul", "Neha", "Vikram", "Kiran"]
    edges = [
        ("Amit", "Rohan"), ("Amit", "Priya"), ("Priya", "Sneha"), ("Sneha", "Rahul"),
        ("Rahul", "Neha"), ("Neha", "Vikram"), ("Vikram", "Kiran"), ("Neha", "Kiran"), ("Rahul", "Priya")
    ]
    
    community_detection = CommunityDetection(nodes, edges)
    community_detection.detect_communities()
    community_detection.visualize_graph()
