# Pokemon-Info-Flask- 
The purpose of this repository is to understand working of Flask and features like routing, template as well as understand using database by creating Pokedox that allows CRUD operations.<br><br>
    I've tried implementing a simple MVT architecture by separating components into following files:<br>
            - **models.py**: contains ORM for database schema<br>
            - **views.py**: contains application logic i.e the response the apps returns<br>
            - **./templates/**: contains Jinja html templates<br>
    In addition to this, I've   implemented **manage.py** file for common database migration commands and running server commands.<br>
For database, I have used SQlite. Instead of using raw SQL queries  I have chosen to use SQLAlchemy to understand ORM database model.    
    
    
    
## How to use:    
- Clone this  [repository](https://github.com/sarangbishal/Pokemon-Info-Flask-)  
 - Install all the requirements  
`pip install -r requirement.txt`  
 - Open terminal in current directory and make database schema by migrations command  
`python manage.py db init`  
`python manage.py db migrate`  
`python manage.py db upgrade`  
 - Run   
 `python manage.py run_server`

## Database Schema
![enter image description here](https://github.com/sarangbishal/Pokemon-Info-Flask-/blob/master/assets/database%20schema.png)

## Screenshots
![enter image description here](https://github.com/sarangbishal/Pokemon-Info-Flask-/blob/master/assets/sc.gif)