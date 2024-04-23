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

    if not nx.is_eulerian(G):
        print("This graph is not Eulerian.")
        return None
    if nx.has_eulerian_path(G) and not nx.is_eulerian(G):
        euler = list(nx.eulerian_path(G))
        print("There is a Eulerian Path in this graph")
        return euler
    else:
        euler = list(nx.eulerian_circuit(G))
        print("The graph has a Eulerian Circuit, which means it has a Eulerian Path")
        return euler


# draws the eulerian path or circuit given the path and the graph
# ended here, correctly draw the eulerian path onto the regular graph
def draw_eulerians(G, euler):

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="black", edge_color="gray", width=1)

    path_edges = [(euler[i], euler[i + 1])]

    path_edges = [(euler[i], euler[i + 1]) for i in range(len(euler) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
    nx.draw_networkx_nodes(G, pos, node_color="red", node_size=300)
    plt.show()


def main():
    """
    print("Welcome to the Chinese Postman Problem! ")

    mailboxes = int(input("How many mailboxes do you want the postman to travel to? "))
    seed = 420

    degree_sequence = generate_even_sequence(mailboxes, seed)
    G = generate_eulerian_graph(degree_sequence, seed)

    print("Degrees of vertices:")
    for node in G.nodes:
        print(f"Vertex {node}: Degree {G.degree[node]}")
    draw_graph(G)

    if nx.is_eulerian(G):
        print("The graph is Eulerian.")
        found_path = find_eulerian_path(G)
        if found_path:
            draw_eulerian_path(G, found_path)
    else:
        print("The graph is not Eulerian.")"""

    sequence = generate_even_sequence(10, 420)
    G = make_eulerian_graph(sequence, 420)
    euler = find_eulerians(G)
    draw_eulerians(G, euler)


if __name__ == "__main__":
    main()
