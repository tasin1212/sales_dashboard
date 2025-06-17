import pandas as pd

# Read the CSV file
df = pd.read_csv('project 2.csv', header=None)

# Assign column names (assuming the structure based on the data)
column_names = ['Date', 'Category', 'Units_Sold', 'Revenue', 'Profit', 'Temperature']
df.columns = column_names

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display basic information about the data
print("Data Overview:")
print(df.head())
print("\nData Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Optional: Group by Category to see aggregated statistics
print("\nStatistics by Category:")
print(df.groupby('Category').describe())

# Optional: Save the processed data to a new CSV file
df.to_csv('processed_project2.csv', index=False)
print("\nProcessed data saved to 'processed_project2.csv'")