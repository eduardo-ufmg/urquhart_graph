import numpy as np
from numpy.typing import ArrayLike
from scipy.spatial import Delaunay


def urquhart_graph(X: ArrayLike) -> np.ndarray:
    """
    Generate the Urquhart graph from a set of points.

    Parameters
    ----------
    X : ArrayLike
        An array-like structure containing the coordinates of the points.

    Returns
    -------
    np.ndarray
        An adjacency matrix representing the Urquhart graph.
    """

    X = np.array(X)
    n = len(X)

    # Create adjacency matrix
    adj_matrix = np.zeros((n, n), dtype=bool)

    # Compute Delaunay triangulation
    tri = Delaunay(X)

    # Process each triangle
    for triangle in tri.simplices:
        # Get the three vertices of the triangle
        p1, p2, p3 = triangle

        # Calculate edge lengths
        edge_lengths = [
            np.linalg.norm(X[p1] - X[p2]),  # edge p1-p2
            np.linalg.norm(X[p2] - X[p3]),  # edge p2-p3
            np.linalg.norm(X[p3] - X[p1]),  # edge p3-p1
        ]

        # Find the longest edge
        longest_edge_idx = np.argmax(edge_lengths)

        # Add the two shorter edges to the adjacency matrix
        edges = [(p1, p2), (p2, p3), (p3, p1)]
        for i, (u, v) in enumerate(edges):
            if i != longest_edge_idx:
                adj_matrix[u, v] = True
                adj_matrix[v, u] = True

    return adj_matrix.astype(int)
