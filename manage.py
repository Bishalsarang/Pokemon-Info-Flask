# Author: Bishal Sarang
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.secret_key = '\x024\xe6\x98\x8cq\x06mh\x90(4\xe6\xf5\xe9\xd6\xe4\x8f\x86\x91\x1f\xc0\xee\xaf'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Use sqlite://// for absolute path
# Use sqlite:/// for relative path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# I moved the import here to prevent circular dependencies between models.py and server.py
# ./manage.py -> import models
# ./models.py -> from __main__ import db

import models  # Module level not imported at top and unused skipcq: PYL-W0611, FLK-E402

# All the routes are moved to views.py
# ./manage.py -> import views
# ./models.py -> from __main__ import app, db
import views  # Module level not imported at top and unused skipcq: PYL-W0611, FLK-E402

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def run_server():
    """
     To run the server:
        $ python manage.py run_server
    """
    app.run()


if __name__ == "__main__":
    ###################################
    # Commands for database migrations:
    # $ python manage.py run_server
    # $ python manage.py db init
    # $ python manage.py db migrate
    # $ python manage.py db upgrade
    ###################################
    manager.run()
