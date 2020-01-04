# Author: Bishal Sarang

from flask import Flask, render_template, request, flash, redirect
from models import load_data

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
@app.route('/index')
def index():
    return "Welcome"


@app.route('/pokedox/<string:pokemon_name>')
def pokedox(pokemon_name):
    all_pokemon_data = load_data()['pokemons']

    requested_pokemon_data = all_pokemon_data.get(pokemon_name)

    if requested_pokemon_data is not None:
        pokemon_description = requested_pokemon_data["description"]
        pokemon_info = requested_pokemon_data["info"]

        pokemon_type = pokemon_info.get("type")
        pokemon_abilities = pokemon_info.get("abilities")
        pokemon_weakness = pokemon_info.get("weakness")

        return  render_template("index.html", pokemon_name=pokemon_name, pokemon_description=pokemon_description, pokemon_type=pokemon_type, pokemon_abilities=pokemon_abilities, pokemon_weakness=pokemon_weakness)
    return "Not found"

if __name__ == "__main__":
    app.run(debug=True)