from bs4 import BeautifulSoup
import requests
import csv

url = "https://owllife.kennesaw.edu/events"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html")

print(soup)

