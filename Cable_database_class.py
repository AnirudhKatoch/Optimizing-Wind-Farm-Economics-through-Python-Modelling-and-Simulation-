import numpy as np

class Cable_database_class:

    Cable_Voltage = None
    Cable_Type = None
    Cable_Resistance = None
    Cable_Capacitance = None
    Cable_ConductorSize = None
    Cable_CostPer_km = None
    Cable_CurrentCapacity = None
    Cable_inductance = None
    Cable_mass = None
    Cable_Name = None
    Max_active_power = None

    def __init__(self):

        self.Cable_Voltage = self.Cable_Voltage_function()
        self.Cable_Type = self.Cable_Type_function()
        self.Cable_Resistance = self.Cable_Resistance_function()
        self.Cable_Capacitance = self.Cable_Capacitance_fucntion()
        self.Cable_ConductorSize = self.Cable_ConductorSize_fucntion()
        self.Cable_CostPer_km = self.Cable_CostPer_km_fucntion()
        self.Cable_CurrentCapacity = self.Cable_CurrentCapacity_function()
        self.Cable_inductance = self.Cable_inductance_function()
        self.Cable_mass = self.Cable_mass_function()
        self.Cable_Name = self.Cable_Name_function()
        self.Max_active_power = self.Max_active_power_fucntion()

# Cable type (array or export)

    def Cable_Type_function(self):

        Cable_Type_ = np.array(["Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
            "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
            "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
            "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
            "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
            "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export"])

        return Cable_Type_[0:75]   # As we are only looking in cable type "Array"


# Cable Voltage in kV

    def Cable_Voltage_function(self):

        Cable_Voltage_ = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                                   20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
                                   30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
                                   45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
                                   60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60,
                                   60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60])


        return Cable_Voltage_[0:75] # As we are only looking in cable type "Array"


# Cable Resistance in Ohm/km

    def Cable_Resistance_function(self):

        Cable_Resistance_ = np.array([0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020, 0.017, 0.015, 0.013, 0.011,
             0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020, 0.017, 0.015, 0.013, 0.011,
             0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020, 0.017, 0.015, 0.013, 0.011,
             0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020, 0.017, 0.015, 0.013, 0.011,
             0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020, 0.017, 0.015, 0.013, 0.011,
             0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020, 0.017, 0.015, 0.013, 0.011])

        return Cable_Resistance_[0:75]


# Cable Capacitance in F/km

    def Cable_Capacitance_fucntion(self):

        Cable_Capacitance_ = np.array([0.33, 0.35, 0.39, 0.42, 0.47, 0.52, 0.57, 0.65, 0.72, 0.80, 0.89, 1.05, 1.15, 1.21, 1.29,
             0.22, 0.24, 0.26, 0.28, 0.31, 0.34, 0.38, 0.42, 0.47, 0.52, 0.57, 0.67, 0.74, 0.77, 0.83,
             0.17, 0.18, 0.2, 0.21, 0.23, 0.25, 0.28, 0.31, 0.34, 0.38, 0.41, 0.48, 0.53, 0.55, 0.59,
             0.17, 0.18, 0.2, 0.21, 0.23, 0.25, 0.28, 0.31, 0.34, 0.38, 0.41, 0.48, 0.53, 0.55, 0.59,
             0.16, 0.17, 0.18, 0.2, 0.21, 0.23, 0.25, 0.28, 0.31, 0.34, 0.37, 0.44, 0.48, 0.5, 0.53,
             0.16, 0.17, 0.18, 0.2, 0.21, 0.23, 0.25, 0.28, 0.31, 0.34, 0.37, 0.44, 0.48, 0.5, 0.53]) * 1e-6

        return Cable_Capacitance_[0:75]


# Cable conductor size in mm²

    def Cable_ConductorSize_fucntion(self):

        Cable_ConductorSize_ = np.array([95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000, 1200, 1400, 1600, 2000,
             95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000, 1200, 1400, 1600, 2000,
             95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000, 1200, 1400, 1600, 2000,
             95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000, 1200, 1400, 1600, 2000,
             95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000, 1200, 1400, 1600, 2000,
             95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000, 1200, 1400, 1600, 2000]
)

        return Cable_ConductorSize_[0:75]


# Cable cost per length in $/km

    def Cable_CostPer_km_fucntion(self):

        Cable_CostPer_km_ = np.array([8.068, 9.662, 11.782, 13.368, 16.546, 19.720, 25.000, 30.287, 37.154, 45.597, 56.153, 66.222, 77.859, 87.883, 107.382,
             9.203, 10.802, 12.925, 15.052, 18.236, 21.415, 26.704, 31.999, 38.876, 47.862, 58.431, 69.047, 80.701, 90.735, 110.248,
             10.902, 13.048, 15.173, 17.303, 20.494, 24.216, 29.511, 35.349, 42.771, 53.369, 64.482, 75.648, 86.255, 96.829, 118.479,
             10.902, 13.048, 15.173, 17.303, 20.494, 24.216, 29.511, 35.349, 42.771, 53.369, 64.482, 75.648, 86.255, 96.829, 118.479,
             11.475, 13.080, 15.208, 17.342, 20.536, 24.264, 29.564, 35.408, 42.301, 51.840, 62.430, 73.071, 85.285, 95.866, 115.932,
             11.475, 13.080, 15.208, 17.342, 20.536, 24.264, 29.564, 35.408, 42.301, 51.840, 62.430, 73.071, 85.285, 95.866, 115.932])*1000


        return Cable_CostPer_km_[0:75]


# Cable current rating in A

    def Cable_CurrentCapacity_function(self):

        Cable_CurrentCapacity_ = np.array([325, 365, 410, 460, 530, 600, 675, 760, 845, 930, 1005, 1145, 1210, 1265, 1345,
              325, 365, 410, 460, 530, 600, 675, 760, 845, 930, 1005, 1145, 1210, 1265, 1345,
              325, 365, 410, 460, 530, 600, 675, 760, 845, 930, 1005, 1145, 1210, 1265, 1345,
              325, 365, 410, 460, 530, 600, 675, 760, 845, 930, 1005, 1145, 1210, 1265, 1345,
              325, 365, 410, 460, 530, 600, 675, 760, 845, 930, 1005, 1145, 1210, 1265, 1345,
              325, 365, 410, 460, 530, 600, 675, 760, 845, 930, 1005, 1145, 1210, 1265, 1345]
)

        return Cable_CurrentCapacity_[0:75]

# Cable inductance in H/km

    def Cable_inductance_function(self):

        Cable_inductance_ = np.array([0.37, 0.36, 0.34, 0.33, 0.32, 0.31, 0.30, 0.29, 0.28, 0.28, 0.27, 0.26, 0.26, 0.26, 0.26,
              0.40, 0.39, 0.37, 0.36, 0.35, 0.33, 0.32, 0.31, 0.30, 0.30, 0.29, 0.28, 0.28, 0.27, 0.27,
              0.43, 0.41, 0.40, 0.38, 0.37, 0.36, 0.35, 0.33, 0.32, 0.31, 0.30, 0.29, 0.29, 0.28, 0.28,
              0.43, 0.41, 0.40, 0.38, 0.37, 0.36, 0.35, 0.33, 0.32, 0.31, 0.30, 0.29, 0.29, 0.28, 0.28,
              0.44, 0.42, 0.41, 0.39, 0.38, 0.37, 0.35, 0.34, 0.33, 0.32, 0.31, 0.30, 0.29, 0.29, 0.29,
              0.44, 0.42, 0.41, 0.39, 0.38, 0.37, 0.35, 0.34, 0.33, 0.32, 0.31, 0.30, 0.29, 0.29, 0.29]) * 1e-3

        return Cable_inductance_[0:75]


# Cables mass per length in kg/km

    def Cable_mass_function(self):

        Cable_mass_ = np.array([1.5, 1.8, 2.2, 2.5, 3.1, 3.7, 4.7, 5.7, 7.0, 8.6, 10.6, 12.5, 14.7, 16.6, 20.3,
              1.7, 2, 2.4, 2.8, 3.4, 4.0, 5.0, 6.0, 7.3, 9.0, 11.0, 13.0, 15.2, 17.1, 20.8,
              2, 2.4, 2.8, 3.2, 3.8, 4.5, 5.5, 6.6, 8.0, 10.0, 12.1, 14.2, 16.2, 18.2, 22.3,
              2, 2.4, 2.8, 3.2, 3.8, 4.5, 5.5, 6.6, 8.0, 10.0, 12.1, 14.2, 16.2, 18.2, 22.3,
              2.1, 2.4, 2.8, 3.2, 3.8, 4.5, 5.5, 6.6, 7.9, 9.7, 11.7, 13.7, 16, 18, 21.8,
              2.1, 2.4, 2.8, 3.2, 3.8, 4.5, 5.5, 6.6, 7.9, 9.7, 11.7, 13.7, 16, 18, 21.8]) * 1e3

        return Cable_mass_[0:75]

# Cable names

    def Cable_Name_function(self):

        Cable_Name_array = np.array([])

        for i in range(len(self.Cable_Voltage)):
            name = "XLPE_" + str(self.Cable_ConductorSize[i]) + "mm_" + str(self.Cable_Voltage[i]) + "kV"
            Cable_Name_array = np.append(Cable_Name_array, name)

        return Cable_Name_array

# Max Cable active power in MW

    def Max_active_power_fucntion(self):

        f = 50 # Hz # frequency in ht grid

        # Calculate characteristic impedance
        Char_Impedance = np.sqrt((self.Cable_Resistance + 2j * np.pi * f * self.Cable_inductance) /
                                 ((1 / self.Cable_Resistance) + 2j * np.pi * f * self.Cable_Capacitance))

        # Calculate phase angle in radians
        Phase_angle = np.arctan2(np.imag(Char_Impedance), np.real(Char_Impedance))

        # Calculate power factor
        Power_factor = np.cos(Phase_angle)

        # Max active power in MW
        # The calculations are hand verified
        Max_active_power_array = np.sqrt(3) * self.Cable_Voltage * self.Cable_CurrentCapacity * Power_factor / 1000

        return Max_active_power_array
