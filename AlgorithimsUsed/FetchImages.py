import requests
from bs4 import BeautifulSoup
import csv
import os

# Define the URL and headers
url = 'https://www.woolworths.com.au/shop/browse/fruit-veg/fruit'
headers = {'User-Agent': 'Mozilla/5.0'}

# Fetch the page
print("Fetching the webpage...")
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
print("Webpage fetched.")

# Function to clean the name
def clean_name(name):
    name = name.replace('_', ' ')
    name = ' '.join([word for word in name.split() if not any(char.isdigit() for char in word)])
    return name.strip()

# Extract data from the page
products = []
print("Extracting products...")
product_tiles = soup.select('.shelfProductTile')
print(f"Found {len(product_tiles)} product tiles.")
for product in product_tiles:
    try:
        aria_label = product.select_one('.shelfProductTile-descriptionLink').get('aria-label')
        if aria_label:
            name = clean_name(aria_label.split(',')[0].strip())
            category = 'Fruit'
            image_url = product.select_one('.shelfProductTile-image img')['src']
            popularity = 3  # Default to least popular; you can implement logic to adjust this based on your criteria
            products.append([name, category, popularity, '', image_url])
            print(f"Extracted product: {name}")
        else:
            print("No aria-label found.")
    except Exception as e:
        print(f"Error extracting product: {e}")

print(f"Total products extracted: {len(products)}")

# Read the existing CSV file
csv_file = 'FruitsAndVegetables.csv'
if os.path.exists(csv_file):
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        existing_products = list(reader)
else:
    existing_products = [['Name', 'Category', 'Popularity', 'Season', 'Image Location']]

# Create a set of existing names to avoid duplicates
existing_names = set(row[0] for row in existing_products[1:])
print(f"Existing products in CSV: {len(existing_names)}")

# Write the updated data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(existing_products)
    new_entries = 0
    for product in products:
        if product[0] not in existing_names:
            writer.writerow(product)
            existing_names.add(product[0])
            new_entries += 1
            print(f"Added new product: {product[0]}")

print(f"Total new products added: {new_entries}")
