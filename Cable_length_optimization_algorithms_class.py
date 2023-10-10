# All the algorithms related to minimum spanning tree have almost the same results
# Other approaches can have different results

from numpy import argmin, array, sqrt
import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
from numpy import newaxis as na
from scipy.sparse.csgraph import shortest_path
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment


class Cable_length_optimization_algorithms_class:

    Turbine_coordinates = None
    Substation_coordinate = None

    def __init__(self, Turbine_coordinates_input, Substation_coordinate_input ):

        self.Turbine_coordinates  = Turbine_coordinates_input
        self.Substation_coordinate = Substation_coordinate_input

    def minimum_spanning_tree_Prim_algorithm(self):  # Prim's algorithm

        all_coordinates = np.vstack((self.Turbine_coordinates, self.Substation_coordinate))
        x_coordinates, y_coordinates = all_coordinates[:, 0], all_coordinates[:, 1]
        x = x_coordinates
        y= y_coordinates
        d_ij = np.hypot(x - x[:, na], y - y[:, na])
        Tcsr = minimum_spanning_tree(d_ij)
        sp = (Tcsr.toarray())
        return {tuple(i): sp[tuple(i)] for i in np.argwhere(sp)}


    def find_parent(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def minimum_spanning_tree_kruskal_algorithm(self): # Kruskal algorithm
        all_coordinates = np.vstack((self.Turbine_coordinates, self.Substation_coordinate))
        num_nodes = all_coordinates.shape[0]
        edges = []

        # Create a list of all edges with their weights
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                distance = np.linalg.norm(all_coordinates[i] - all_coordinates[j])
                edges.append((i, j, distance))

        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        parent = list(range(num_nodes))
        minimum_spanning_tree = {}

        for edge in edges:
            u, v, weight = edge
            parent_u = self.find_parent(parent, u)
            parent_v = self.find_parent(parent, v)

            if parent_u != parent_v:
                minimum_spanning_tree[(u, v)] = weight
                parent[parent_u] = parent_v

        return minimum_spanning_tree

    def calculate_cable_lengths_Dijkstra_Algorithm(self):  # Dijkstra's Algorithm
        all_coordinates = np.vstack((self.Turbine_coordinates, self.Substation_coordinate))
        num_nodes = all_coordinates.shape[0]
        distances = np.zeros((num_nodes, num_nodes))

        # Calculate distances between nodes (Euclidean distance)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                distance = np.linalg.norm(all_coordinates[i] - all_coordinates[j])
                distances[i, j] = distances[j, i] = distance

        # Use Dijkstra's Algorithm to find the shortest paths
        shortest_paths = shortest_path(distances)

        # Calculate cable lengths for each connection
        cable_lengths = {}
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                cable_lengths[(i, j)] = shortest_paths[i, j]

        max_coordinate = max(max(key) for key in cable_lengths.keys())
        cable_lengths_ = {k: v for k, v in cable_lengths.items() if max_coordinate in k}

        return cable_lengths_

    def calculate_cable_lengths_TSP_Heuristic(self): # TSP Heuristic algorithm ( This is much more efficient when used in solving Saleman Problem)
        all_coordinates = np.vstack((self.Turbine_coordinates, self.Substation_coordinate))
        num_nodes = all_coordinates.shape[0]

        # Calculate pairwise distances between nodes (Euclidean distance)
        dist_matrix = distance_matrix(all_coordinates, all_coordinates)

        # Solve TSP using the linear_sum_assignment (Hungarian) algorithm
        row_ind, col_ind = linear_sum_assignment(dist_matrix)

        # Calculate cable lengths for each connection based on the TSP solution
        cable_lengths = {}
        for i in range(num_nodes - 1):
            node1 = row_ind[i]
            node2 = row_ind[i + 1]
            cable_lengths[(node1, node2)] = dist_matrix[node1, node2]

        # Close the loop by connecting the last node to the starting node
        cable_lengths[(row_ind[-1], row_ind[0])] = dist_matrix[row_ind[-1], row_ind[0]]

        return cable_lengths


    def minimum_spanning_tree_boruvka_algorithm(self):  # Boruvka's Algorithm     (Don't use it take takes too much time)
        all_coordinates = np.vstack((self.Turbine_coordinates, self.Substation_coordinate))
        num_nodes = all_coordinates.shape[0]
        edges = []

        # Create a list of all edges with their weights
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                distance = np.linalg.norm(all_coordinates[i] - all_coordinates[j])
                edges.append((i, j, distance))

        parent = list(range(num_nodes))
        minimum_spanning_tree = {}

        while len(parent) > 1:
            # Find the nearest neighbor for each component
            nearest_neighbors = {}
            for u, v, weight in edges:
                parent_u = self.find_parent(parent, u)
                parent_v = self.find_parent(parent, v)

                if parent_u != parent_v:
                    if u not in nearest_neighbors or weight < nearest_neighbors[u][1]:
                        nearest_neighbors[u] = (v, weight)
                    if v not in nearest_neighbors or weight < nearest_neighbors[v][1]:
                        nearest_neighbors[v] = (u, weight)

            # Add the minimum edge for each component to the MST
            for u, (v, weight) in nearest_neighbors.items():
                parent_u = self.find_parent(parent, u)
                parent_v = self.find_parent(parent, v)

                if parent_u != parent_v:
                    minimum_spanning_tree[(u, v)] = weight
                    parent[parent_u] = parent_v

        return minimum_spanning_tree

