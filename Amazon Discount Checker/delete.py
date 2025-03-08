from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Path to your ChromeDriver (update it to the correct path on your system)
chrome_driver_path = "path/to/chromedriver"

# Use Service to pass the ChromeDriver path
service = Service(executable_path=chrome_driver_path)

# Initialize the Chrome driver with the service object
driver = webdriver.Chrome(service=service)

try:
    # Open the pricehistory.app website
    driver.get("https://pricehistory.app/")

    # Wait for the page to load completely
    time.sleep(5)  # You may increase the time if the page loads slowly

    # Find the search input element by its ID
    search_box = driver.find_element(By.ID, "search")

    # Enter the product link or name
    product_name = "iPhone 13"  # You can modify this with any actual product name or link
    search_box.send_keys(product_name)

    # Simulate pressing Enter to trigger the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the redirection to complete
    time.sleep(5)  # Adjust this as needed for the redirection

    # Get and print the current URL (this will be the redirected URL)
    redirected_url = driver.current_url
    print(f"Redirected to: {redirected_url}")

finally:
    # Close the browser
    driver.quit()
