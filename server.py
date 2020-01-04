# Author: Bishal Sarang

from flask import Flask, render_template, request, flash, json
from models import load_data

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/pokedox/<string:pokemon_name>')
def pokedox(pokemon_name):
    all_pokemon_data = load_data()['pokemons']

    requested_pokemon_data = all_pokemon_data.get(pokemon_name)
    requested_pokemon_description = requested_pokemon_data["description"]
    requested_pokemon_info = requested_pokemon_data["info"]

    requested_pokemon_type = requested_pokemon_data.get("type")
    requested_pokemon_weakness = requested_pokemon_data.get("weakness")

    return   render_template("index.html", pokemon_name=pokemon_name, requested_pokemon_description=requested_pokemon_description)


if __name__ == "__main__":
    app.run(debug=True)