from bs4 import BeautifulSoup
import requests

url = 'https://owllife.kennesaw.edu/events'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
events = soup.find_all('div', class_='event-card')

event_list = []
for event in events:
    title = event.find('h3').text.strip()
    date = event.find('div style', class_='event-date').text.strip()
    location = event.find('div', class_='event-location').text.strip()

    print("Title:", (title))
    print("Date:" (date))
    print("Location:" (location))
    print("---")

