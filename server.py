# Author: Bishal Sarang
from flask import Flask, render_template
from flask_sqlalchemy import  SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = '\x024\xe6\x98\x8cq\x06mh\x90(4\xe6\xf5\xe9\xd6\xe4\x8f\x86\x91\x1f\xc0\xee\xaf'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Use sqlite://// for absolute path
# Use sqlite:/// for relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)


def create_databases():
    db.create_all()


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
        return f'Pokemon(id={self.id},id={self.name})'


class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))

    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.pokemon_id'))

    def __repr__(self):
        return f'Pokemon({self.pokemon_id},{self.type})'


class Weakness(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weakness = db.Column(db.String(20))

    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.pokemon_id'))

    def __repr__(self):
        return f'Pokemon({self.pokemon_id},{self.type})'

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/pokedox/<string:pokemon_name>')
def pokedox(pokemon_name):

    pokemon = Pokemon.query.filter(Pokemon.name==pokemon_name).first()

    if pokemon is not None:
        pokemon_name = pokemon.name
        image_link = pokemon.image_link
        pokemon_description = pokemon.description
        height = pokemon.height
        weight = pokemon.weight
        pokemon_abilities = pokemon.abilities

        return  render_template("detail.html", pokemon_name=pokemon_name, image_link= image_link, pokemon_description=pokemon_description, height=height, weight=weight, pokemon_type=["grass"], pokemon_abilities=pokemon_abilities, pokemon_weakness=["water"])
    return "Not found"

if __name__ == "__main__":
    app.run(debug=True)
