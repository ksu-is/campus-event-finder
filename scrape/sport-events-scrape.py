from bs4 import BeautifulSoup
import requests

url = "https://ksuowls.com/calendar?date=4/14/2025&vtype=list"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
sport_games = soup.find_all("div", class_="event-card")

sport_games_list = []
for game in sport_games:
    sport = game.find("span data-bind").text.strip()