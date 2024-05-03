import requests
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


def fetch_data():
    uri = 'https://api.football-data.org/v4/matches'
    headers = { 'X-Auth-Token': '20f8c4b0e26c4a5ea68c66cdf20e55e4' }

    response = requests.get(uri, headers=headers)
    data = response.json()
    #print(data)
    return data['matches'] if 'matches' in data else []

def display_results(matches, results_text):
    for match in matches:
        home_url = match['homeTeam']['crest']
        away_url = match['awayTeam']['crest']
        home_response = requests.get(home_url)
        away_response = requests.get(away_url)
        home_image = Image.open(BytesIO(home_response.content))
        away_image = Image.open(BytesIO(away_response.content))
        home_image = home_image.resize((100,50))
        away_image = away_image.resize((100,50))
        home_image = ImageTk.PhotoImage(home_image)
        away_image = ImageTk.PhotoImage(away_image)
        
        home_image_label = tk.Label(results_text, image = home_image)
        home_image_label.image = home_image
        home_image_label.pack(side=tk.LEFT)
        
        away_image_label = tk.Label(results_text, image = away_image)
        away_image_label.image = away_image
        away_image_label.pack(side = tk.LEFT)

        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        if match['status'] == "FINISHED":
            home_score = match['score']['fullTime']['homeTeam']
            away_score = match['score']['fullTime']['awayTeam']
            score = f"{home_score}-{away_score}"
        else:
            score = "not played yet"
        results_text.insert(tk.END, f" {home_team} vs {away_team}: {score}\n")

