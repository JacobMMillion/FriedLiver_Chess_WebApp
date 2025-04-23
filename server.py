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

# Get the players score dynamically
def get_score_and_max():
    liver_seq   = ATTACKS["fried_liver"]["whiteSeq"]
    traxler_seq = ATTACKS["traxler_counter"]["blackSeq"]

    # max is just total moves
    max_score = len(liver_seq) + len(traxler_seq)

    # pull what the user actually tried
    fm_liver   = session.get("first_moves_fried_liver", [])
    fm_traxler = session.get("first_moves_traxler", [])

    # count how many match the expected
    score_liver = sum(
        1 for i, exp in enumerate(liver_seq)
        if i < len(fm_liver) and fm_liver[i] == exp
    )
    score_traxler = sum(
        1 for i, exp in enumerate(traxler_seq)
        if i < len(fm_traxler) and fm_traxler[i] == exp
    )

    return score_liver + score_traxler, max_score

# 1) Home / landing page
@app.route('/')
def index():
    score, max_score = get_score_and_max()
    return render_template('index.html',
                           score=score,
                           max_score=max_score)

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

@app.route('/liver_quiz')
def liver_quiz():
    return render_template(
        'liver_quiz.html',
        quiz_type='fried_liver',
        score=score,
        liver_whiteSeq=ATTACKS["fried_liver"]["whiteSeq"],
        liver_blackSeq=ATTACKS["fried_liver"]["blackSeq"]
    )

@app.route('/traxler_quiz')
def traxler_quiz():
    return render_template(
        'traxler_quiz.html',
        quiz_type='traxler',
        score=score,
        traxler_whiteSeq=ATTACKS["traxler_counter"]["whiteSeq"],
        traxler_blackSeq=ATTACKS["traxler_counter"]["blackSeq"]
    )

@app.route('/quiz_score')
def quiz_score():
    score, max_score = get_score_and_max()
    return render_template('quiz_score.html',
                           score=score,
                           max_score=max_score)

@app.route('/submit_move', methods=['POST'])
def submit_move():
    data = request.get_json()
    quiz = data.get('quiz')
    idx  = data.get('index')
    san  = data.get('san')

    key = f"first_moves_{quiz}"
    moves = session.get(key, [])

    # grow list if needed
    if len(moves) <= idx:
        moves += [None] * (idx + 1 - len(moves))

    moves[idx] = san
    session[key] = moves

    print("== submit_move ==")
    print(" Fried Liver moves:", session.get('first_moves_fried_liver'))
    print("      Traxler moves:", session.get('first_moves_traxler'))

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)

#stuff to consider
# store quiz answers
# use json to represent chess puzzle (5 on spec hw10)
# do we have a quiz results page (6d on spec hw10)
# make button to advance to next page (7)
