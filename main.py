import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '94429b7f80c726b9eaea1da70829088b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

data_cr = {
    "name":"generate",
    "photo":"generate"
}

data_cd = {
    "pokemon_id": "27975",
    "name": "New Name",
    "photo": "generate"
}

data_ad = {
    "pokemon_id": "27975",
}


response_create = requests.post('https://api.pokemonbattle.me/v2/pokemons', headers = HEADER, json=data_cr)
print(response_create.text)


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json=data_cd)
print(response_change.text)


response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json=data_ad)
print(response_catch.text)
