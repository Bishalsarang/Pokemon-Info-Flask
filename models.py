from __main__ import db
from datetime import datetime


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
    weaknesses = db.relationship('Weakness', backref='pokemon', lazy='dynamic')

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
