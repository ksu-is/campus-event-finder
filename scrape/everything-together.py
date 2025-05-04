from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv
import json

# Set up driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def scrape_ksu_athletics():
    url = "https://ksuowls.com/calendar?date=5/01/2025&vtype=list"
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    span_tags = soup.find_all("span", attrs={"data-bind": "text: sport.title"})
    h4s = soup.find_all("h4", attrs={"data-bind": "formatDate: date, format: 'dddd, MMMM Do, YYYY'"})
    times = soup.find_all("span", attrs={"data-bind": "text: time"})
    locations = soup.find_all("span", attrs={"data-bind": "text: location"})
    at_vs = soup.find_all("span", attrs={"data-bind": "text: at_vs"})
    opponents = soup.find_all("span", attrs={"data-bind": "text: opponent.title"})

    data = []
    for i, span in enumerate(span_tags):
        data.append({
            "Source": "KSU Athletics",
            "Event": span.get_text(strip=True),
            "Date": h4s[i].get_text(strip=True) if i < len(h4s) else "N/A",
            "Location": locations[i].get_text(strip=True) if i < len(locations) else "N/A",
            "Opponent": opponents[i].get_text(strip=True) if i < len(opponents) else "N/A"
        })
    return data


def scrape_owl_life():
    url = "https://owllife.kennesaw.edu/events"
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    h3s = soup.find_all('h3', attrs={'style': 'font-size: 1.06rem; font-weight: 600; overflow: visible; margin: 0.125rem 0px 0.313rem; line-height: 1.313rem; display: -webkit-box; max-width: 400px; -webkit-line-clamp: 2; -webkit-box-orient: vertical; text-overflow: initial;'})
    date_divs = soup.find_all('div', attrs={'style': 'margin: 0px 0px 0.125rem;'})

    data = []
    for i, div in enumerate(date_divs):
        location = "N/A"
        sibling = div.find_next_sibling()
        while sibling and sibling.name != 'div':
            sibling = sibling.find_next_sibling()
        if sibling:
            svg = sibling.find('svg')
            if svg:
                svg.decompose()
            location = sibling.get_text(strip=True)

        data.append({
            "Source": "Owl Life",
            "Event": h3s[i].get_text(strip=True) if i < len(h3s) else "N/A",
            "Date": div.get_text(strip=True),
            "Location": location
        })
    return data


def scrape_ksu_calendar():
    url = "https://calendar.kennesaw.edu/calendar"
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    titles = soup.find_all('h3', class_='em-card_title')
    descriptions = soup.find_all('p'[0], class_='em-card_event-text')

    data = []
    for i, title in enumerate(titles):
        data.append({
            "Source": "KSU Calendar",
            "Event": title.get_text(strip=True),
            "Date": descriptions[i].get_text(strip=True) if i < len(descriptions) else "N/A"
        })
    return data


# Collect and combine all scraped data
all_data = scrape_ksu_athletics() + scrape_owl_life() + scrape_ksu_calendar()

# Close driver after scraping
driver.quit()

for event in all_data:
    print(event)

#Export to CSV
csv_headers = sorted({key for event in all_data for key in event})
with open("ksu_combined_events.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(all_data)

# Export to JSON
with open("ksu_combined_events.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2)