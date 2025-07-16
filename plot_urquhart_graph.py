import matplotlib.pyplot as plt
import numpy as np

from numpy.typing import ArrayLike

def plot_urquhart_graph(X: ArrayLike, adj_matrix: np.ndarray) -> None:
    """
    Plot the Urquhart graph given the points and adjacency matrix.

    Parameters
    ----------
    X : ArrayLike
        An array-like structure containing the coordinates of the points in bidimensional space.
    adj_matrix : np.ndarray
        An adjacency matrix representing the Urquhart graph.
    """
    
    X = np.array(X)
    n = len(X)
    
    if X.ndim != 2 or X.shape[1] != 2:
        raise ValueError("Input points must be in 2D space.")

    plt.figure()
    
    # Plot points
    plt.scatter(X[:, 0], X[:, 1])
    
    # Plot edges based on adjacency matrix
    for i in range(n):
        for j in range(i + 1, n):
            if adj_matrix[i, j]:
                plt.plot([X[i, 0], X[j, 0]], [X[i, 1], X[j, 1]])
    
    plt.title('Urquhart Graph')
    plt.show()
