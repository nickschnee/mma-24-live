import requests

# URL to fetch the data
url = "https://www.freepublicapis.com/api/apis?limit=10&sort=best"

# Make the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON data
    apis = response.json()
    
    # Loop through each API and print the emoji and title
    for api in apis:
        print(f"{api['emoji']} {api['title']}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
