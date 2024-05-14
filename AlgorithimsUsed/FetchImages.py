import requests
from bs4 import BeautifulSoup
import os

# Create a directory to store the images if it doesn't already exist
img_directory = 'images'
if not os.path.exists(img_directory):
    os.makedirs(img_directory)

# URL of the webpage you want to scrape
url = 'https://web.archive.org/web/20231207103929/https://www.harrisfarm.com.au/collections/in-season-december'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate all containers that include both image and name
    containers = soup.find_all('div', class_='inner-product')
    
    # Loop through each container
    for container in containers:
        # Find the image element within the container
        img = container.find('img', class_='lazyOwl')
        # Extract the name from the title or link text, found in the container's caption
        name = container.find('p', class_='title').get_text(strip=True) if container.find('p', class_='title') else 'Unnamed'

        if img and 'data-src' in img.attrs:
            image_url = img['data-src']
            if image_url.startswith('//'):
                image_url = 'http:' + image_url  # Ensure the URL is complete
            
            # Sanitize the file name derived from the fruit name
            file_name = name.replace(' ', '_').replace('/', '_').replace('%', '').replace('-', '_') + '.jpg'
            
            # Download the image
            img_response = requests.get(image_url)
            if img_response.status_code == 200:
                # Save the image to a file in the 'img' directory
                with open(os.path.join(img_directory, file_name), 'wb') as f:
                    f.write(img_response.content)
                print(f"Downloaded and saved: {file_name}")
            else:
                print(f"Failed to download image from {image_url}")
        else:
            print("Image URL not found or invalid in container.")
else:
    print(f"Failed to retrieve webpage, status code: {response.status_code}")