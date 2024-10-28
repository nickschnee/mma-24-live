import requests
from bs4 import BeautifulSoup
import json

# Base URL with a placeholder for the page number
base_url = "https://www.digezz.ch/page/{}/#articles"

# Start with the first page
page_number = 1

# List to store all article links
all_links = []

while True:
    # Format the URL with the current page number
    url = base_url.format(page_number)
    
    # Make the request
    response = requests.get(url)
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check if the error message is present
    error_message = soup.find('h1', class_='m-article__headline fs-headline')
    if error_message and "Sorry, aber diese Seite gibt es nun wirklich nicht" in error_message.text:
        print("Reached a non-existent page. Stopping scrape.")
        break
    
    # Find the div with the specified class
    div = soup.find('div', class_='m-article-grid__items')
    
    # Get all <a> tags within this div and add the links to the list
    if div:
        links = div.find_all('a')
        for link in links:
            href = link.get('href')
            if href:  # Ensure the href attribute exists
                all_links.append(href)
    else:
        print(f"No div found with class 'm-article-grid__items' on page {page_number}")
    
    # Increment the page number
    page_number += 1

# Save all links to a JSON file
with open('digezz_articles.json', 'w') as f:
    json.dump(all_links, f, indent=4)

# Display the total number of articles
print(f"Total number of articles found: {len(all_links)}")
