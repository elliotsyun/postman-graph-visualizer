import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# This program will generate a random Eulerian graph with a given number of vertices, and tries to find
# the Eulerian path or circuit within it.

# The Chinese Postman Problem is where a postman tries to deliver mail to a town using the shortest route possible


# generating a degree sequence full of even numbers for the random graph,
# maximum amount of degrees at a single vertex is capped to 7
def generate_even_sequence(vertices, seed=None):

    if seed is not None:
        np.random.seed(seed)

    # generates a random degree sequence of just even numbers
    even_degree_sequence = np.random.randint(1, 4, size=vertices) * 2

    print("The number of routes that leads to each house is: ", even_degree_sequence)

    return even_degree_sequence


# generates a random graph with a degree seequence and eulerizes it then draws it
def make_eulerian_graph(degree_sequence, seed=None):

    print("Creating Eulerian graph...")
    G = nx.configuration_model(degree_sequence, seed=seed)
    G = nx.Graph(G)

    nx.eulerize(G)

    pos = nx.spring_layout(G)

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


# finds if there exists a eulerian path or circuit and returns it
def find_eulerians(G):

    if nx.is_eulerian(G):
        print("The graph has an Eulerian Circuit, which means it has an Eulerian Path.")
        print(list(nx.eulerian_circuit(G)))
        return list(nx.eulerian_circuit(G))
    elif nx.has_eulerian_path(G):
        print("There is an Eulerian Path in this graph.")
        print(list(nx.eulerian_path(G)))
        return list(nx.eulerian_path(G))
    else:
        print("This graph is neither Eulerian nor has an Eulerian Path.")
        return None


# draws the eulerian path or circuit given the path and the graph
# ended here, correctly draw the eulerian path onto the regular graph
def draw_eulerians(G, eulerian_path, pos):
    if eulerian_path is None:
        print("There is no Eulerian circuit or path to draw.")
        return

    # Draw the entire graph subtly
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightgray",
        edge_color="gray",
        width=1,
        node_size=300,
    )

    # Highlight the Eulerian path or circuit
    nx.draw_networkx_edges(G, pos, edgelist=eulerian_path, edge_color="red", width=2)

    # Number the edges along the Eulerian path
    for i, edge in enumerate(eulerian_path):
        node1, node2 = edge
        x1, y1 = pos[node1]
        x2, y2 = pos[node2]

        # Check if it is a self-loop
        if node1 == node2:
            # Adjust label position for self-loop
            # Use a small radial shift for the label
            angle = np.deg2rad(90)  # For example, 45 degrees in radians
            radius = 0.2  # Distance away from the node center
            dx, dy = radius * np.cos(angle), radius * np.sin(angle)
            edge_label_pos = (x1 + dx, y1 + dy)
        else:
            # Calculate the position for the edge label normally for other edges
            edge_label_pos = ((x1 + x2) / 2, (y1 + y2) / 2)

        # Annotate the edge with its order in the path
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

    sequence = generate_even_sequence(6, seed=6969)
    G, pos = make_eulerian_graph(sequence, seed=6969)
    euler = find_eulerians(G)
    if euler is not None:
        print("Eulerian path/circuit:", euler)
        draw_eulerians(G, euler, pos)
    else:
        print("No Eulerian path or circuit was found.")


if __name__ == "__main__":
    main()
