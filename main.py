from Cable_length_optimization_algorithms_class import Cable_length_optimization_algorithms_class
from Connection_specifications_class import Connection_specifications_class
from Cable_database_class import Cable_database_class
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt


# Part 1: Inputs
#########################################################################################################################
# Power of each Turbine in MW
Turbine_Power = 25 # MW

# Random turbine and substation coordinates (in meter)
Turbine_coordinates = np.random.randint(0, 100, size=(10, 2))
Substation_coordinate = np.random.randint(0, 100, size=(1, 2))

# Specific turbine and substation coordinates (in meter)
# Turbine_coordinates = np.array([(6, 61), (97, 69), (31, 50), (6, 91), (44, 45), (56, 70), (25, 71), (31, 54), (57, 72), (92, 9)])
# Substation_coordinate = np.array([(69, 80)])


# Part 2: Cable length opmization for each connection
#########################################################################################################################
Cable_optimization = Cable_length_optimization_algorithms_class(Turbine_coordinates, Substation_coordinate)
Optimized_cable_length_for_each_connection = Cable_optimization.minimum_spanning_tree()
# print("Optimized_cable_length_for_each_connection",Optimized_cable_length_for_each_connection)
# print("\n")
Connections =  list(Optimized_cable_length_for_each_connection.keys())
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
    if node != Substation_coordinate_number :
        paths = dfs_paths(Point_connections, node, Substation_coordinate_number)
        if paths:
            for path in paths:
                Path_to_substaion.append(path)

# print("Path_to_substaion",Path_to_substaion)
# print("\n")

# Each_connection_list divides Path_to_substaion based on the total edges between substation and the turbine
Each_connection_list = [[(sublist[i], sublist[i+1]) for i in range(len(sublist)-1)] for sublist in Path_to_substaion]
# print("Each_connection_list",Each_connection_list)
# print("\n")

Each_connection = []
for sublist in Each_connection_list:
    Each_connection.extend(sublist)
# print("Each_connection",Each_connection)
# print("\n")

Connection_frequency = defaultdict(int)
# Count the frequencies of each connection
for item in Each_connection: # Change that
    Connection_frequency[item] += 1
result_dict = dict(Connection_frequency)

# Now finding power handled by each connection in MW
Power_handled_by_each_connection = {key: value * Turbine_Power for key, value in result_dict.items()}
# print("Power_handled_by_each_connection",Power_handled_by_each_connection)
# print("\n")


# Part 4: Finding connection specifications such as cost, name and number of cables for each connection.
#########################################################################################################################
ConnectionSpecifications = Connection_specifications_class(Power_handled_by_each_connection,Optimized_cable_length_for_each_connection)

# print("TotalCostOfEachConnection", ConnectionSpecifications.TotalCostOfEachConnection)
# print("\n")
# print("NameOfCable", ConnectionSpecifications.NameOfCable)
# print("\n")
# print("NumberOfCables", ConnectionSpecifications.NumberOfCables)
# print("\n")


# Initialize a variable to store the sum
Total_Cabling_costs = 0

# Iterate through the values in the dictionary and add them to the total
for value in ConnectionSpecifications.TotalCostOfEachConnection.values():
    Total_Cabling_costs += value

# Print the total
print(f' Total Cabling Costs : {Total_Cabling_costs : .2f} $ ')


# Part 5: Displaying the results in graph
#########################################################################################################################

Optimized_cable_length_for_each_connection_sorted  = {}

for key_x, value_x in Optimized_cable_length_for_each_connection.items():
    key_y = key_x if key_x in Power_handled_by_each_connection else key_x[::-1]
    if key_y in Power_handled_by_each_connection:
        Optimized_cable_length_for_each_connection_sorted[key_y] = value_x

# print("Optimized_cable_length_for_each_connection_sorted",Optimized_cable_length_for_each_connection_sorted)
# print("\n")

NameOfCable = ConnectionSpecifications.NameOfCable
NumberOfCables = ConnectionSpecifications.NumberOfCables

all_coordinates = np.vstack((Turbine_coordinates, Substation_coordinate))

# Extract the unique all_coordinates from the connections
unique_coordinates = list(set(coord for connection in Optimized_cable_length_for_each_connection_sorted.keys() for coord in connection))
# print("unique_coordinates",unique_coordinates)

fig, ax = plt.subplots(figsize=(8, 6))

# Create a dictionary to store cable colors
cable_colors = {}

# Plot coordinates
for idx, (x, y) in enumerate(all_coordinates):
    if idx == len(all_coordinates) - 1:
        ax.plot(x, y, 'ro', markersize=8, label='Starting Point (S)')
        ax.text(x, y + 2, 'S', fontsize=12, ha='center')
    else:
        ax.plot(x, y, 'ko', markersize=8)

# Plot lines based on connections and add labels for cable count
for connection, _ in NameOfCable.items():
    start_coord, end_coord = connection
    start_x, start_y = all_coordinates[start_coord]
    end_x, end_y = all_coordinates[end_coord]
    num_cables = NumberOfCables.get(connection, 1)
    name_cables = NameOfCable.get(connection, 1)

    # Assign a unique color to each cable type
    if name_cables not in cable_colors:
        cable_colors[name_cables] = plt.cm.jet(len(cable_colors) / len(NameOfCable))

    cable_color = cable_colors[name_cables]

    ax.plot([start_x, end_x], [start_y, end_y], '--', linewidth=1.0, color=cable_color)
    mid_x = (start_x + end_x) / 2
    mid_y = (start_y + end_y) / 2
    if num_cables == 1:
        ax.text(mid_x, mid_y, f'{num_cables} Cable', fontsize=8, color=cable_color)
    else:
        ax.text(mid_x, mid_y, f'{num_cables} Cables', fontsize=8, color=cable_color)

# Set labels for coordinates
for idx, (x, y) in enumerate(all_coordinates):
    if not idx == len(all_coordinates) - 1:
        ax.text(x + 2, y + 2, f'T{idx + 1}', fontsize=10)

# Add legend for cable names and colors
handles = []
for cable_name, color in cable_colors.items():
    handles.append(plt.Line2D([0], [0], marker='o', color='w', label=f'{cable_name}', markersize=8, markerfacecolor=color))

# Place the legend outside of the graph
legend = ax.legend(handles=handles, loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Add labels, title, and enable gridlines
# plt.xlabel('X')
# plt.ylabel('Y')
plt.title(f'Cabling optimization')
# plt.xlim(0,100)
# plt.ylim(0,100)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

# End
##########################################################################################################################3