import requests
import json

API_URL = "https://wss-2061.key-drop.com/v1/giveaway/list"
TOKEN = "TU_TOKEN_AQUI"  # Reemplaza por tu token JWT

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7",
    "authorization": f"Bearer {TOKEN}",
    "dnt": "1",
    "origin": "https://key-drop.com",
    "referer": "https://key-drop.com/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "x-currency": "USD"
}

params = {
    "type": "active",
    "page": 0,
    "perPage": 100,
    "status": "active",
    "sort": "latest"
}

response = requests.get(API_URL, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    giveaways = data.get("giveaways", [])
    
    if not giveaways:
        print("No se encontraron sorteos activos.")
    else:
        sorted_giveaways = sorted(giveaways, key=lambda g: g.get("price", float('inf')))
        for giveaway in sorted_giveaways:
            print(f"{giveaway['name']} - ${giveaway['price']:.2f}")
else:
    print(f"Error al obtener datos: {response.status_code}\n{response.text}")
