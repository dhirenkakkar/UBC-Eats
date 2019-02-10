# UBC-Eats
A web application that visualizes UBC meal card transaction in the form of plots, heatmaps and statistical projections instead of a boring transaction column found on the student portal.


# Working 
* Backend - A python script scrapes one year's worth of transaction data from the university student portal. This is performed using Selenium to perform automated button clicks and beutiful soup to make HTTP request and write the parsed response onto a CSV file. 
- Generates descriptive statistics such as average spending per day, locations spent, per account, etc. 
- Generates time series data (spending over time) and a heatmap using python tools Numpy, Matplotlib and Pandas.

* Frontend - Integrated such that sign in button calls the python script (control flow passes onto the backend) and then outputs the returned HTML data onto the next window.


[alt tag](https://drive.google.com/file/d/1kStBi4v3lSGTB_y3aRlrsE_rfTQ6a0fT/view?usp=sharing)
