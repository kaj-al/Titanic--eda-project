This project performs Exploratory Data Analysis (EDA) on the famous Titanic dataset using Python. The objective is to analyze passenger data, identify survival patterns, and generate automated insights using Pandas Profiling (YData Profiling).<br>
EDA helps in understanding data distribution, missing values, feature relationships, and overall dataset structure before applying machine learning models.<br>

--Dataset Information<br>

The Titanic dataset contains details about passengers aboard the RMS Titanic, including demographic, ticket, and survival information.<br>
Dataset is taken from the kaggle<br>

--Objectives<br>

Understand dataset structure and data types<br>
Detect missing or inconsistent data<br>
Analyze survival trends<br>
Identify feature correlations<br>
Generate automated EDA report using Pandas Profiling<br>

--Technologies Used<br>

Python<br>
Pandas<br>
NumPy<br>
Matplotlib n<br>
Pandas Profiling / YData Profiling<br>
Jupyter Notebook<br>

--Project Workflow<br>

1.Data Loading<br>
Import dataset using Pandas<br>
Display basic dataset information<br>

2️.Data Cleaning<br>
Handle missing values<br>
Convert data types if required<br>
Remove duplicates<br>

3.Exploratory Data Analysis<br>
Statistical summary of dataset<br>
Survival analysis based on:<br>
Gender<br>
Passenger class<br>
Age group<br>
Fare distribution<br>

4. Visualization<br>
Bar charts<br>
Heatmaps<br>
Histograms<br>
Distribution plots<br>

5.Automated Report Generation<br>
Pandas Profiling generates:<br>
Data summary<br>
Missing value analysis<br>
Correlation matrix<br>
Feature distribution<br>
Duplicate detection<br>

--Pandas Profiling<br>

Pandas Profiling (now known as YData Profiling) automatically generates an interactive HTML report containing complete dataset insights.<br>

--Key Advantages<br>

Saves time in manual analysis<br>
Provides visual and statistical summaries<br>
Highlights missing data patterns<br>
Shows feature correlations<br>

--Installation<br>
Install required libraries:<br>
Copy code<br>
Bash<br>
pip install pandas numpy matplotlib seaborn ydata-profiling<br>

--Usage<br>
Run the code given in pandas_profiling.py file  to generate the profiling report<br>

--Key Insights<br>

Female passengers had higher survival rates compared to males<br>
Passengers in higher classes had better survival chances<br>
Age and fare influenced survival probability<br>
Some features contain missing values such as Age and Cabin<br>

--Output<br>

The project generates:<br>
Visual graphs and statistical summaries<br>
Interactive HTML profiling report<br>

--Future Enhancements<br>
Apply machine learning models for survival prediction<br>
Perform feature engineering<br>
Build interactive dashboards using Power BI<br>
