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
    home_images = []  # List to store references to home images
    away_images = []  # List to store references to away images

    for match in matches:
        home_url = match['homeTeam']['crest']
        away_url = match['awayTeam']['crest']
        home_response = requests.get(home_url)
        away_response = requests.get(away_url)
        home_image = Image.open(BytesIO(home_response.content)).resize((50, 50))  
        away_image = Image.open(BytesIO(away_response.content)).resize((50, 50))  
        home_image = ImageTk.PhotoImage(home_image)
        away_image = ImageTk.PhotoImage(away_image)

        home_images.append(home_image)  
        away_images.append(away_image) 
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        if match['status'] == "FINISHED":
            home_score = match['score']['fullTime']['homeTeam']
            away_score = match['score']['fullTime']['awayTeam']
            score = f"{home_score}-{away_score}"
        else:
            score = "not played yet"
        
        results_text.image_create(tk.END, image=home_image)
        results_text.insert(tk.END, f" {home_team} ")
        results_text.image_create(tk.END, image=away_image)
        results_text.insert(tk.END, f" {away_team}: {score}\n")

    results_text.home_images = home_images
    results_text.away_images = away_images


