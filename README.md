# Titanic-EDA

This notebook performs Exploratory Data Analysis (EDA) on the Titanic dataset to understand the factors that influenced passenger survival during the Titanic disaster. goal is to analyze the dataset, identify patterns, detect missing values, and explore relationships between different variables.
Through visualization and statistical analysis, we gain insights into how features such as age, gender, passenger class, fare, and family size affected survival chances.

## Dataset 
features included in the dataset:
- Feature
- 1. PassengerId
- 2. Survived (0 = No, 1 = Yes)
- 3. Pclass - Passenger class (1 = First, 2 = Second, 3 = Third)
- 4. Name
- 5. Sex -Gender of passenger
- 6. Age
- 7. SibSp - siblings/spouses aboard
- 8. Parch - parents/children aboard
- 9. Ticket
- 10. Fare
- 11. Cabin
- 12. Embarked - Port of baording

## Objectives
- Understand the structure of the dataset
- Identify missing values and data types
- Analyze distribution of variables
- relationships between features and survival
- Visualize trends using graphs and charts
- Generate insights useful for building machine learning models 
- pandas profiling

## Install dependencies
```bash
pip install -r requirements.txt
``` 
## File structure
- `pro.ipynb` - Main notebook
- `README.md` - this documentation
- `Titanic-Dataset.csv` - full dataset
- `test.csv` - test dataset
- `train.csv` - train dataset
- `output.html` - pandas profiling output file

## Steps Performed in EDA
- 1. Data Loading
- 2️. Data Inspection
- 3️.Missing Value Analysis
- 4️.Univariate Analysis
- 5️.Bivariate Analysis
- 6️.Data Visualization

## Key Insights

- Female passengers had a much higher survival rate than male passengers.
- First-class passengers had better survival chances compared to second and third class.
- Younger passengers and children showed relatively higher survival probability.
- Passengers who paid higher fares tended to survive more often.
- Cabin data contains a large number of missing values.

## How to Run 

Clone the repository
```bash
git clone https://github.com/your-username/titanic-eda.git
```

Navigate to the project folder
```bash
cd titanic-eda
```

Install required libraries
```bash
pip install -r requirements.txt
```

## Future Improvements
- Building machine learning models
- Comparing classification algorithms
- Hyperparameter tuning

## Learning Outcomes
- Practical Exploratory Data Analysis workflow
- Data cleaning techniques
- Visualization methods for insights
- Feature relationships before machine learning

