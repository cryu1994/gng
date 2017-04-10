from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "charles"
@app.route('/')
def index():
    
    if not "number" in session:
        session['number'] = random.randint(1,101)
        print session["number"]
        session['guessedNum'] = ''
        session["numberofguess"] = 0
    return render_template("index.html", number=session['number'], guessedNum = session["guessedNum"], numberofguess=session["numberofguess"])

@app.route('/guess', methods=['POST'])
def render():
    print("hello")
    
    guess = request.form['guess']
    session['numberofguess'] += 1

    if int(guess) > 100 or int(guess) < 0:
        session['guessedNum'] = "Please Enter a number between 1 and 100"

    elif int(guess) > int(session['number']):
        session['guessedNum'] = 'Too High!'

    elif int(guess) == int(session['number']):
        session['guessedNum'] = 'was the number!'
    
    elif int(guess) < int(session['number']):
        session["guessedNum"] = 'Too Low!'

    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
	# global first_visit
	# global numberToGuess
	del session['number']
	return redirect('/')

app.run(debug=True)