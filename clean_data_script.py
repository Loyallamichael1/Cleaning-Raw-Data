
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


#import pandas as pd
#import numpy as np
I imported Pandas and NumPy, essential libraries for handling and analyzing datasets.
Pandas was used for data manipulation, while NumPy provides mathematical functions.

#df_large = pd.read_csv('path_to_raw_data.csv')
The dataset was loaded into a Pandas DataFrame. This allows for easy processing and cleaning of raw data.

# df_large['Quantity'].fillna(df_large['Quantity'].median(), inplace=True)
#df_large['Price'].fillna(df_large['Price'].mean(), inplace=True)
#df_large['Customer ID'].fillna(df_large['Customer ID'].mode()[0], inplace=True)
#df_large['Region'].fillna(df_large['Region'].mode()[0], inplace=True)
Quantity: Missing values were replaced with the median, as it's robust to outliers and provides a balanced central value.
Price: Missing values were replaced with the mean, which is suitable for continuous numerical data like prices.
Customer ID: Since IDs are categorical, missing values were filled with the mode (most frequent value). This avoids introducing new IDs and maintains consistency.
Region: As a categorical field, missing values were also filled with the mode for similar reasons.
This ensures no missing data is left in the dataset, making it analysis-ready.

#df_large.drop_duplicates(inplace=True)
I removed any duplicate rows to ensure each entry in the dataset is unique. This step is crucial to avoid skewed 
analysis or overrepresentation of duplicate records.

#df_large.to_csv('cleaned_large_sales_data.csv', index=False)
After completing the cleaning process, I saved the cleaned dataset as a new CSV file.
The cleaned data is now in cleaned_large_sales_data.csv, ready for further analysis or visualization.                                               
                                                                   

