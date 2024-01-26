import pandas as pd

# Importing the data set
data = pd.read_csv("cleaned_data.csv")
# Printing the first 5 rows of the data
print(data.head())

# Getting the column names of the data
columns = list(data.columns)
print(columns)

# Finding the proporting of missing values
print("Missing values distribution: ")
print(data.isnull().mean())
print("")
