import os
import csv
import re

# Create a directory to store the images if it doesn't already exist
img_directory = 'images'
if not os.path.exists(img_directory):
    os.makedirs(img_directory)

# Function to clean the name
def clean_name(name):
    # Remove underscores and metric units
    name = name.replace('_', ' ')
    name = re.sub(r'\b\d+\s*(g|kg|grams|kilograms|oz|pounds|lbs)\b', '', name, flags=re.IGNORECASE)
    return name.strip()

# Read the existing CSV file
csv_file = 'FruitsAndVegetables.csv'
existing_products = []
if os.path.exists(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        existing_products = list(reader)

# Create a set of existing names to avoid duplicates
existing_names = set(row[0] for row in existing_products[1:] if len(row) > 0)

# Function to determine the category based on the name (can be improved if necessary)
def determine_category(name):
    name_lower = name.lower()
    if 'apple' in name_lower:
        return 'Apples'
    elif 'banana' in name_lower:
        return 'Other Fruits'
    elif 'cabbage' in name_lower:
        return 'Vegetables'
    elif 'grape' in name_lower:
        return 'Other Fruits'
    elif 'melon' in name_lower:
        return 'Melons'
    elif 'tomato' in name_lower:
        return 'Tomatoes'
    elif 'citrus' in name_lower or 'orange' in name_lower or 'lemon' in name_lower or 'lime' in name_lower:
        return 'Citrus'
    # Add more categories as needed
    return 'Other Fruits'

# List to hold new products to add to the CSV
new_products = []

# Read the images in the directory and add to CSV
for filename in os.listdir(img_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        name = filename.rsplit('.', 1)[0]
        name = name.replace('_', ' ')
        name = clean_name(name)
        image_location = os.path.join(img_directory, filename)

        # Skip products with 'box' in their name
        if 'box' in name.lower():
            print(f"Skipped product with 'box' in name: {name}")
            continue

        if name not in existing_names:
            category = determine_category(name)
            new_products.append([name, category, 3, '', image_location])  # Assuming '3' as default popularity
            existing_names.add(name)
            print(f"Added to CSV: {name}")

# Write the updated data to the CSV file
with open(csv_file, mode='a', newline='') as file:  # Open in append mode to keep existing data
    writer = csv.writer(file)
    for product in new_products:
        writer.writerow(product)

print(f"Total new products added to CSV: {len(new_products)}")
