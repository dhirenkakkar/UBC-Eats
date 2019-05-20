# UBC-Eats
A web application that visualizes UBC meal card transaction in the form of plots, heatmaps and statistical projections instead of a boring transaction column found on the student portal.


# 
- A python script scrapes one year's worth of transaction data from the university student portal. This is implemented using Selenium to perform automated button clicks, making an HTTP request and using 'Beautiful soup' lib to parse the response onto a CSV file. 
- CSV file is then used to generate descriptive statistics such as average spending per day, locations spent at etc. 
- Used python tools Pandas and Matplotlib to generates time series data (spending over time) and a heatmap.
- Integrated such that sign in button calls the python script (control flow passes onto the backend) and then outputs the returned HTML data onto the next window.


[Heatmap](https://drive.google.com/file/d/1kStBi4v3lSGTB_y3aRlrsE_rfTQ6a0fT/view?usp=sharing)  
[Pie chart](https://drive.google.com/file/d/10OIJq_XcX6Hmrle8yOVz8YCE8vjiHg0b/view?usp=sharing)
