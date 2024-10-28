from seleniumbase import Driver
from bs4 import BeautifulSoup
import time

def main():
    
    print("Starting Chrome")
    # Initialize the SeleniumBase driver with Undetectable Chrome (UC) and Headless
    driver = Driver(uc=True, headless=True)
    
    try:
        # Define URL to open
        url = "https://www.digezz.ch"
        
        # Open the URL with a reconnect time
        driver.uc_open_with_reconnect(url, reconnect_time=10)
        
        # Wait a moment to ensure full JS rendering if needed
        time.sleep(3)
        
        # Get the page source after rendering
        page_source = driver.get_page_source()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(page_source, "html.parser")
        
        # Extract desired content, e.g., the entire HTML
        print(soup.prettify())
        
    finally:
        # Quit the driver to close the browser
        driver.quit()

if __name__ == "__main__":
    main()
