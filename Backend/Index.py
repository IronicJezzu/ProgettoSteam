import os
import functions 
from dotenv import load_dotenv
load_dotenv()
STEAM_API_KEY = os.getenv('STEAM_API_KEY')    
BASE_URL = "http://api.steampowered.com"




if not STEAM_API_KEY:
    raise ValueError("Non hai settato la variabile d'ambiente STEAM_API_KEY")



STEAM_ID = "76561199096123419"

players = functions.get_player_summaries(STEAM_ID)

for p in players:
    print("URLprofilo", p.get("profileurl"))
    print("Nome", p.get("personaname"))
    
    if p.get("personastate") == 1 :
        print("Stato","Online")
    else:
        print("Stato","Offline")
    
    if p.get("gameid") is None:
        print("Non sta giocando a nulla")
    else:
        print("Sta giocando a ", p.get("gameextrainfo"))