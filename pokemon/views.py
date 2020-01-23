from pokemon import app, db
from flask import render_template, redirect, url_for, abort, request
from pokemon.forms import AddPokemonForm
import pokemon.models as models


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/list')
def list_view():
    pokemons = models.Pokemon.query.all()

    pokemon_info = []
    for pokemon in pokemons:
        # Get Types of current Pokemon using one to multiple queries: types =
        # db.relationship('Type', backref='pokemon', lazy='dynamic')
        types = pokemon.types.all()
        types = [pk_type.type for pk_type in types]

        # Get Weakness of current Pokemon
        weaknesses = pokemon.weaknesses.all()
        weaknesses = [weakness.weakness for weakness in weaknesses]

        pokemon_num, name, description, image_url, category, height, weight = pokemon.pokemon_id,pokemon.name, pokemon.description, pokemon.image_link, pokemon.category, pokemon.height, pokemon.weight
        pokemon_info.append((pokemon_num, name, description, image_url, category, height, weight,
                             types, weaknesses))
    return render_template('list.html', pokemon_info=pokemon_info)


@app.route('/search', methods=["GET"])
def detail_view():
    q = request.args.get("q")

    if q:
        try:
            queried_pokemon_name = models.Pokemon.query.filter(
                models.Pokemon.pokemon_id == int(q)).first()
            return redirect(
                url_for('pokedox', pokemon_name=queried_pokemon_name.name))

        except ValueError:
            q = q.strip().lower()
            return redirect(url_for('pokedox', pokemon_name=q))

    return abort(404)


@app.route('/delete_pokemon')
def delete_pokemon():
    # print("here")
    if request.method == "GET":
        pokemon_id = int(request.args.get("q").strip())

        # Delete from Pokemon table
        q_pokemon = models.Pokemon.query.filter(
            models.Pokemon.pokemon_id == pokemon_id).first()

        # If at least one query exits then it is possible to delete
        if q_pokemon is not None:
            name = q_pokemon.name

            # Delete from Type table
            for pokemon_type in q_pokemon.types.all():
                db.session.delete(pokemon_type)

            # Delete from Weakness Table
            for pokemon_weakness in q_pokemon.weaknesses.all():
                db.session.delete(pokemon_weakness)

            # Delete from  Pokemon table
            db.session.delete(q_pokemon)

            # Write changes to database
            db.session.commit()
            return render_template("success.html", name=name,
                                   operation="deleted")

        # Pokemon with requested id is not found
        return render_template("error.html",
                               message=f"Requested {pokemon_id} doesn't exist")

    return f"Request method {request.method} not allowed"


@app.route('/edit_pokemon', methods=["GET", "POST"])
def edit_pokemon():
    # Pass WTForm to edit template
    form = AddPokemonForm()
    pokemon_types = ["fire", "water", "grass", "eletric", "psychic", "steel",
                     "normal", "fairy", "dark", "flying",
                     "ghost", "poison", "ice", "ground", "rock", "dragon",
                     "fighting", "bug"]

    # If submitted form passes all the validation rules
    if form.validate_on_submit():
        """
                   Update edited Pokemon infos
        """
        pokemon_id = int(request.form.get("pokemon_id"))
        pokemon_name = request.form.get("name").strip().lower()
        q_pokemon = models.Pokemon.query.filter(
            models.Pokemon.pokemon_id == pokemon_id).first()

        q_pokemon.pokemon_id = pokemon_id
        q_pokemon.name = pokemon_name
        q_pokemon.description = request.form.get("description")
        q_pokemon.image_link = request.form.get("image_link")
        q_pokemon.height = request.form.get("height")
        q_pokemon.weight = request.form.get("weight")
        q_pokemon.category = request.form.get("category")
        q_pokemon.abilities = request.form.get("ability")

        """
            Update edited Pokemon type
        """
        q_pokemon_types = models.Type.query.filter(
            models.Type.pokemon_id == pokemon_id).all()
        for pokemon_type in q_pokemon_types:
            db.session.delete(pokemon_type)

        # Types of Pokemons
        for pokemon_type in pokemon_types:
            if request.form.get(f"t_{pokemon_type}") == "on":
                db.session.add(
                    models.Type(pokemon_id=pokemon_id, type=f"{pokemon_type}"))

        """
                Update edited Pokemon weakness
        """
        q_pokemon_weakness = models.Weakness.query.filter(
            models.Weakness.pokemon_id == pokemon_id).all()
        for pokemon_weakness in q_pokemon_weakness:
            db.session.delete(pokemon_weakness)

        # Weakness of Pokemons
        for pokemon_type in pokemon_types:
            if request.form.get(f"w_{pokemon_type}") == "on":
                db.session.add(models.Weakness(pokemon_id=pokemon_id,
                                               weakness=f"{pokemon_type}"))

        db.session.commit()
        return render_template("success.html", name=pokemon_name,
                               operation="updated")

    # When route edit_pokemon receives a query
    if request.method == "GET":
        pokemon_id = request.args.get("q")
        if pokemon_id is not None:

            """
                Fill basic pokemon info
            """
            pokemon_id = int(pokemon_id.strip())
            q_pokemon = models.Pokemon.query.filter(
                models.Pokemon.pokemon_id == pokemon_id).first()
            name = q_pokemon.name
            description = q_pokemon.description
            height = q_pokemon.height
            weight = q_pokemon.weight
            image_link = q_pokemon.image_link
            category = q_pokemon.category
            abilities = q_pokemon.abilities

            """
                Set button for queried pokemon type
            """
            queried_pk_types = models.Type.query.filter(
                models.Type.pokemon_id == pokemon_id).all()
            queried_pk_types = [pokemon_type.type for pokemon_type in
                                queried_pk_types]

            pk_type_flag = [0] * len(pokemon_types)

            for i, pokemon_type in enumerate(pokemon_types):
                if pokemon_type in queried_pk_types:
                    pk_type_flag[i] = 1

            """
                Set button for queried pokemon weaknesses
            """
            queried_pk_weaknesses = models.Weakness.query.filter(
                models.Weakness.pokemon_id == pokemon_id).all()
            queried_pk_weaknesses = [pokemon_type.weakness for pokemon_type in
                                     queried_pk_weaknesses]

            pk_weakness_flag = [0] * len(pokemon_types)

            for i, pokemon_type in enumerate(pokemon_types):
                if pokemon_type in queried_pk_weaknesses:
                    pk_weakness_flag[i] = 1

            return render_template("edit_pokemon.html", form=form, name=name,
                                   pokemon_id=pokemon_id, image_link=image_link,
                                   description=description, height=height,
                                   weight=weight, category=category,
                                   abilities=abilities,
                                   pk_type_flag=pk_type_flag,
                                   pk_weakness_flag=pk_weakness_flag,
                                   pokemon_types=pokemon_types)

        return render_template("error.html",
                               message=f"Requested {pokemon_id} doesn't exist")
    return f"Request method {request.method} not allowed"


@app.route('/add_pokemon', methods=["GET", "POST"])
def add_pokemon():
    form = AddPokemonForm()
    pokemon_types = ["fire", "water", "grass", "eletric", "psychic", "steel",
                     "normal", "fairy", "dark", "flying",
                     "ghost", "poison", "ice", "ground", "rock", "dragon",
                     "fighting", "bug"]

    if form.validate_on_submit():
        pokemon_id = request.form.get("pokemon_id")
        name = request.form.get("name")

        if pokemon_id is not None and name is not None:
            pokemon_id = int(pokemon_id.strip())
            name = name.strip().lower()
            image_link = request.form.get("image_link")
            description = request.form.get("description")
            height = request.form.get("height")
            weight = request.form.get("weight")
            category = request.form.get("category")
            ability = request.form.get("ability")

            pokemon = models.Pokemon(pokemon_id=pokemon_id,
                                     image_link=image_link, name=name,
                                     description=description, height=height,
                                     category=category, weight=weight,
                                     abilities=ability)
            db.session.add(pokemon)

            # Types of Pokemons
            for pokemon_type in pokemon_types:
                if request.form.get(f"t_{pokemon_type}") == "on":
                    db.session.add(models.Type(pokemon_id=pokemon_id,
                                               type=f"{pokemon_type}"))

            # Weakness of Pokemons
            for pokemon_type in pokemon_types:
                if request.form.get(f"w_{pokemon_type}") == "on":
                    db.session.add(models.Weakness(pokemon_id=pokemon_id,
                                                   weakness=f"{pokemon_type}"))

            db.session.commit()
            return render_template("success.html", name=name, operation="added")

        return render_template("error.html",
                               message=f"Requested {pokemon_id} doesn't exist")

    if request.method == "GET":
        return render_template("add_pokemon.html", form=form, pokemon_types=pokemon_types)
    return f"Request method {request.method} not allowed"


@app.route('/pokedox/<string:pokemon_name>')
def pokedox(pokemon_name):
    pokemon = models.Pokemon.query.filter(
        models.Pokemon.name == pokemon_name).first()
    if pokemon is not None:
        name = pokemon.name
        pokemon_id = pokemon.pokemon_id
        image_link = pokemon.image_link
        description = pokemon.description
        height = pokemon.height
        weight = pokemon.weight
        abilities = pokemon.abilities

        # Extract Pokemon type info
        pk_type = [pokemon_type.type for pokemon_type in pokemon.types.all()]

        # Extract Pokemon weakness info
        weakness = [pokemon_weakness.weakness for pokemon_weakness in
                    pokemon.weaknesses.all()]

        return render_template("detail.html", name=name, image_link=image_link,
                               description=description, height=height,
                               weight=weight, pk_type=pk_type,
                               abilities=abilities, weakness=weakness)

    return abort(404)
