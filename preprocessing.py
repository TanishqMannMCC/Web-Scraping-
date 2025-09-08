import pandas as pd
import numpy as np

INPUT_FILENAME = 'india_cities_population_cleaned_final.csv'
PROCESSED_OUTPUT_FILENAME = 'india_cities_preprocessed.csv'


df = pd.read_csv(INPUT_FILENAME)

print("\n Descriptive Statistics of the original data.")
# .describe() provides a statistical summary of the numerical columns
print(df.describe())

# The 'Ref' column is not needed for analysis, so we drop it.
# inplace=True modifies the DataFrame directly without needing to reassign it.
df.drop(columns=['Ref'], inplace=True)
print("\n✅ Step 3: 'Ref' column deleted successfully.")
print(f"   Columns remaining: {list(df.columns)}")

print("\n Checking for null (missing) values in each column.")
# .isnull() creates a boolean DataFrame (True for nulls), and .sum() counts the 'True' values.
print(df.isnull().sum())

# We will drop any row that has a null value in any of its columns.
rows_before_drop = df.shape[0]
df.dropna(inplace=True)
rows_after_drop = df.shape[0]
print("\n Rows with null values have been dropped.")
print(f"   Number of rows before dropping: {rows_before_drop}")
print(f"   Number of rows after dropping:  {rows_after_drop}")
print(f"   Total rows removed: {rows_before_drop - rows_after_drop}")

# This new column will show the population growth between 2001 and 2011.
df['Population Change'] = df['Population (2011)'] - df['Population (2001)']
print("\n New column 'Population Change' created successfully.")

# This new column calculates the percentage growth from 2001 to 2011.
# We use np.where to avoid division by zero if any 2001 population is 0.
df['Growth Rate (%)'] = np.where(
    df['Population (2001)'] > 0,
    (df['Population Change'] / df['Population (2001)']) * 100,0  # If 2001 population was 0, growth is 0 or undefined. We'll set to 0.
)
# Round the result to two decimal places for readability
df['Growth Rate (%)'] = df['Growth Rate (%)'].round(2)
print("\n✅ Step 7: New column 'Growth Rate (%)' created successfully.")


 # --- Step 8: Save the Processed Data to a New CSV File ---
df.to_csv(PROCESSED_OUTPUT_FILENAME, index=False)
print(f"\n✅ Step 8 (Final): Fully preprocessed data saved to '{PROCESSED_OUTPUT_FILENAME}'.")

# --- Final Output ---
print("\n--- Preprocessing Complete ---")
print("Here is a sample of the final, cleaned DataFrame:")
print(df.head())




