import pandas as pd

# Import the data set and print the first 5 rows
gqii_data = pd.read_csv("cleaned_data.csv")
print(gqii_data.head())

# Save each column to a list in different variables
eco_name = gqii_data["Economy Name"]
eco_code = gqii_data["Economy Code"]
score = gqii_data["GQII Scores"]
rank = gqii_data["GQII Rank"]

western_european_regions = ["Germany", "France", "Netherlands", "Belgium", "Austria", "Switzerland", "Luxembourg", "Liechtenstein", "Monaco"]

western_european_df = gqii_data[gqii_data["Economy Name"].isin(western_european_regions)]

avg_score = western_european_df["GQII Scores"].mean()



# Print the average GQII Score for Western Europe Countries
print("The average score in Western European Countries is:", avg_score)

# Print the maximum GQII Score
print("The maximum score is:", score.max())

# Print the minimum GQII Score
print("The minimum score is:", score.min())
