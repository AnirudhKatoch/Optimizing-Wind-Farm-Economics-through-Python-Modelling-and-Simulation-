import numpy as np

class Cable_database_class:

    Cable_Voltage = None
    Cable_Type = None
    Cable_Resistance = None
    Cable_Capacitance = None
    Cable_ConductorSize = None
    Cable_CostPer_m = None
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
        self.Cable_CostPer_m = self.Cable_CostPer_m_fucntion()
        self.Cable_CurrentCapacity = self.Cable_CurrentCapacity_function()
        self.Cable_inductance = self.Cable_inductance_function()
        self.Cable_mass = self.Cable_mass_function()
        self.Cable_Name = self.Cable_Name_function()
        self.Max_active_power = self.Max_active_power_fucntion()

# Cable type (array or export)

    def Cable_Type_function(self):

        Cable_Type_ = np.array( ["Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
             "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
             "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",
             "Array", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export",
             "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export",
             "Export", "Export", "Export", "Export", "Export", "Export", "Export", "Export"])

        return Cable_Type_[0:31]   # As we are only looking in cable type "Array"


# Cable Voltage in kV

    def Cable_Voltage_function(self):

        Cable_Voltage_ = np.array([30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
                                   45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45,
                                   66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66,
                                   110, 110, 110, 110, 110, 110, 110, 110,
                                   132, 132, 132, 132, 132, 132, 132, 132,
                                   150, 150, 150, 150, 150, 150, 150,
                                   220, 220, 220, 220, 275, 275, 275, 275])

        return Cable_Voltage_[0:31] # As we are only looking in cable type "Array"


# Cable Resistance in Ohm/km

    def Cable_Resistance_function(self):

        Cable_Resistance_ = np.array([0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024,
                               0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020,
                               0.195, 0.154, 0.123, 0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020,
                               0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020,
                               0.100, 0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020,
                               0.077, 0.062, 0.047, 0.038, 0.030, 0.024, 0.020,
                               0.038, 0.030, 0.024, 0.020, 0.038, 0.030, 0.024, 0.020])

        return Cable_Resistance_[0:31]


# Cable Capacitance in F/km

    def Cable_Capacitance_fucntion(self):

        Cable_Capacitance_ = np.array([0.18, 0.19, 0.21, 0.22, 0.24, 0.26, 0.29, 0.32, 0.35, 0.38,
                                       0.18, 0.19, 0.21, 0.22, 0.24, 0.26, 0.29, 0.32, 0.35, 0.38, 0.42,
                                       0.17, 0.18, 0.19, 0.2, 0.22, 0.24, 0.26, 0.29, 0.32, 0.35, 0.38,
                                       0.14, 0.15, 0.17, 0.2, 0.22, 0.24, 0.26, 0.28,
                                       0.13, 0.14, 0.16, 0.18, 0.2, 0.21, 0.23, 0.25,
                                       0.13, 0.14, 0.15, 0.17, 0.19, 0.21, 0.23,
                                       0.14, 0.16, 0.17, 0.19, 0.14, 0.16, 0.17, 0.18]) * 1e-6

        return Cable_Capacitance_[0:31]


# Cable conductor size in mm²

    def Cable_ConductorSize_fucntion(self):

        Cable_ConductorSize_ = np.array([95, 120, 150, 185, 240, 300, 400, 500, 630, 800,
                                        95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000,
                                        95, 120, 150, 185, 240, 300, 400, 500, 630, 800, 1000,
                                        185, 240, 300, 400, 500, 630, 800, 1000,
                                        185, 240, 300, 400, 500, 630, 800, 1000,
                                        240, 300, 400, 500, 630, 800, 1000,
                                        500, 630, 800, 1000,500, 630, 800, 1000])

        return Cable_ConductorSize_[0:31]


# Cable cost per length in $/m

    def Cable_CostPer_m_fucntion(self):

        Cable_CostPer_m_ = np.array([168137, 178785, 191212, 204558, 225029, 245536, 279465, 315074, 358782, 415046,
                                     178014, 191148, 209409, 225237, 254078, 283829, 327800, 374301, 431477, 509651, 593391,
                                     184822, 203875, 220497, 240625, 269362, 295776, 338878, 393004, 451030, 522430, 615498,
                                     350196, 364604, 379075, 406906, 457676, 524983, 602383, 698814,
                                     384240, 396936, 412266, 440096, 500164, 563307, 640683, 740539,
                                     475154, 491343, 520036, 560559, 601609, 689979, 783971,
                                     698363, 746089, 821646, 898585,
                                     727362, 764881, 841299, 918243]) / 1000

        return Cable_CostPer_m_[0:31]


# Cable current rating in A

    def Cable_CurrentCapacity_function(self):

        Cable_CurrentCapacity_ = np.array([300, 340, 375, 420, 480, 530, 590, 655, 715, 775,
                                           300, 340, 375, 420, 480, 530, 590, 655, 715, 775, 825,
                                           300, 340, 375, 420, 480, 530, 590, 655, 715, 775, 825,
                                           420, 480, 530, 590, 655, 715, 775, 825,
                                           420, 480, 530, 590, 655, 715, 775, 825,
                                           480, 530, 590, 655, 715, 775, 825,
                                           655, 715, 775, 825, 655, 715, 775, 825])

        return Cable_CurrentCapacity_[0:31]

# Cable inductance in H/km

    def Cable_inductance_function(self):

        Cable_inductance_ = np.array([0.44, 0.42, 0.41, 0.39, 0.38, 0.36, 0.35, 0.34, 0.32, 0.31,
                                      0.43, 0.42, 0.4, 0.39, 0.37, 0.36, 0.35, 0.33, 0.32, 0.31, 0.3,
                                      0.44, 0.43, 0.41, 0.4, 0.38, 0.37, 0.35, 0.34, 0.33, 0.32, 0.31,
                                      0.46, 0.43, 0.41, 0.38, 0.37, 0.36, 0.34, 0.33,
                                      0.47, 0.44, 0.42, 0.4, 0.38, 0.37, 0.36, 0.35,
                                      0.47, 0.44, 0.42, 0.4, 0.38, 0.37, 0.36,
                                      0.43, 0.41, 0.4, 0.38,
                                      0.44, 0.42, 0.4, 0.39]) * 1e-3

        return Cable_inductance_[0:31]


# Cables mass per length in kg/km

    def Cable_mass_function(self):

        Cable_mass_ = np.array([19.5, 20.7, 22.1, 23.6, 25.9, 28.2, 32.0, 36.0, 40.9, 47.2,
                                20.8, 22.3, 24.4, 26.2, 29.5, 32.9, 37.9, 43.2, 49.7, 58.6, 68.1,
                                21.6, 23.8, 25.7, 28, 31.3, 34.3, 39.2, 45.4, 52, 60.1, 70.7,
                                40.9, 42.5, 44.1, 47.2, 53, 60.7, 69.5, 80.5,
                                44.9, 46.3, 48, 51.1, 58, 65.2, 74, 85.4,
                                55.5, 57.3, 60.5, 65.1, 69.7, 79.8, 90.5,
                                81.3, 86.7, 95.3, 104,
                                84.7, 88.9, 97.6, 106.3]) * 1e3

        return Cable_mass_[0:31]

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
