# Optimizing Wind Farm Economics through Python Modelling and Simulation

Wind farm economics were improved through the development of a Python-based cabling optimization model and integration of that into the LandBOSSE model. The LandBOSSE model was further modified to enhance its ability to accommodate irregular wind farm layouts. The project's success was demonstrated through simulations and case studies.

The project significantly enhances wind farm economics and helps in accurate calculations of the Balance of Plant costs for wind farms,   generating more accurate economic results that mirror real-world scenarios more closely.

## Cable Optimization model

Input -  Turbine coordinates, Substation Coordinates, and Turbine Rated Power

Output - Total Cabling Costs, Total Connection Costs, Total Cabling length

* Created a comprehensive database that includes cabling specifications.
* Developed a specialized class to optimize cable length between turbines by employing a minimum spanning tree.
* Designed a class to determine the specific cable type needed for each connection.
* The main class seamlessly integrates all these components to deliver the final output and visualize the results.


Flow Chart for the Cable Optimization model

<img align="center" alt="Coding" width="500" src="https://i.imgur.com/NIZX2ug.jpg">

Result Visualization 

<img align="center" alt="Coding" width="500" src="https://i.imgur.com/v14vAKy.png">

This model is integrated into the updated LandBOSSE model

## Original LandBOSSE model 

The GitHub repository for the original LandBOSSE model can be found here - https://github.com/WISDEM/LandBOSSE.git

Read this for diving deeper into the model - https://www.nrel.gov/docs/fy19osti/72201.pdf

This is the original LandBOSSE model to which further modifications are made.


## Updated LandBOSSE model 

The google drive link for LandBOSSE model can be found here - [[https://drive.google.com/drive/folders/1gJj-m61e4zeGtEx3Jzqwq_22JqeaxbT6](https://drive.google.com/drive/folders/1gJj-m61e4zeGtEx3Jzqwq_22JqeaxbT6?usp=sharing)]


Input - Turbine and Substation Coordinates
(Additional inputs are retrieved from an Excel-based database located in the "input" folder, it is similar to the original LandBOSSE model)

Output - The generated output is an Excel spreadsheet within the database, stored in the "output" folder. The resulting structure is similar to that of the original LandBOSSE model


FLow char for the LandBOSSE model 
<img align="center" alt="Coding" width="1000" src="https://i.imgur.com/BOYtsfz.png">

The primary limitation of the initial LandBOSSE model lies in its inability to accommodate input for wind farm layout as it builds its own layout based on number of turbines and average turbine spacing. This limitation poses challenges, as it hinders the accurate estimation of Balance of Plant Costs for irregular layouts. Consequently, essential adjustments have been implemented in the original LandBOSSE model, as elaborated below.

* The model was enhanced to be invoked using the "run_landBOSSE" function, providing more user-friendly accessibility compared to the previous command-line approach.
* Specific modules, namely CollectionCost, SitePreparationCost, and ErectionCost, were revamped to compute costs based on user-provided layouts.
* Cabling Optimization model was created as a function and seamlessly integrated within these modules for improved functionality.
* Various other essential modifications were implemented to meet specific project requirements.

## Results


Significant improvements were noted in the economic results, rendering them considerably more realistic.


