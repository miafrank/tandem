# Guac is extra!
An application to find interesting recipes that are friendly to many dietary restrictions for the Tandem annual potluck. 

Many Tandemites love tacos̶ and the application is a solution for finding recipes for team members with dietary restrictions, 
such as those who eat Vegetarian, Vegan, Gluten-free, Dairy-free, Halal, Kosher, and those with nut allergies. 

# Setup
## System dependencies:
1. [Python 3 (MacOs setup)](https://docs.python-guide.org/starting/install3/osx/)
    1. Follow instructions under _"Doing It Right"_ to install Python 3 if you do not have Python >= 3.7 installed 

## Project Setup
1. Set up virtual environment using [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/basics.html) in project directory: 
    1. `$ pip install pipenv`
    1. `$ pipenv install`
    1. `$ pipenv shell`

## Start the app with auto reload
```
$ python api.py
```

## Testing the API In Postman
1. Included in the repo is a `.postman_collection.json` file that can be opened in [Postman](https://www.postman.com/). 
To import the file into Postman
    1. `Import` > `Upload Files` > Select the file `Guac Is Extra.postman_collection.json`
    2. Once the server is running, you will be able to hit the endpoints in the collection!
 
## Run Tests
1. `$ python -m unittest discover`

## API Endpoints
|request name  |  request value  |
:-------:|:-------:
|get recipe by name   | _GET/recipes/{recipe or food name}_
|get recipe by ingredients        | _GET/recipes/{recipe or food name}/ingredients/{ingredients, another}_
|get recipe by dietary restrictions    | _GET/recipes/{recipe or food name}/diet/{diet}_