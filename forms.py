from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class AddPokemonForm(FlaskForm):
    pokemon_id = StringField(label='Pokedox_ID', validators=[DataRequired(), Length(min=1, max=3, message="Pokedox Id should be three digits maximum")])
    name = StringField(label="Name", validators=[DataRequired(), Length(min=2, max=20)])
    image_link = StringField(label="Image Link", validators=[Length(max=20)])
    description = StringField(label="Description")
    height = StringField(label="Height", validators=[Length(max=20)])
    weight = StringField(label="Weight", validators=[Length(max=20)])
    category = StringField(label="Category", validators=[Length(max=20)])
    ability = StringField(label="Ability", validators=[Length(max=20)])



