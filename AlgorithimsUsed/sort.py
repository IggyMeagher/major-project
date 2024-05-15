
import csv
import re
import os

# Define the CSV file path
csv_file = 'FruitsAndVegetables.csv'

# Read the existing CSV file
products = []
if os.path.exists(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Store the header separately
        products = list(reader)

# Function to determine if a name should be kept
def keep_variant(name):
    name_lower = name.lower()
    if 'organic' in name_lower or 'imperfect' in name_lower or 'normal' in name_lower:
        return True
    return False

# Function to clean the name by removing 'min' part
def clean_name(name):
    # Remove 'min' part and any extra spaces around it
    name = re.sub(r'\bmin\b', '', name, flags=re.IGNORECASE).strip()
    # Remove any extra spaces left
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Dictionary to store the best variant of each product
best_variants = {}

# Process each product
for product in products:
    name = clean_name(product[0])
    # Extract the base name without variants
    base_name = re.sub(r'\b(organic|imperfect|normal|each)\b', '', name, flags=re.IGNORECASE).strip()

    # Keep only organic, imperfect, and normal variants
    if keep_variant(name) or base_name not in best_variants:
        best_variants[base_name] = product
        best_variants[base_name][0] = name  # Update the name in the product

# Convert dictionary back to list
cleaned_products = [header] + list(best_variants.values())

# Write the cleaned data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cleaned_products)

print(f"Total products after cleaning: {len(cleaned_products) - 1}")
