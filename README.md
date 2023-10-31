# Optimizing Wind Farm Economics through Python Modelling and Simulation

## Wind farm economics were improved through the development of a Python-based cabling optimization model. This model was integrated into LandBOSSE, enhancing its ability to accommodate irregular wind farm layouts. The project's success was demonstrated through simulations and case studies.

The project significantly enhances wind farm economics, aligning calculations with real-world Balance of Plant Costs. This was achieved by integrating the cable optimization model into the open-source systems engineering tool, LandBOSSE, thereby improving its flexibility and generating more accurate economic results that mirror real-world scenarios more closely.

Cable Optimization model

Input -  Turbine coordinates, Substation Coordinates, Cable Voltage and Turbine Rated Power
Output - Total Cabling Costs, Total Connection Costs, Total Cabling length

* Built a database as a class with cabling specifications
* Built a class to minize the cabling lenght between turbines utilizing minimum spanning tree
* Built a class to find a cable type required for each connection
* Main class bring all these classes together providing the final output

LandBOSSE model
