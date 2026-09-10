import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    respone = requests.get(url)

    if respone.status_code == 200:
        pokemon_data = respone.json()
        return pokemon_data
    else:
        print(f"failed to retrieve data {respone.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"name: {pokemon_info["name"]}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]}")
    print(f"weight: {pokemon_info["weight"]}")


