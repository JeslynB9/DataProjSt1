import pandas as pd

# Importing the data set
gqii_data = pd.read_csv("gqii_data.csv")
# Printing the first 5 rows of the data
print(gqii_data.head())

# Getting the column names of the data
columns = list(gqii_data.columns)
print(columns)

# Finding the proporting of missing values
print("Missing values distribution: ")
print(gqii_data.isnull().mean())

# Checking the datatype of each column
print("Column datatypes: ")
print(gqii_data.dtypes)

# Removing all columns except for Economy, Economy Code, GQII Scores and GQII Rank
col_keep = ['Economy Name', 'Economy Code', 'GQII Scores', 'GQII Rank'] # keep these columns
new_gqii_data = gqii_data[col_keep]
new_gqii_data.to_csv("cleaned_data.csv", index=False)

# Checking every country starts with a capital letter
country_name_column = 'Economy Name'
is_starting_with_capital = new_gqii_data[country_name_column].str[0].str.isupper()
if is_starting_with_capital.all():
    print("All country names start with a capital letter.")
else:
    print("Not all country names start with a capital letter.")

# Checking if the country code is 3 capital letters
country_code_column = 'Economy Code'  # Replace with the actual column name
is_valid_country_code = new_gqii_data[country_code_column].str.isupper() & (new_gqii_data[country_code_column].str.len() == 3)
if is_valid_country_code.all():
    print("All country codes consist of three capital letters.")
else:
    print("Not all country codes consist of three capital letters.")

# Checking data types of GQII Scores and GQII Rank columns
gqii_scores_column = 'GQII Scores'

# Check if GQII Scores are float
if new_gqii_data[gqii_scores_column].dtype == float:
    print(f"{gqii_scores_column} column contains float values.")
else:
    print(f"{gqii_scores_column} column does not contain float values.")

# Check if GQII Rank are integers
gqii_rank_column = 'GQII Rank'
if new_gqii_data[gqii_rank_column].dtype == int:
    print(f"{gqii_rank_column} column contains integer values.")
else:
    print(f"{gqii_rank_column} column does not contain integer values.")







