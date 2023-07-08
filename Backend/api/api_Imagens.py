import re
import requests
from bs4 import BeautifulSoup



Game_ID = 324800
steam_game_name = f"https://store.steampowered.com/app/{Game_ID}"


steam_URL = f'https://cdn.akamai.steamstatic.com/steam/apps/{Game_ID}/header.jpg'


responseName = requests.get(steam_game_name)
response = requests.get(steam_URL)
html_content = responseName.text

soup = BeautifulSoup(html_content, "html.parser")
div_element = str(soup.find(id="appHubAppName"))


html_string = div_element

pattern = r'<div class="apphub_AppName" id="appHubAppName">(.+?)</div>'

match = re.search(pattern, html_string)

if match:
    title = match.group(1)
    print(title)  
else:
    print("Título não encontrado.")

def append_image():
    """
        A function that appends an image to 'Imagens_dos_games/header.jpg' if the response status code is 200.
    """
    
    if response.status_code == 200:
        print('OK')
        try:

            with open(f'Backend/routes/static/images/api_Imagens/header.jpg', 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(e)
    else:
        print('Game id not found')
        
append_image()
