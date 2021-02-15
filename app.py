from flask import flask
import random

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def  favorite_dessert(users_dessert):
    """Displays a message to the user that changes based on their favorite dessert."""
    return f'Wow, {users_dessert} is my favorite dessert, too!'

@app.route('/madlibs/<adjective>/<noun>')
def madLibs(adjective, noun):
    """Displays a funny (but appropriate) string!"""
    return f"I think this game is {adjective}, but my teacher is {noun}"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    """Multiplies number 1 by number 2"""
    if number1.isdigit() & number2.isdigit() == True:
        return number1 * number2
    else:
        return "Invalid inputs, please input two numbers"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    """Prints out a word a certain number of times"""
    i = 0
    while i < n:
        print(word)
        i++


@app.route('/dicegame/')
def dicegame():
    """Returns a number between one and 6. If the user rolls a 6, they win
    otherwise they lose"""
    diceRoll = randint(1,6):
        if diceRoll == 6:
            return f"You rolled a {diceRoll}, you won!"
        else:
            return f"You rolled a {diceRoll}, you lost."
if __name__ == '__main__':
    app.run(debug=True)