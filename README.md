# Community Detection using Louvain Method

## Overview
This project implements **Community Detection** in a network using the **Louvain Method**. It utilizes the `networkx` and `community-louvain` Python libraries to detect and visualize communities in a given network of nodes and edges.

## Features
- Builds an undirected graph using `networkx`
- Applies **Louvain Modularity** to detect communities
- Visualizes the network with detected communities

## Installation
Ensure you have Python installed and install the required libraries:
```sh
pip install networkx matplotlib python-louvain
```

## Usage
Run the script using Python:
```sh
python community_detection.py
```

## Code Explanation
### Class: `CommunityDetection`
- **`__init__(nodes, edges)`**: Initializes the graph with given nodes and edges.
- **`detect_communities()`**: Uses Louvain method to detect communities and prints results.
- **`visualize_graph()`**: Plots the graph with detected community clusters.

### Example Data
The network consists of:
#### **Nodes:**
```
[Amit, Rohan, Priya, Sneha, Rahul, Neha, Vikram, Kiran]
```
#### **Edges:**
```
[(Amit, Rohan), (Amit, Priya), (Priya, Sneha), (Sneha, Rahul), (Rahul, Neha),
(Neha, Vikram), (Vikram, Kiran), (Neha, Kiran), (Rahul, Priya)]
```

## Output Example
### **Communities Detected:**
```
Node Amit: Community 0
Node Rohan: Community 0
Node Priya: Community 1
Node Sneha: Community 1
Node Rahul: Community 1
Node Neha: Community 2
Node Vikram: Community 2
Node Kiran: Community 2
```

### **Visualization:**
A graph will be displayed showing the communities with different colors.

## Dependencies
- Python 3+
- `networkx`
- `matplotlib`
- `community-louvain`

## Author
**Yogesh** (2022BCD0052)

