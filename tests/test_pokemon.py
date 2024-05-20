import requests
import pytest

URL = 'https://pokemonbattle.me/v2'
TRAINER_ID = '2377'

def test_get_trainers_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_get_trainer_name():
    responsename = requests.get('https://api.pokemonbattle.me/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responsename.status_code == 200
    assert responsename.json()["data"][0]["trainer_name"] == "Vivaldi"
