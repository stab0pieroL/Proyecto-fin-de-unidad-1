import requests
import json



def menu():

    print("\n- - - - - - - - Bienvenido al programa de listado de Pokemon - - - - - - -")
    print("Elige la opcion segun el metodo de listado preferido.")
    print("[1] Opcion por generación")
    print("[2] Opcion por forma")
    print("[3] Opcion por habilidad")
    print("[4] Opcion por habitad")
    print("[5] Opcion por tipo")
    print("[6] Salir")

def option_1():

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