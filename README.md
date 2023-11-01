# Optimizing Wind Farm Economics through Python Modelling and Simulation

Wind farm economics were improved through the development of a Python-based cabling optimization model. This model was integrated into LandBOSSE, enhancing its ability to accommodate irregular wind farm layouts. The project's success was demonstrated through simulations and case studies.

The project significantly enhances wind farm economics, aligning calculations with real-world Balance of Plant Costs. This was achieved by integrating the cable optimization model into the open-source systems engineering tool, LandBOSSE, thereby improving its flexibility and generating more accurate economic results that mirror real-world scenarios more closely.

Cable Optimization model

Input -  Turbine coordinates, Substation Coordinates and Turbine Rated Power
Output - Total Cabling Costs, Total Connection Costs, Total Cabling length

*Created a comprehensive database that includes cabling specifications.
*Developed a specialized class to optimize cable length between turbines by employing a minimum spanning tree.
*Designed a class to determine the specific cable type needed for each connection.
*The main class seamlessly integrates all these components to deliver the final output and visualize the results.


Model Visualizations ( In progress)

Visualized Results ( In Progress)


This model is integrated into LandBOSSE model

## Original LandBOSSE model - https://github.com/WISDEM/LandBOSSE.git
(Put reference here)

The spefiications, user guidelines and software installations for the original LandBOSSE repository can be found above.

Model Visualizations( Put Reference here)

## Updated LandBOSSE model - [[https://drive.google.com/drive/folders/1gJj-m61e4zeGtEx3Jzqwq_22JqeaxbT6](https://drive.google.com/drive/folders/1gJj-m61e4zeGtEx3Jzqwq_22JqeaxbT6?usp=sharing)]

Updated LandBOSSE model

Input - Turbine and Substation Coordinates
(Additional inputs are retrieved from an Excel-based database located in the "input" folder)

Output - The generated output is an Excel spreadsheet within the database, stored in the "output" folder.


