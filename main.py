from flask import Flask
from random import choice

app = Flask("Ciao guys")

lista_fatti = [
    "Il miele non scade mai.",
    "Le banane sono bacche, mentre le fragole no.",
    "I polpi hanno tre cuori.",
    "La Grande Muraglia Cinese non è visibile dallo spazio."
]
coin = ["heads", "tails"]

@app.route("/")
def home():
    return '<p>benvenuto <a href= "/fatto_casuale">Scopri un fatto casuale </a> </p>'

@app.route("/fatto_casuale")
def fatto_casuale():
    return  f'<p>{choice(lista_fatti)}</p>'

@app.route("/secret")
def coin():
    return f"<p>{choice(coin)}</p>"

app.run(debug=True)
