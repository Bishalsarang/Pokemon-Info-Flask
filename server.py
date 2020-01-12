# Author: Bishal Sarang

from flask import Flask, render_template, request, flash, redirect, url_for
from models import load_data

app = Flask(__name__)
app.secret_key = '\x024\xe6\x98\x8cq\x06mh\x90(4\xe6\xf5\xe9\xd6\xe4\x8f\x86\x91\x1f\xc0\xee\xaf'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/pokedox/<string:pokemon_name>')
def pokedox(pokemon_name):
    all_pokemon_data = load_data()['pokemons']
    # print(pokemon_name)
    requested_pokemon_data = all_pokemon_data.get(pokemon_name)
    print(all_pokemon_data)
    if requested_pokemon_data is not None:
        pokemon_description = requested_pokemon_data["description"]
        pokemon_info = requested_pokemon_data["info"]

        image_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/003.png"
        height = pokemon_info.get("height")
        weight = pokemon_info.get("weight")
        pokemon_type = pokemon_info.get("type")
        pokemon_abilities = pokemon_info.get("abilities")
        pokemon_weakness = pokemon_info.get("weakness")

        return  render_template("detail.html", pokemon_name=pokemon_name, pokemon_description=pokemon_description, height=height, weight=weight, pokemon_type=pokemon_type, pokemon_abilities=pokemon_abilities, pokemon_weakness=pokemon_weakness)
    return "Not found"


if __name__ == "__main__":
    app.run(debug=True)
