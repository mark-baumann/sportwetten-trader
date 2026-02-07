import requests
import json

api_key = "YOUR_API_KEY"
sport_key = "basketball_nba"
regions = "us"
markets = "h2h"
odds_format = "decimal"
date_format = "iso"

url = f"https://api.the-odds-api.com/v4/sports/{sport_key}/odds/?apiKey={api_key}&regions={regions}&markets={markets}&oddsFormat={odds_format}&dateFormat={date_format}"

response = requests.get(url)
data = response.json()

thunder_games = []
for game in data:
    if "Oklahoma City Thunder" in game["home_team"] or "Oklahoma City Thunder" in game["away_team"]:
        thunder_games.append(game)

print(json.dumps(thunder_games, indent=4))