import requests
def get(url):   #jag definierar en funktion som tar länken och gör den json 
    web = requests.get(url)
    return web.json()