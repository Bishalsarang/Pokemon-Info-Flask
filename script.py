from server import db, Pokemon, Type, Weakness

db.create_all()
pokemon1 = Pokemon(pokemon_id=1, image_link="https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png",
                   name="bulbasaur",
                   description="Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger.",
                   height="2'04''", category="seed", weight="15.2lbs", abilities="overgrow")

type1 = Type(pokemon_id=1, type="grass")
type2 = Type(pokemon_id=1, type="poison")

weakness1 = Weakness(pokemon_id=1, weakness="fire")
weakness2 = Weakness(pokemon_id=1, weakness="flying")
weakness3 = Weakness(pokemon_id=1, weakness="ice")
weakness4 = Weakness(pokemon_id=1, weakness="psychic")
db.session.add(pokemon1)
db.session.add(type1)
db.session.add(type2)
db.session.add(weakness1)
db.session.add(weakness2)
db.session.add(weakness3)
db.session.add(weakness4)
db.session.commit()
