import pandas as pd

# Load pivoted data from CSV
input_file = 'PivotDataMilk.csv'         # Replace with your file path
output_file = 'tabular_pricesMilk.csv' # Output file name

# Read CSV into a DataFrame
df_pivot = pd.read_csv(input_file)

# Melt the DataFrame to tabular format
df_tabular = pd.melt(df_pivot,
                     id_vars=['State'],
                     var_name='Month',
                     value_name='Price')

# Drop rows where Price is NaN or empty
df_tabular.dropna(subset=['Price'], inplace=True)

# Optional: Reset index
df_tabular.reset_index(drop=True, inplace=True)

# Save to new CSV
df_tabular.to_csv(output_file, index=False)

print("✅ Tabular data saved to:", output_file)