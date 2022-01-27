from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def main():
    """ Returns 'welcome' """
    return "welcome"

@app.route('/welcome/home')
def home():  
    """ Returns 'welcome home' """
    return "welcome home"

@app.route('/welcome/back')
def back():  
    """ Returns 'welcome back' """
    return "welcome back"
