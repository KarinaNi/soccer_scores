import requests

def fetch_data():
    uri = 'https://api.football-data.org/v4/matches'
    headers = { 'X-Auth-Token': '20f8c4b0e26c4a5ea68c66cdf20e55e4' }

    response = requests.get(uri, headers=headers)
    data = response.json()

    if 'matches' in data:
        for match in data['matches']:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            if match['status'] == "FINISHED":
                home_score = match['score']['fullTime']['homeTeam']
                away_score = match['score']['fullTime']['awayTeam']

                score = f"{home_score}-{away_score}"
            else:
                score = "not played yet"
            print(f"{home_team} vs {away_team}: {score}")

def display_results():
    pass
