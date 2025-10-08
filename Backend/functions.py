
import requests 
import os
from dotenv import load_dotenv
load_dotenv()

STEAM_API_KEY = os.getenv('STEAM_API_KEY')    
BASE_URL = "http://api.steampowered.com"
if not STEAM_API_KEY:
    raise ValueError("Non hai settato la variabile d'ambiente STEAM_API_KEY")  #Controllo che la chiave API sia stata caricata correttamente

def get_player_summaries(steamid):                                        #Funzione per ottenere i sommari dei giocatori
    url=f"{BASE_URL}/ISteamUser/GetPlayerSummaries/v2/"
    param={
        "key":STEAM_API_KEY,
        "steamids":steamid
    }
    resp = requests.get(url, params=param)
    resp.raise_for_status()
    data=resp.json()
    return data["response"]["players"]

def get_owned_games(appids_filter):
    url=f"{BASE_URL}/ISteamUser/GetPlayerSummaries/v2/"
    param={
         "key":STEAM_API_KEY,
        "gameids":appids_filter
    }
    resp = requests.get(url, params=param)
    resp.raise_for_status()
    data=resp.json()
    return data["response"]["games"]
