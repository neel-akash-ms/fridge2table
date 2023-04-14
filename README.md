# Fridge2Table

## Installation
### Project Setup
1. Clone the Repository
2. Install Python3
3. Go to Project Folder and run virtual env: `virtualenv .venv`, `source .venv/bin/activate`
4. Install Django in virtual env: `pip install --upgrade pip`, `pip install django`
5. Install Crispy forms - Bootstrap5: `pip install crispy-bootstrap5`
6. Follow the Database Setup Instruction
7. To create migrations: `python manage.py makemigrations`, `python manage.py migrate`
8. To make static files load, run : `python manage.py collectstatic`
9. To run the application: `python manage.py runserver`
### Postgresql Database Setup
1. Install Postgresql and setup your postgres user.
2. Run application pgAdmin
3. Create a Database : `fridge-2-table` under Databases
4. Enter all the DB Details in the `.env` file
5. If migrations give error, trying changing password in the .env file to the one that you set when you started the pgAdmin application.
### Deployment
1. Create an account on Heroku + github Student credits
2. Install Heroku CLI
3. Go to project directory in Terminal and use command `heroku login` and follow the steps as instructed
4. Use command `heroku create fridge2table` to create an app on Heroku
5. Add env variables to heroku using command: `heroku config:set env_variable_name=env_variable_value`
6. Run `git push heroku main` to push your code to heroku
7. Run `heroku python3 manage.py migrate` to set the db
8. Create a superuser using the command `heroku python3 manage.py createsuperuser` and follow the instructions on screen
9. To open the deployed app, run `heroku open` and it will open the deployed app in the default web browser
### Logging
1. To enable logging, uncomment the Logging code in env file and set DEBUG = True
2. To use logger to log details, add this lines to the top of your file:<br />
    `import logging`<br />
    `logger = logging.getLogger(__name__)`
3. To use it, write `logger.debug('Add what you want to print')`