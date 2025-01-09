# Cleaning-Raw-Data
🧹 Raw Data Cleaning Project This project focuses on transforming raw data into analysis-ready formats. Key tasks include resolving missing or inconsistent data, removing duplicates and outliers, and standardizing datasets for accuracy. It highlights effective data cleaning practices to ensure data integrity and support better decision-making.


Missing Data and Fixes

1. Missing Values:
   
• Quantity: Some rows had missing values in the Quantity column.

• Fix: Replaced missing values with the median of the Quantity column to maintain the distribution and avoid introducing bias.

• Price: Some rows had missing values in the Price column.

• Fix: Filled missing Price values with the mean of the column to keep the overall price range intact.

• Customer ID: There were missing values in the Customer ID column.

• Fix: Filled missing Customer ID values with the mode (the most common value) to ensure consistency in customer identification.

• Region: Some rows had missing Region values.

• Fix: Replaced missing Region values with the mode of the Region column, ensuring all regions were represented correctly.



What Was Fixed:

• Replaced missing values with appropriate statistics (median for Quantity, mean for Price, and mode for Customer ID and Region).

• No rows with missing data remain in the dataset after imputation.

