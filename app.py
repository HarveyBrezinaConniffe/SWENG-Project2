# imports
from Calculator import calculate
from flask import Flask, render_template, request


# create app object
app = Flask(__name__)


# define calculator
# query handling flow

# home page
@app.route('/')
def home():
    return render_template('index.html')


# calculation page
@app.route('/calculate', methods=['POST'])
def ans():
    eq = request.form['eq']
    result = calculate(eq)

    return render_template('index.html', answer=str(result))


if __name__ == "__main__":
    app.run(debug=True)
