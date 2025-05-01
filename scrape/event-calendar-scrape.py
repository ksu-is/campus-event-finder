from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the page
driver.get("https://calendar.kennesaw.edu/calendar")

time.sleep(5)
 
# Get rendered HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

h3_elements = soup.find_all('h3', class_='em-card_title')
p_elements = soup.find_all('p', class_='em-card_event-text')


for i, h3 in enumerate(h3_elements, start=1):
    print()
    print(f"--- Event {i} ---")
    
    # Get text from h3 element
    h3_text = h3.get_text(strip=True)
    print("Event:", h3_text)

    # Get text from p element
    if i-1 < len(p_elements):
        p_text = p_elements[i-1].get_text(strip=True)
        print("Date:", p_text)
    else:
        print("Date: [No corresponding Date found]")
    print()

# Close the driver
driver.quit()