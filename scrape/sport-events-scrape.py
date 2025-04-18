from bs4 import BeautifulSoup
import requests

url = "https://ksuowls.com/calendar?date=4/17/2025&vtype=list"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

games = soup.find_all("div")
print(games)