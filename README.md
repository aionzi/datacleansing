# datacleansing
data cleansing and file management 
#TASK 2 : Data Processing, Analysis, and visualisation

This Python script performs data cleaning, transformation, visualisation, and analysis on a messy sales dataset.

#Installation
1. *Extract the project*: Download and unzip the folder anywhere on your computer.
2. *Python Version*: Make sure you’re using Python 3.8+ (This was tested on Python 3.12) 
3. *Install Dependencies*: This project uses the pandas library alongside other imports used to desl with the data. You can install it using pip. Run in your terminal:
    `pip install pandas`
    `pip install matplotlib`
    `pip install seaborn`
    `pip install sklearn` or `pip install scikit-learn`
4. *Run the Project*: Run the program through the different files for each task. T

The order of task's go:
 *Data Cleaning and Preprocessing*
 *Data Wrangling and Transformation*
 *Exploratory Data Analysis*
 *Data Visualisation*
 *Interactive Dashboard for Data Filtering*
 *Advanced Data Analysis*

#Features
- *Data Cleaning and Preprocessing*: Handle missing values using the median, mode and mean dropping duplicate values and convert all data types to the correct data type. Also detect and manage outliers in the the dataset.
- *Data Wrangling and Transformation*: Extract meaningful data and perfrom grouping and aggregation on dataset columns. Transformations are applied and new Profit Margin columns are created based on existing data.
- *Exploratory Data Analysis (EDA)*: Statistical summaries are generated and correlations between numerical variables are identified using correlation matricies. Moreoever, pivot tables are created to help analyse trends.
- *Data Visualisation*: Bar charts, histograms, scatter plots and box plots are generated using the `Seaborn` library.
- *Interactive Dashboard for Data Filtering*: User inputs are taken to  filter data, and select which plot to use to visualise the data.
- *Advanced Data Analysis*: Clustering analysis is preformed to identify clustering. Missing `Sales` values are predicted using linear regression. Moreover, a heatmap of feature correlations is generated to highlight relationships.

#File Structure
- `dataCleaningAndPreprocessing.py`: 
- Load the dataset using Pandas pd.read_csv()
• Handle missing values by dropping or imputing with mean/median.
• Identify and remove duplicate records.
• Convert data types where necessary (e.g., object to int or datetime).
• Detect and manage outliers using statistical techniques.

- `dataWranglingAndTransformation.py`
• Use Pandas functions to filter and extract meaningful data.
• Perform grouping and aggregation on dataset columns.
• Apply lambda functions and apply() methods for transformation.
• Create new computed columns based on existing data.

- `exploratoryDataAnalysis.py`
• Generate summary statistics using .describe().
• Identify correlations between numerical variables.
• Use pivot tables to analyse trends.

- `dataVisualisation.py`
• Generate bar charts, histograms, scatter plots, and box plots.
• Customise Visualisations with titles, labels, and legends.
• Use Seaborn for advanced visual styling.

- `interactiveDashboardForDataFiltering.py`
• Implement real-time interactive filtering.
• Allow users to select categories and Visualisation types dynamically.
• Generate customised Visualisations based on user input.

- `advancedDataAnalysis.py`
• Implement clustering analysis using KMeans to identify customer segments.
• Predict missing sales values using a linear regression model.
• Generate a heatmap of feature correlations to highlight relationships.

- `data-dropna.csv`: This is the cleaned dataset used.

- `messy_dataset.csv`: The messy dataset that is used.



All interactions are guided, no setup is required.
