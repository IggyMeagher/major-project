import pandas as pd
import csv

def process_csv(input_file, output_file):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print("CSV file loaded successfully.")

    # Check the first few rows to ensure the data is loaded correctly
    print("First few rows of the DataFrame:")
    print(df.head())

    # Group by category and filter out categories with fewer than 4 items
    category_counts = df['Category'].value_counts()
    print("Category counts:")
    print(category_counts)

    categories_to_move = category_counts[category_counts < 4].index
    print("Categories to move to 'Miscellaneous':")
    print(categories_to_move)

    # Move items from categories with fewer than 4 items to 'Miscellaneous'
    df['Category'] = df['Category'].apply(lambda x: 'Miscellaneous' if x in categories_to_move else x)

    # Save the updated DataFrame back to a CSV file
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Updated CSV file saved as {output_file}")

# File paths
input_file = 'FruitsAndVegetables.csv'
output_file = 'FruitsAndVegetables_Updated.csv'

# Process the CSV file
process_csv(input_file, output_file)
