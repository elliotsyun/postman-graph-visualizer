Sure, here is a README file for your Eulerian Graph Generator script:

---

# Eulerian Graph Generator

This script generates a random Eulerian graph with a given number of vertices and attempts to find the Eulerian path or circuit within it. The Chinese Postman Problem is a famous problem in graph theory. The problem is to find the shortest path or circuit that visits every edge of a graph. This script provides a solution by generating a random Eulerian graph and finding the Eulerian path or circuit within it.

## Author
Elliot Yun

## Date
April 23, 2024

## Prerequisites

To run this script, you need the following Python packages:
- `networkx`
- `matplotlib`
- `numpy`

You can install these packages using `pip`:

```sh
pip install networkx matplotlib numpy
```

## Usage

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/postman-graph-visualizer.git
   cd chinesepostman
   ```

2. **Run the Script**:
   ```sh
   python chinesepostman.py
   ```

   You will be prompted to enter the number of houses (vertices) for the postman to travel to.

## Code Overview

### Imports

```python
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
```

These imports include necessary libraries for graph generation, plotting, and numerical operations.

### Functions

#### `generate_even_sequence(vertices, seed=None)`

Generates a sequence of even integers, representing degrees of vertices in a graph.

#### `make_eulerian_graph(degree_sequence, seed=None)`

Creates and displays an Eulerian graph from a given degree sequence.

#### `find_eulerians(G)`

Determines if the graph has an Eulerian circuit or path and returns it.

#### `draw_eulerians(G, eulerian_path, pos)`

Draws the Eulerian path or circuit on the graph.

### Main Function

The `main` function drives the script by:
1. Asking the user for the number of houses (vertices).
2. Generating an even degree sequence.
3. Creating and displaying an Eulerian graph.
4. Finding the Eulerian path or circuit.
5. Drawing the Eulerian path or circuit if it exists.

### Example

Here is a brief example of how the script might run:

```sh
Welcome to the Chinese Postman Problem Solver, which is a Eulerian circuit based graph solver.
...
How many houses do you want the postman to travel to? 10
The number of routes that leads to each house is:  [2 4 2 2 4 2 2 4 4 4]
Creating Eulerian graph...
Eulerian graph created...
The graph has an Eulerian Circuit, which means it has a Eulerian Path.
[(0, 2), (2, 5), (5, 1), (1, 6), (6, 3), (3, 0), (0, 7), (7, 4), (4, 0)]
Eulerian path/circuit: [(0, 2), (2, 5), (5, 1), (1, 6), (6, 3), (3, 0), (0, 7), (7, 4), (4, 0)]
```

## Notes

- The script uses a fixed seed for the random number generator to ensure reproducibility. You can change the seed if you want different random graphs.
- The script uses NetworkX's `eulerize` method to ensure the graph is Eulerian.
