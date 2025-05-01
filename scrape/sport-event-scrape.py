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

span_str_time = "text: time"
span_tags_time = soup.find_all("span", attrs={"data-bind": span_str_time})

span_str_location = "text: location"
span_tags_location = soup.find_all("span", attrs={"data-bind": span_str_location})

span_str_at_vs = "text: at_vs"
span_tags_at_vs = soup.find_all("span", attrs={"data-bind": span_str_at_vs})

span_str_opponent_title = "text: opponent.title"
span_tags_opponent_title = soup.find_all("span", attrs={"data-bind": span_str_opponent_title})

for i, span in enumerate(span_tags, start=1):
    print()
    print(f"--- Event {i} ---")
    # Get text from span element
    span_text = span.get_text(strip=True)
    print("Event:", span_text)
    # Get text from h4 element
    if i - 1 < len(h4s):
        h4_text = h4s[i - 1].get_text(strip=True)
        print("Date:", h4_text)
    else:
        print("Date: [No corresponding Date found]")
    # Get text from span element
    if i - 1 < len(span_tags_time):
        span_text_time = span_tags_time[i - 1].get_text(strip=True)
        print("Time:", span_text_time)
    else:
        print("Time: [No corresponding Time found]")
    # Get text from span element
    if i - 1 < len(span_tags_location):
        span_text_location = span_tags_location[i - 1].get_text(strip=True)
        print("Location:", span_text_location)
    else:
        print("Location: [No corresponding Location found]")
    # Get text from span element
    if i - 1 < len(span_tags_at_vs):
        span_text_at_vs = span_tags_at_vs[i - 1].get_text(strip=True)
        print("AT or VS:", span_text_at_vs.upper())
    else:
        print("AT or VS: [No corresponding At vs found]")
    # Get text from span element
    if i - 1 < len(span_tags_opponent_title):
        span_text_opponent_title = span_tags_opponent_title[i - 1].get_text(strip=True)
        print("Opponent Title:", span_text_opponent_title)
    else:
        print("Opponent Title: [No corresponding Opponent Title found]")
    print()
# Close the driver
driver.quit()
# The above code is a web scraper that uses Selenium and BeautifulSoup to extract event information from the KSU Owls sports calendar.
# It retrieves the event name, date, time, location, and opponent title for each event listed on the page.