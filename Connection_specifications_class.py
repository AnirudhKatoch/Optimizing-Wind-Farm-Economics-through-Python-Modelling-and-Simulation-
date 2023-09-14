# Note
# This new class calculates the cost, name and number of each connection

from Cable_database_class import Cable_database_class
import numpy as np

Cable_Database = Cable_database_class()
Max_active_power = Cable_Database.Max_active_power
# print("Max_active_power", Max_active_power)
# print("\n")
Cable_Name = Cable_Database.Cable_Name
# print("Cable_Name", Cable_Name)
# print("\n")
Cable_CostPer_m = Cable_Database.Cable_CostPer_m
# print("Cable_CostPer_m", Cable_CostPer_m)
# print("\n")

class Connection_specifications_class:

    NameOfCable = None
    NumberOfCables = None
    TotalCostOfEachConnection = None

# Cost_Name_and_Number_of_Cables

# Input:
#     P_each_connection : A dictionary with key as the connections in the wind farm and values as the power handled
#     by each connection
#     Example : {(0, 1): 40, (1, 5): 50, (5, 8): 60, (8, 7): 70, (7, 6): 80, (6, 10): 100, (3, 0): 30, (2, 3): 20, (4, 2): 10, (9, 6): 10}
#     Optimized_cable_length_for_each_connection : A dictionary containing different connections and its optimized length in m
#     Example : {(0, 10): 33.12099032335839, (1, 2): 25.238858928247925, (1, 11): 6.082762530298219, (2, 4): 23.0, (3, 6): 15.620499351813308,
    #     (3, 11): 29.068883707497267, (5, 7): 17.46424919657298, (7, 10): 13.0, (8, 9): 33.54101966249684, (9, 10): 14.866068747318506,
    #     (9, 11): 16.15549442140351}

# Output:
#     Three different dictionaries with the name NameOfCable, NumberOfCables  and TotalCostOfEachConnection whose keys
#     hold the connections and values hold the name of cable, number of cables between each connections and total cost
#     of setting up each connection respectively.


    def __init__(self,P_each_connection, Optimized_cable_length_for_each_connection):


        Cost_of_cable, Name_of_cable, Number_of_cables = self.Calculations(P_each_connection, Optimized_cable_length_for_each_connection)
        self.TotalCostOfEachConnection = Cost_of_cable  # right now in $/m , change it to $ by multiplying the cost by length of the connection
        self.NameOfCable = Name_of_cable
        self.NumberOfCables = Number_of_cables

        print("")

    def Calculations(self,P_each_connection, Optimized_cable_length_for_each_connection):

        Closest_biggest_neighbour = {}
        Index = {}
        Name_of_cable = {}
        Cost_of_cable_per_m = {}
        Number_of_cables = {}

        for key, value in P_each_connection.items():
            for factor in range(1, 100000000000000000000000000000000000000000000000000000000000000000000000000):

                Max_active_power_value = Max_active_power * factor
                greater_values = Max_active_power_value[Max_active_power_value > value]
                if len(greater_values) > 0:
                    closest_bigger_neighbor = np.min(greater_values)
                    index_of_neighbor = np.where(Max_active_power_value == closest_bigger_neighbor)[0][0]
                    Closest_biggest_neighbour[key] = closest_bigger_neighbor
                    Index[key] = index_of_neighbor
                    Name_of_cable[key] = Cable_Name[index_of_neighbor]
                    Cost_of_cable_per_m[key] = Cable_CostPer_m[index_of_neighbor] * factor
                    Number_of_cables[key] = factor
                    break

        # # Print the dictionaries
        # print("Closest_biggest_neighbour: ", Closest_biggest_neighbour)
        # print("\n")
        # print("Index:", Index)
        # print("\n")
        # print("Number_of_cables: ", Number_of_cables)
        # print("\n")
        # print("Name_of_cable:", Name_of_cable)
        # print("\n")
        # print("Total_Cost_of_combined_cables:", Cost_of_cable_per_m)
        # print("\n")

        Cost_of_cable = {}

        for key_x, value_x in Optimized_cable_length_for_each_connection.items():
            key_y = key_x if key_x in Cost_of_cable_per_m else key_x[::-1]
            if key_y in Cost_of_cable_per_m:
                Cost_of_cable[key_y] = value_x * Cost_of_cable_per_m[key_y]

        return Cost_of_cable, Name_of_cable, Number_of_cables
