
import pandas as pd
import numpy as np

# Example dataset
df_large = pd.read_csv('path_to_raw_data.csv')

# Step 1: Handle Missing Values
df_large['Quantity'].fillna(df_large['Quantity'].median(), inplace=True)
df_large['Price'].fillna(df_large['Price'].mean(), inplace=True)
df_large['Customer ID'].fillna(df_large['Customer ID'].mode()[0], inplace=True)
df_large['Region'].fillna(df_large['Region'].mode()[0], inplace=True)

# Step 2: Remove Duplicates
df_large.drop_duplicates(inplace=True)

# Step 3: Save Cleaned Data
df_large.to_csv('cleaned_large_sales_data.csv', index=False)
