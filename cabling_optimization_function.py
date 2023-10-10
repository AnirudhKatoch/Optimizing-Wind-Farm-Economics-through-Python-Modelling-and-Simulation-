from Cable_length_optimization_algorithms_class import Cable_length_optimization_algorithms_class
from Connection_specifications_class import Connection_specifications_class
from Cable_database_class import Cable_database_class
from collections import defaultdict
import numpy as np


def cabling_optimization_function(Turbine_Power,Turbine_coordinates,Substation_coordinate):

    # Part 2: Cable length opmization for each connection
    #########################################################################################################################
    Cable_optimization = Cable_length_optimization_algorithms_class(Turbine_coordinates, Substation_coordinate)

    Optimized_cable_length_for_each_connection = Cable_optimization.minimum_spanning_tree_Prim_algorithm()
    # Optimized_cable_length_for_each_connection = Cable_optimization.minimum_spanning_tree_kruskal_algorithm()
    # Optimized_cable_length_for_each_connection = Cable_optimization.calculate_cable_lengths_Dijkstra_Algorithm()
    # Optimized_cable_length_for_each_connection = Cable_optimization.calculate_cable_lengths_TSP_Heuristic()
    # Optimized_cable_length_for_each_connection = Cable_optimization.minimum_spanning_tree_boruvka_algorithm()

    # print("Optimized_cable_length_for_each_connection",Optimized_cable_length_for_each_connection)
    # print("\n")

    # Total length of connection in km
    Total_connection_length = sum(Optimized_cable_length_for_each_connection.values())
    # print(f' Total Connection length: {Total_connection_length : .2f} km ')
    # print("\n")

    Connections = list(Optimized_cable_length_for_each_connection.keys())
    # print("Connections", Connections)
    # print("\n")

    # Part 3: Finding the Power handled by each connection
    #########################################################################################################################
    Point_connections = {}
    # Add the edges to the Point_connections based on your list of coordinates
    for edge in Connections:
        a, b = edge
        if a not in Point_connections:
            Point_connections[a] = []
        if b not in Point_connections:
            Point_connections[b] = []
        Point_connections[a].append(b)
        Point_connections[b].append(a)

    def dfs_paths(Point_connections, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in Point_connections:
            return []
        paths = []
        for neighbor in Point_connections[start]:
            if neighbor not in path:
                new_paths = dfs_paths(Point_connections, neighbor, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    # Find the paths to reach substation from each point
    Path_to_substaion = []
    for node in Point_connections.keys():
        Substation_coordinate_number = (len(Point_connections) - 1)
        if node != Substation_coordinate_number:
            paths = dfs_paths(Point_connections, node, Substation_coordinate_number)
            if paths:
                for path in paths:
                    Path_to_substaion.append(path)

    # print("Path_to_substaion",Path_to_substaion)
    # print("\n")

    # Each_connection_list divides Path_to_substaion based on the total edges between substation and the turbine
    Each_connection_list = [[(sublist[i], sublist[i + 1]) for i in range(len(sublist) - 1)] for sublist in
                            Path_to_substaion]
    # print("Each_connection_list",Each_connection_list)
    # print("\n")

    Each_connection = []
    for sublist in Each_connection_list:
        Each_connection.extend(sublist)
    # print("Each_connection",Each_connection)
    # print("\n")

    Connection_frequency = defaultdict(int)
    # Count the frequencies of each connection
    for item in Each_connection:  # Change that
        Connection_frequency[item] += 1
    result_dict = dict(Connection_frequency)

    # Now finding power handled by each connection in MW
    Power_handled_by_each_connection = {key: value * Turbine_Power for key, value in result_dict.items()}
    # print("Power_handled_by_each_connection",Power_handled_by_each_connection)
    # print("\n")

    # Part 4: Finding connection specifications such as cost, name and number of cables for each connection.
    #########################################################################################################################
    ConnectionSpecifications = Connection_specifications_class(Power_handled_by_each_connection,
                                                               Optimized_cable_length_for_each_connection)

    # print("TotalCostOfEachConnection", ConnectionSpecifications.TotalCostOfEachConnection)
    # print("\n")
    # print("NameOfCable", ConnectionSpecifications.NameOfCable)
    # print("\n")
    # print("NumberOfCables", ConnectionSpecifications.NumberOfCables)
    # print("\n")

    Total_cable_length_per_connection = {}

    for key_x, value_x in Optimized_cable_length_for_each_connection.items():
        key_y = key_x if key_x in ConnectionSpecifications.NumberOfCables else key_x[::-1]
        if key_y in ConnectionSpecifications.NumberOfCables:
            Total_cable_length_per_connection[key_y] = value_x * ConnectionSpecifications.NumberOfCables[key_y]

    # Total Cabling legth
    Total_Cabling_length = 0

    # Iterate through the values in the dictionary and add them to the total
    for value in Total_cable_length_per_connection.values():
        Total_Cabling_length += value

    # Print the total
    # print(f' Total Cabling Length : {Total_Cabling_length : .2f} km ')
    # print("\n")

    # Initialize a variable to store the sum
    Total_Cabling_costs = 0

    # Iterate through the values in the dictionary and add them to the total
    for value in ConnectionSpecifications.TotalCostOfEachConnection.values():
        Total_Cabling_costs += value

    # Print the total
    # print(f' Total Cabling Costs : {Total_Cabling_costs : .2f} $ ')
    # print("\n")

    return Total_connection_length, Total_Cabling_length ,Total_Cabling_costs

