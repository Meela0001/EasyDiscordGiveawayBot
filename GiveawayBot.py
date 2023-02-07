import requests
import time
import random
import os

TOKEN = os.environ['DISCORD_TOKEN']
API_BASE = "https://discordapp.com/api"
HEADERS = {
    "Authorization": f"Bot {TOKEN}",
    "User-Agent": "MyBot/0.0.1",
    "Content-Type": "application/json",
}

def get_json(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def patch_json(url, payload):
    response = requests.patch(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def start_giveaway(channel_id, message_id, end_time):
    url = f"{API_BASE}/channels/{channel_id}/messages/{message_id}"
    payload = {"content": f"Giveaway ends in {end_time} seconds."}
    patch_json(url, payload)

def end_giveaway(channel_id, message_id, winner_id):
    url = f"{API_BASE}/channels/{channel_id}/messages/{message_id}"
    payload = {"content": f"The giveaway has ended. The winner is <@{winner_id}>"}
    patch_json(url, payload)

def reroll_giveaway(channel_id, message_id, winner_id):
    url = f"{API_BASE}/channels/{channel_id}/messages/{message_id}"
    payload = {"content": f"The giveaway has ended. The winner is <@{winner_id}>"}
    patch_json(url, payload)

def handle_message(message):
    if message["content"].startswith("/start"):
        args = message["content"].split(" ")[1:]
        end_time = int(args[0])
        message_id = args[1]
        channel_id = message["channel_id"]
        start_giveaway(channel_id, message_id, end_time)
    elif message["content"].startswith("/end"):
        channel_id = message["channel_id"]
        message_id = message["id"]
        winner_id = random.choice(giveaway_entries)
        end_giveaway(channel_id, message_id, winner_id)
    elif message["content"].startswith("/reroll"):
        channel_id = message["channel_id"]
        message_id = message["id"]
        winner_id = random.choice(giveaway_entries)
        reroll_giveaway(channel_id, message_id, winner_id)
    elif message["content"].startswith("/enter"):
        author_id = message["author"]["id"]
        if author_id not in giveaway_entries:
            giveaway_entries.append(author_id)

def main
