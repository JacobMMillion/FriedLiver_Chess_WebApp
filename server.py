from flask import Flask, render_template

app = Flask(__name__)

@app.route('/chessboard_testing')
def chessboard_testing():
    return render_template('chessboard_testing.html')

if __name__ == '__main__':
    app.run(debug=True)