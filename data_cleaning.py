import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("Salary_Data.csv")

# Show the first 5 rows
print("Original Data")
print(df.head())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numeric values
df = df.fillna(df.mean(numeric_only=True))

# Save cleaned data
df.to_csv("Cleaned_Salary_Data.csv", index=False)

# Display summary
print("\nSummary:")
print(df.describe())

# Create a graph
df.hist(figsize=(8,5))
plt.savefig("salary_report.png")
plt.show()

print("\nProject Completed Successfully!")