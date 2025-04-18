# import BeautifulSoup and requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

url = "https://owllife.kennesaw.edu/events"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(60)

soup = BeautifulSoup(driver.page_source, "html.parser")

# Find all the event elements (headings, dates and times, and locations)

headings = [h3.text.strip() for h3 in soup.find_all("h3")]
print(headings)

driver.close()