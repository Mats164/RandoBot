import json
from typing import Text
from requests import get
import random

# Defines the jprint function for printing Json in a readable format
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

latest = get("http://xkcd.com/info.0.json")

insult = get("https://evilinsult.com/generate_insult.php?lang=en&type=json")

query = input('Query: ')
offset = random.randint(0, 5)
giphyParameters = {
    'api_key': 'UIX3RcfF8cUJGSBwbJAeSfuuaPeRITTx',
    'q': query,
    'limit': 1,
    'offset': offset
}

giphy = get('https://api.giphy.com/v1/gifs/search', params=giphyParameters)

gifUrl = giphy.json()['data'][0]['url']
print(gifUrl)
# jprint(giphy.json())

compendium = get('https://botw-compendium.herokuapp.com/api/v1/entry/cucco')
'''name = compendium.json()['data']['name']
location = compendium.json()['data']['common_locations']
description = compendium.json()['data']['description']
drops = compendium.json()['data']['drops']
img = compendium.json()['data']['image']
print(name)
print(', '.join(location))
print(description)
print(', '.join(drops))
print(img)
jprint(compendium.json())
'''
'''sender = 'Nuddel'
to = 'Amir'

foaasUrls = [
    f'/asshole/{sender}',
    f'/back/{to}/{sender}', 
    f'/bag/{sender}', 
    f'/because/{sender}', 
    f'/blackadder/{to}/{sender}', 
    f'/bucket/{sender}', 
    f'/bus/{to}/{sender}', 
    f'/bye/{sender}', 
    f'/chainsaw/{to}/{sender}', 
    f'/cocksplat/{to}/{sender}', 
    f'/cool/{sender}', 
    f'/cup/{sender}', 
    f'/off/{to}/{sender}', 
    f'/nugget/{to}/{sender}', 
    f'/madison/{to}/{sender}', 
    f'/looking/{sender}', 
    f'/linus/{to}/{sender}', 
]

headers = {'Accept': 'application/json'}
foaas = get(f"https://foaas.com{random.choice(urls)}", headers=headers)
# jprint(foaas.json())
print(foaas.json()['message'], '\n', foaas.json()['subtitle'])'''


'''
jprint(tronald.json())
print('\n', tronald.json()['value'])
print(latest.status_code, "\n")
jprint(latest.json())
print(latest.json()["img"])
print('\n')
print(insult.status_code, '\n')
jprint(insult.json())
print(insult.json()["insult"])'''

'''bubbles = ''
dimensions = (input('Dimensions: ')).split('x')
width = int(dimensions[0])
height = int(dimensions[1])

for i in range(height):
    for i in range(width):
        bubbles = bubbles + '||pop||'
    bubbles = bubbles + '\n'

print(bubbles)
print(len(bubbles))'''