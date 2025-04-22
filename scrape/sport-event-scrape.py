from bs4 import BeautifulSoup
import requests

url = "https://ksuowls.com/calendar?date=4/17/2025&vtype=list"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# Each game is usually within a div or list item; inspect the site for accuracy
games = soup.find_all("li", class_="sidearm-calendar-schedule-event")

for game in games:
    game_date = game.find("h4", class_="text-uppercase")
    game_time = game.find("span", class_="sidearm-calendar-schedule-event-time")
    game_location = game.find("span", class_="text-uppercase sidearm-calendar-schedule-event-meta-value")
    game_opponent = game.find("span", class_="sidearm-calendar-schedule-event-opponent-title")

    print("Date:", game_date.get_text(strip=True) if game_date else "N/A")
    print("Time:", game_time.get_text(strip=True) if game_time else "N/A")
    print("Location:", game_location.get_text(strip=True) if game_location else "N/A")
    print("Opponent:", game_opponent.get_text(strip=True) if game_opponent else "N/A")
    print("-" * 40)
