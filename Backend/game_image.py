import requests

Game_ID = 252490
steam_game_name = f"https://steamdb.info/app/{Game_ID}/"


steam_URL = f'https://cdn.akamai.steamstatic.com/steam/apps/{Game_ID}/header.jpg?t=1675801903'


response = requests.get(steam_URL)


if response.status_code == 200:
    try:
        print('OK')
        with open('header.jpg', 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(e)
else:
    print('Game id not found')