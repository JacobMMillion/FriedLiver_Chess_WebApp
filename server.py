from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import json

# score variables
score = 0
max_score = 14

app = Flask(__name__)
app.secret_key = 'secret'

# load JSON
with open('data/attacks.json') as f:
    ATTACKS = json.load(f)

# 1) Home / landing page
@app.route('/')
def index():
    # show current cumulative score
    return render_template(
      'index.html',
      score=score,
      max_score=max_score
    )

# 2) TESTING PAGE FOR CHESSBOARD
@app.route('/chessboard_testing')
def chessboard_testing():
    return render_template('chessboard_testing.html')

# 3) Fried Liver puzzles
@app.route('/fried_liver')
def fried_liver():
    session['fried_liver'] = datetime.now().isoformat()
    desc = ATTACKS['fried_liver']['description']
    return render_template('fried_liver.html', description = desc)

# 4) Traxler Counter Attack puzzles
@app.route('/traxler_counter')
def traxler_counter():
    session['traxler_counter'] = datetime.now().isoformat()
    desc = ATTACKS['traxler_counter']['description']
    return render_template('traxler_counter.html', description = desc)

# 5) Quiz
@app.route('/liver_quiz')
def liver_quiz():
    return render_template('liver_quiz.html', score=score)

# 5) Quiz
@app.route('/traxler_quiz')
def traxler_quiz():
    return render_template('traxler_quiz.html', score=score)

@app.route('/quiz_score')
def quiz_score():
    return render_template(
      'quiz_score.html',
      score=score,
      max_score=max_score
    )

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    global score, max_score
    score = data.get('score', 0)
    # if you want, also bump max_score here—or handle elsewhere
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)

#stuff to consider
# store quiz answers
# use json to represent chess puzzle (5 on spec hw10)
# do we have a quiz results page (6d on spec hw10)
# make button to advance to next page (7)
