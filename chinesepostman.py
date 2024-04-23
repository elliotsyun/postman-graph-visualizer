import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# This program will generate a graph with at least 2 vertices of odd degrees
# and basic visualization to represent it, and then find a Eulerian path through the graph
# and applies it to the Chinese Postman Problem

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
    nx.draw(G, with_labels=True, node_color="black", edge_color="gray", width=1)
    plt.show()

    print("Eulerian graph created...")

    return G


# finds if there exists a eulerian path or circuit and returns it
def find_eulerians(G):

    if nx.is_eulerian(G):
        print("The graph has an Eulerian Circuit, which means it has an Eulerian Path.")
        return list(nx.eulerian_circuit(G))
    elif nx.has_eulerian_path(G):
        print("There is an Eulerian Path in this graph.")
        return list(nx.eulerian_path(G))
    else:
        print("This graph is neither Eulerian nor has an Eulerian Path.")
        return None


# draws the eulerian path or circuit given the path and the graph
# ended here, correctly draw the eulerian path onto the regular graph
def draw_eulerians(G, euler):

    if euler is None:
        print("There is no eulerian circuit or path to draw.")
        return

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="black", edge_color="gray", width=1)
    path_edges = [(euler[i], euler[i + 1]) for i in range(len(euler) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
    nx.draw_networkx_nodes(G, pos, node_color="red", node_size=300)
    plt.show()


def main():

    sequence = generate_even_sequence(10, seed=69)
    G = make_eulerian_graph(sequence, seed=69)
    euler = find_eulerians(G)
    if euler is not None:
        print("Eulerian path/circuit:", euler)
        draw_eulerians(G, euler)
    else:
        print("No Eulerian path or circuit was found.")


if __name__ == "__main__":
    main()
