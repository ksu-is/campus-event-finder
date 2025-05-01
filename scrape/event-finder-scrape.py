from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
 
# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 
# Load the page
driver.get("https://owllife.kennesaw.edu/events")
 
# Wait for JavaScript to load (adjust time if needed)
time.sleep(5)
 
# Get rendered HTML
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
 
# Extract h3 headings
 
 
h3_style_str = 'font-size: 1.06rem; font-weight: 600; overflow: visible; margin: 0.125rem 0px 0.313rem; line-height: 1.313rem; display: -webkit-box; max-width: 400px; -webkit-line-clamp: 2; -webkit-box-orient: vertical; text-overflow: initial;'
h3s = soup.find_all('h3', attrs={'style': h3_style_str})
 
div_style_str = 'margin: 0px 0px 0.125rem;'
target_divs = soup.find_all('div', attrs={'style': div_style_str}) 
 
for i, target in enumerate(target_divs, start=1):
    print()
    print(f"--- Event {i} ---")
    
    if i-1 < len(h3s):
        h3_text = h3s[i-1].get_text(strip=True)
        print("Event:", h3_text)
    else:
        print("Event: [No corresponding Event found]")
 
    # Get text from target div
    target_text = target.get_text(strip=True)
    print("Date:", target_text)
 
    # Find the immediate next sibling div
    sibling = target.find_next_sibling()
    while sibling and sibling.name != 'div':
        sibling = sibling.find_next_sibling()
 
    if sibling:
        # Remove svg if present
        svg = sibling.find('svg')
        if svg:
            svg.decompose()
 
        sibling_text = sibling.get_text(strip=True)
        print("Location:", sibling_text)
        print()

# Close the driver
driver.quit()