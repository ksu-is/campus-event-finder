from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the page
driver.get("https://ksuowls.com/calendar?date=4/24/2025&vtype=list")

time.sleep(5)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Each game is usually within a div or list item; inspect the site for accuracy

span_str = "text: sport.title"
span_tags = soup.find_all("span", attrs={"data-bind": span_str})

h4_style_str = "formatDate: date, format: 'dddd, MMMM Do, YYYY'"
h4s = soup.find_all("h4", attrs={"data-bind": h4_style_str})

date_text = soup.find_all('h4', {'data-bind': "formatDate: date, format: 'dddd, MMMM Do, YYYY'"}).text

span_str_time = "text: time"
span_tags_time = soup.find_all("span", attrs={"data-bind": span_str_time})

print(span_tags)