from numpy import argmin, array, sqrt
import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
import numpy as np
from numpy import newaxis as na

class Cable_length_optimization_algorithms_class:

    Turbine_coordinates = None
    Substation_coordinate = None

    def __init__(self, Turbine_coordinates_input, Substation_coordinates_input ):

        self.Turbine_coordinates  = Turbine_coordinates_input
        self.Substation_coordinates = Substation_coordinates_input

    def minimum_spanning_tree(self):  # Minimum Spanning Tree

        all_coordinates = np.vstack((self.Turbine_coordinates, self.Substation_coordinates))
        x_coordinates, y_coordinates = all_coordinates[:, 0], all_coordinates[:, 1]
        x = x_coordinates
        y= y_coordinates
        d_ij = np.hypot(x - x[:, na], y - y[:, na])
        Tcsr = minimum_spanning_tree(d_ij)
        sp = (Tcsr.toarray())
        return {tuple(i): sp[tuple(i)] for i in np.argwhere(sp)}
