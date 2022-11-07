import requests
import json

print("\t\t.:GENERACION POKEMON:.")
print("1.Generation-1\n"
      "2.Generation-2\n"
      "3.Generation-3\n"
      "4.Generation-4\n"
      "5.Generation-5\n"
      "6.Generation-6\n"
      "7.Generation-7\n"
      "8.Generation-8\n")

link_pokiapi1 = 'https://pokeapi.co/api/v2/generation/'

user_input1=input("Introduce la generacion: ")

def lista_pokemon(id1):
    resp = requests.get(link_pokiapi1+id1)

    data = resp.json()

    gen_pokemon = [gen['name'] for gen in data['pokemon_species']]
    print(f"Pokemon: {gen_pokemon} ")

for id1 in user_input1:
    lista_pokemon(id1) 

user_input2=input("Ingrese la forma que desea : ")

link_pokiapi2='https://pokeapi.co/api/v2/pokemon-shape/'

def forma_pokemon(id2):
    resp = requests.get(link_pokiapi2+id2)

    data = resp.json()

    forma_pokemon=[nombre['name'] for nombre in data['pokemon_species']]
    print(f"Lists de pokemon por forma: {forma_pokemon}")

for id2 in user_input2:
    forma_pokemon(id2)