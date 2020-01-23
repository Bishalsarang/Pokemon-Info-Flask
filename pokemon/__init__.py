from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '\x024\xe6\x98\x8cq\x06mh\x90(4\xe6\xf5\xe9\xd6\xe4\x8f\x86\x91\x1f\xc0\xee\xaf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Use sqlite://// for absolute path
# Use sqlite:/// for relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

# I moved the import here to prevent circular dependencies between models.py and server.py
# ./manage.py -> import models
# ./models.py -> from __main__ import db
import pokemon.models  # Module level not imported at top and unused skipcq: PYL-W0611, FLK-E402

# All the routes are moved to views.py
# ./manage.py -> import views
# ./models.py -> from __main__ import app, db
import pokemon.views  # Module level not imported at top and unused skipcq: PYL-W0611, FLK-E402