# demonstration of clicking a button with seleniumbase

from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
import os

def is_page_loaded(driver):
    return driver.execute_script('return document.readyState') == 'complete'

def click_pagination_button(driver, wait):
    try:
        # Find all pagination buttons
        pagination_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".c-grid-pagination__nav-button")))
        
        if len(pagination_buttons) >= 2:
            # Click the second pagination button
            pagination_buttons[1].click()
            print("Clicked the second pagination button")
            return True
        else:
            print(f"Not enough pagination buttons found. Total buttons: {len(pagination_buttons)}")
            return False
        
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error finding or clicking pagination button: {e}")
        return False

def scrape(driver, wait):
    try:
        # Locate the div with class m-article-grid__items
        grid_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "m-article-grid__items")))
        
        # Find all 'a' tags within the div
        links = grid_div.find_elements(By.TAG_NAME, "a")
        
        # Extract and return the href attributes
        scraped_links = [link.get_attribute("href") for link in links]
        print(f"Scraped {len(scraped_links)} links")
        
        return scraped_links
    
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error scraping links: {e}")
        return []

def dump_links_to_json(links, filename='digezz_article_links.json'):
    
    print(f"Dumping {len(links)} links to {filename}")
    
    # Read existing links if file exists
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            existing_links = json.load(f)
    else:
        existing_links = []
    
    # Append new links
    existing_links.extend(links)
    
    # Write updated links back to file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_links, f, ensure_ascii=False, indent=4)
    print(f"Appended {len(links)} links to {filename}. Total links: {len(existing_links)}")

def loop(driver, wait):
    page_number = 1
    while True:
        print(f"Processing page {page_number}")
        
        time.sleep(5)
        
        # Call the scrape function
        page_links = scrape(driver, wait)
        
        # Print the scraped links for this page
        print(f"Links scraped from page {page_number}:")
        for index, link in enumerate(page_links, start=1):
            print(f"{index}. {link}")
        
        # Dump links to JSON after each page
        
        dump_links_to_json(page_links)
        
        if click_pagination_button(driver, wait):
            page_number += 1
            # Wait for the page to load after clicking
            wait.until(is_page_loaded)
            time.sleep(2)  # Additional wait to ensure content is loaded
        else:
            print("Ending loop.")
            break
    
    # Get total number of links
    with open('digezz_article_links.json', 'r', encoding='utf-8') as f:
        all_links = json.load(f)
    print(f"Finished scraping all pages. Total links scraped: {len(all_links)}")

def delete_existing_file(filename='digezz_article_links.json'):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted existing file: {filename}")
    else:
        print(f"No existing file found: {filename}")

def main():
    # Delete existing file at the start
    delete_existing_file()

    driver = Driver(uc=True, headless=True)
    
    url = "https://www.digezz.ch"
    driver.uc_open_with_reconnect(url, reconnect_time=10)
    
    # Wait for the page to be fully loaded
    wait = WebDriverWait(driver, 20)
    try:
        wait.until(is_page_loaded)
        print("Page fully loaded")
    except TimeoutException:
        print("Page load timeout, proceeding anyway")
    
    # Try to find and click the cookie button
    try:
        button = wait.until(EC.element_to_be_clickable((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
        button.click()
        print("Cookie-Button clicked!")
    except TimeoutException:
        print('No Cookie-Button found or other exception')
    
    # Call the loop function to scrape and print links
    loop(driver, wait)
    
    time.sleep(5)
    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
