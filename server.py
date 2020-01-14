# Author: Bishal Sarang
from flask import Flask, render_template, redirect, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = '\x024\xe6\x98\x8cq\x06mh\x90(4\xe6\xf5\xe9\xd6\xe4\x8f\x86\x91\x1f\xc0\xee\xaf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Use sqlite://// for absolute path
# Use sqlite:/// for relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text)
    image_link = db.Column(db.String(20))
    height = db.Column(db.String(20))
    category = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    abilities = db.Column(db.String(20))
    date_added = db.Column(db.DateTime, default=datetime.now)

    types = db.relationship('Type', backref='pokemon', lazy='dynamic')

    def __repr__(self):
        return f'Pokemon(id={self.id},name={self.name})'


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))

    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.pokemon_id'))

    def __repr__(self):
        return f'Type(pokemon_id={self.pokemon_id},type={self.type})'


class Weakness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weakness = db.Column(db.String(20))

    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.pokemon_id'))

    def __repr__(self):
        return f'Weakness({self.pokemon_id},{self.weakness})'


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/search', methods=["GET"])
def detail_view():
    query = request.args.get("query")

    if query:
        query = query.strip().lower()
        return redirect(url_for('pokedox',pokemon_name=query))
    return abort(404)

@app.route('/add_pokemon', methods=["GET", "POST"])
def add_pokemon():
    if request.method == "POST":
        pokemon_id = request.form.get("pokemon_id")
        name = request.form.get("name")

        if pokemon_id is not None and name is not None:
            pokemon_id = int(pokemon_id.strip())
            name = name.strip().lower()

            description = request.form.get("description")
            height = request.form.get("height")
            weight = request.form.get("weight")
            category = request.form.get("category")
            ability = request.form.get("ability")

            pokemon = Pokemon(pokemon_id=pokemon_id, image_link="https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png", name=name,
                               description=description, height=height, category=category, weight=weight, abilities=ability)
            db.session.add(pokemon)


        pokemon_types = ["fire", "water", "grass", "eletric", "psychic", "steel", "normal", "fairy", "dark", "flying", "ghost", "poison", "ice", "ground", "rock", "dragon", "fighting", "bug"]

        # Types of Pokemons
        for pokemon_type in pokemon_types:
            if request.form.get(f"t_{pokemon_type}") == "on":
                db.session.add(Type(pokemon_id=pokemon_id, type=f"{pokemon_type}"))

        # Weakness of Pokemons
        for pokemon_type in pokemon_types:
            if request.form.get(f"w_{pokemon_type}") == "on":
                db.session.add(Weakness(pokemon_id=pokemon_id, weakness=f"{pokemon_type}"))

        db.session.commit()

        # Add to db
        return f"The Pokemon {name} has been added successfully."
    return render_template("add_pokemon.html")

@app.route('/pokedox/<string:pokemon_name>')
def pokedox(pokemon_name):

    pokemon = Pokemon.query.filter(Pokemon.name == pokemon_name).first()
    print(pokemon)
    if pokemon is not None:
        name = pokemon.name
        pokemon_id = pokemon.pokemon_id
        image_link = pokemon.image_link
        description = pokemon.description
        height = pokemon.height
        weight = pokemon.weight
        abilities = pokemon.abilities

        # Extract Pokemon type info
        type_query = Type.query.filter(Type.pokemon_id == pokemon_id).all()
        pk_type = [pokemon_type.type for pokemon_type in type_query]

        # Extract Pokemon weakness info
        weakness_query = Weakness.query.filter(Weakness.pokemon_id == pokemon_id).all()
        weakness = [pokemon_weakness.weakness for pokemon_weakness in weakness_query]

        print(weakness_query)
        return render_template("detail.html", name=name, image_link=image_link, description=description, height=height,
                               weight=weight, pk_type=pk_type, abilities=abilities, weakness=weakness)

    return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
