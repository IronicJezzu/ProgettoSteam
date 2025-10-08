import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import functions 
from dotenv import load_dotenv
load_dotenv()
STEAM_API_KEY = os.getenv('STEAM_API_KEY')    
BASE_URL = "http://api.steampowered.com"

if not STEAM_API_KEY:
    raise ValueError("Non hai settato la variabile d'ambiente STEAM_API_KEY")  #Controllo che la chiave API sia stata caricata correttamente

class Player(BaseModel):     #Modello per i dati del giocatore usato da FastAPI
    profileurl: str
    personaname: str
    personastate: int
    gameextrainfo: str = None
    gameid: str = None
    avatar: str

app =  FastAPI()     #Inizializzazione dell'app FastAPI
origins = [                     #Lista di origini per il CORS
    "http://localhost:3000"
]

app.add_middleware(                 #Permette le richieste CORS dal frontend React
    CORSMiddleware,      
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STEAM_ID = "76561199096123419"

players = functions.get_player_summaries(STEAM_ID)   #Chiamata alla funzione per ottenere i sommari dei giocatori

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

@app.get("/players/", response_model=List[Player])   #Endpoint per ottenere i dati dei giocatori
async def read_players():
    return players

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)