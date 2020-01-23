from flask_wtf import  FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class AddPokemonForm(FlaskForm):
    pokemon_id = IntegerField(label='Pokedox_ID', validators=[DataRequired()])
    name = StringField(label="Name", validators=[DataRequired(), Length(min=2, max=20)])
    image_link = StringField(label="Image Link")
    description = StringField(label="Description")
    height = StringField(label="Height", validators=[Length(max=20)])
    weight = StringField(label="Weight", validators=[Length(max=20)])
    category = StringField(label="Category", validators=[Length(max=20)])
    ability = StringField(label="Ability", validators=[Length(max=20)])



