from flask import Flask, render_template

app = Flask(__name__)

# 1) Home / landing page
@app.route('/')
def index():
    return render_template('index.html')

# 2) TESTING PAGE FOR CHESSBOARD
@app.route('/chessboard_testing')
def chessboard_testing():
    return render_template('chessboard_testing.html')

# 3) Fried Liver puzzles
@app.route('/fried_liver')
def fried_liver():
    return render_template('fried_liver.html')

# 4) Traxler Counter Attack puzzles
@app.route('/traxler_counter')
def traxler_counter():
    return render_template('traxler_counter.html')

# 5) Quiz
@app.route('/liver_quiz')
def liver_quiz():
    return render_template('liver_quiz.html')

# 5) Quiz
@app.route('/traxler_quiz')
def traxler_quiz():
    return render_template('traxler_quiz.html')

if __name__ == '__main__':
    app.run(debug=True)