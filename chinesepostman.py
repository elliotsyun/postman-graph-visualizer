"""
Eulerian Graph Generator

This script generates a random Eulerian graph with a given number of vertices
and attempts to find the Eulerian path or circuit within it. The Chinese
Postman Problem is a famous problem in graph theory. The problem is to find
the shortest path or circuit that visits every edge of a graph. This script
provides a solution by generating a random Eulerian graph and finding the
Eulerian path or circuit within it.

Author: Elliot Yun
Date: 4/23/2024

"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def generate_even_sequence(vertices, seed=None):
    """
    Generate a sequence of even integers, representing degrees of vertices in a graph.

    Parameters:
        vertices (int): Number of vertices in the graph.
        seed (int, optional): Seed for the random number generator.

    Returns:
        ndarray: An array containing even integers that sum to an even number.
    """
    if seed is not None:
        np.random.seed(seed)

    even_degree_sequence = np.random.randint(1, 4, size=vertices) * 2
    print("The number of routes that leads to each house is: ", even_degree_sequence)
    return even_degree_sequence


def make_eulerian_graph(degree_sequence, seed=None):
    """
    Create and display an Eulerian graph from a given degree sequence.

    Parameters:
        degree_sequence (list): Degree sequence for the graph.
        seed (int, optional): Seed for the random number generator.

    Returns:
        tuple: A tuple containing the graph object and position dictionary.
    """
    print("Creating Eulerian graph...")
    G = nx.configuration_model(degree_sequence, seed=seed)
    G = nx.Graph(G)  # Convert to simple graph
    nx.eulerize(G)  # Make graph Eulerian

    pos = nx.spring_layout(G)  # Node position layout for visualization
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="black",
        edge_color="gray",
        width=1,
        node_size=400,
    )
    plt.show()

    print("Eulerian graph created...")
    return G, pos


def find_eulerians(G):
    """
    Determine if the graph has an Eulerian circuit or path and return it.

    Parameters:
        G (Graph): A networkx graph.

    Returns:
        list: A list of edges forming the Eulerian circuit or path, if it exists.
    """
    if nx.is_eulerian(G):

        print(
            "The graph has an Eulerian Circuit, which means it has an" "Eulerian Path."
        )
        circuit = list(nx.eulerian_circuit(G))
        print(circuit)
        return circuit
    elif nx.has_eulerian_path(G):
        print("There is an Eulerian Path in this graph.")
        path = list(nx.eulerian_path(G))
        print(path)
        return path
    else:
        print("This graph is neither Eulerian nor has an Eulerian Path.")
        return None


def draw_eulerians(G, eulerian_path, pos):
    """
    Draw the Eulerian path or circuit on the graph.

    Parameters:
        G (Graph): The graph on which to draw.
        eulerian_path (list): Eulerian path or circuit as a list of edges.
        pos (dict): Node positions in the graph.
    """
    if eulerian_path is None:
        print("There is no Eulerian circuit or path to draw.")
        return

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightgray",
        edge_color="gray",
        width=1,
        node_size=300,
    )
    nx.draw_networkx_edges(G, pos, edgelist=eulerian_path, edge_color="red", width=2)

    for i, edge in enumerate(eulerian_path):
        node1, node2 = edge
        x1, y1 = pos[node1]
        x2, y2 = pos[node2]
        edge_label_pos = ((x1 + x2) / 2, (y1 + y2) / 2)

        plt.text(
            edge_label_pos[0],
            edge_label_pos[1],
            str(i + 1),
            color="blue",
            fontsize=12,
            ha="center",
            va="center",
        )
    plt.show()


def main():
    """
    Main function to generate and display an Eulerian graph.
    """

    num_routes = int(
        input(
            "Welcome to the Chinese Postman Problem Solver, which is a"
            "Eulerian circuit based graph solver.\n...\n"
            "How many houses do you want the postman to travel to?"
        )
    )

    sequence = generate_even_sequence(num_routes, seed=6969)
    G, pos = make_eulerian_graph(sequence, seed=6969)
    euler = find_eulerians(G)
    if euler is not None:
        print("Eulerian path/circuit:", euler)
        draw_eulerians(G, euler, pos)
    else:
        print("No Eulerian path or circuit was found.")


if __name__ == "__main__":
    main()
