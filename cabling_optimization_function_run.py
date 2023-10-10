from cabling_optimization_function import  cabling_optimization_function
import numpy as np

# Power of each Turbine in MW
Turbine_Power = 20.3 # MW

# Specific turbine and substation coordinates (in km)
Turbine_coordinates = np.array([(3.50,4.99),(3.70,3.20),(1.10,3.57),(3.37,3.58),(2.34,4.50),(2.53,2.01),(4.28,4.61),(1.60,3.73),(3.50,4.23),(4.39,0.68),(0.16,4.35),(3.23,3.75),(0.54,0.57),(4.85,1.96),(0.99,2.34)])
Substation_coordinate = np.array([(3.5,3.5)])

# Random turbine and substation coordinates (in km)
# Turbine_coordinates = np.random.uniform(0, 100, size=(15, 2))
# Substation_coordinate = np.random.randint(0, 100, size=(1, 2))

Total_connection_length, Total_Cabling_length ,Total_Cabling_costs = cabling_optimization_function(Turbine_Power, Turbine_coordinates,Substation_coordinate)

print(f' Total Connection Length : {Total_connection_length : .2f} km ')
print(f' Total Cabling Length : {Total_Cabling_length : .2f} km ')
print(f' Total Cabling Cost : {Total_Cabling_costs : .2f} $ ')