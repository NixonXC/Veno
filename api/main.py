from flask import Flask, jsonify, render_template, send_from_directory
import random
import json
import os

app = Flask(__name__)

with open("data/questions.json") as q:
    questions = json.load(q)

with open("data/quotes.json", "r") as qo:
    quotes = json.load(qo)

with open("data/facts.json", "r") as f:
    facts = json.load(f)

with open("data/roasts.json") as r:
    roasts = json.load(r)

with open("data/darkjokes.json", "r") as re:
    darkjokes = json.load(re)

with open("data/recommendations.json", "r") as g:
    recommendations = json.load(g)

with open("data/jokes.json", "r", encoding='utf-8') as j:
    jokes = json.load(j)

with open("data/programjokes.json") as pj:
    pjokes = json.load(pj)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/playground')
def playground():
    return render_template("playground.html")

@app.route('/api/version')
def version():
    return jsonify({
        'version' : '1.0.0',
        'Last Updated' : '4 May 2023 '
    })

@app.route('/api/darkjoke')
def darkjoke():
    random_joke = random.choice(darkjokes["jokes"])
    return jsonify({'buildup': random_joke['buildup'], 'punchline': random_joke['punchline'], 'id': random_joke['id']})

@app.route('/api/devjoke')
def devjoke():
    random_devjoke = random.choice(pjokes["programjokes"])
    return jsonify({'buildup': random_devjoke['setup'], 'punchline': random_devjoke['punchline'], 'id': random_devjoke['id']})

@app.route('/api/joke')
def joke():
    random_joke = random.choice(jokes["jokes"])
    return jsonify({'buildup': random_joke['buildup'], 'punchline': random_joke['punchline'], 'id': random_joke['id']})

@app.route('/api/recommendation')
def recommendation():
    random_recommendation = random.choice(recommendations["recommendations"])
    return jsonify({'song': random_recommendation['song'], 'genre': random_recommendation['genre'], 'artist': random_recommendation['artist'], 'id': random_recommendation['id']})

@app.route('/api/question')
def question():
    random_que = random.choice(questions["questions"])
    return jsonify({'question': random_que['question'], 'id': random_que['id']})

@app.route('/api/fact')
def fact():
    random_fact = random.choice(facts["facts"])
    return jsonify({'fact': random_fact['fact'], 'id': random_fact['id']})

@app.route('/api/quote')
def quote():
    random_quote = random.choice(quotes["quotes"])
    return jsonify({'quote': random_quote['quote'], 'author' : random_quote['author'], 'id': f"{random_quote['id']}"})

@app.route('/api/roast/<username>')
def roast(username):
    random_roast = random.choice(roasts["roasts"])
    return jsonify({
        'roast': f"{username}, {random_roast['roast']}",
        'target': username,
        'id' : random_roast['id']
    })

if __name__ == '__main__':
    app.run(debug=True)
