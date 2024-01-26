import pandas as pd

# Uploading all data sets
gini_data = pd.read_csv("cleaned_GINI.csv")
gqii_data = pd.read_csv("cleaned_gqii_data.csv")
hdi_data = pd.read_csv("cleaned_HDI.csv")
uni_data = pd.read_csv("uni_per_country.csv")

# Merging GQII and GINI
gqii_gini = gqii_data.merge(gini_data, left_on = "Economy Name", right_on = "Country Name", suffixes=(False, False))

gqii_gini.to_csv("gqii_gini.csv", index=False)

# Merging GQII, GINI and HDI
gqii_gini_hdi = gqii_gini.merge(hdi_data, left_on = "Economy Name", right_on = "Country", suffixes=(False, False))

gqii_gini_hdi.to_csv("gqii_gini_hdi.csv", index=False)

# Merging GQII, GINI, HDI and Uni
gqii_gini_hdi_uni = gqii_gini_hdi.merge(uni_data, left_on = "Economy Name", right_on = "Name of Country", suffixes=(False, False))

gqii_gini_hdi_uni.to_csv("gqii_gini_hdi_uni.csv", index=False)

# Removing columns that specify the country except for the first one
col_keep = ['Economy Name', 'Economy Code', 'GQII Scores', 'GQII Rank', '2019', '2020', '2021', 'Human Development Index (HDI) ', 'Life expectancy at birth', 'Expected years of schooling', 'Mean years of schooling', 'Gross national income (GNI) per capita', 'Development group', 'Count']
integrated_data = gqii_gini_hdi_uni[col_keep]
# Renaming columns
integrated_data = integrated_data.rename(columns={'2019': 'GINI 2019', '2020': 'GINI 2020', '2021': 'GINI 2021', 'Count': 'Ranked Universities in Top 1000'})
integrated_data.to_csv("integrated_data.csv", index=False)


