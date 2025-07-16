import numpy as np
from sklearn.datasets import make_blobs
from urquhart_graph import urquhart_graph
from plot_urquhart_graph import plot_urquhart_graph

# Generate test data using make_blobs
X, _ = make_blobs(n_samples=100, n_features=2)[0:2]

# Generate Urquhart graph
adj_matrix = urquhart_graph(X)

# Plot the result
plot_urquhart_graph(X, adj_matrix)
