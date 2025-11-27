from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    {"text": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"text": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
    {"text": "In the end, we will remember not the words of our enemies, but the silence of our friends.", "author": "Martin Luther King Jr."},
    {"text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"text": "What we think, we become.", "author": "Buddha"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "The journey of a thousand miles begins with one step.", "author": "Lao Tzu"},
    {"text": "Success is not how high you have climbed, but how you make a positive difference to the world.", "author": "Roy T. Bennett"},
    {"text": "It always seems impossible until it’s done.", "author": "Nelson Mandela"},
    {"text": "The mind is everything. What you think you become.", "author": "Buddha"},
    {"text": "Everything you’ve ever wanted is on the other side of fear.", "author": "George Addair"},
    {"text": "Happiness is not something ready-made. It comes from your own actions.", "author": "Dalai Lama"},
    {"text": "Don’t watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"text": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
    {"text": "Whether you think you can or think you can’t, you’re right.", "author": "Henry Ford"},
    {"text": "Be yourself; everyone else is already taken.", "author": "Oscar Wilde"},
    {"text": "Turn your wounds into wisdom.", "author": "Oprah Winfrey"},
    {"text": "Act as if what you do makes a difference. It does.", "author": "William James"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
