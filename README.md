# Pokemon-Info-Flask- 
The purpose of this repository is to understand working of Flask and features like routing, template as well as understand using database by creating Pokedox that allows CRUD operations.

I've tried implementing a simple MVT architecture by separating components into following files:
- **models.py**: contains ORM for database schema
- **views.py:** contains application logic i.e the response the apps returns
- **./templates/**: contains Jinja html templates
- **forms.py**: contains wtforms

In addition to this, I've implemented **manage.py** file for common database migration commands and running server commands.
For database, I have used SQlite. Instead of using raw SQL queries I have chosen to use SQLAlchemy to understand ORM database model.

I've deployed the app on heroku. You can view the demo [here](https://flask-pokedox.herokuapp.com/)
## How to use:    
- Clone this  [repository](https://github.com/Bishalsarang/Pokemon-Info-Flask-)  
 - Install all the requirements  
`pip install -r requirement.txt`  
 - ##### DO this :If you want to start from fresh database delete **database.db** where db is the extension and start  type following commands on terminal<br>
    `python manage.py db init`  
    `python manage.py db migrate`  
    `python manage.py db upgrade`  
 - Run   
    `python manage.py run_server`

## Database Schema
![enter image description here](https://github.com/Bishalsarang/Pokemon-Info-Flask-/blob/master/assets/database%20schema.png)

## Screenshots
![enter image description here](https://github.com/Bishalsarang/Pokemon-Info-Flask-/blob/master/assets/sc.gif)
