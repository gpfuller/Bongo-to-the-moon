from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "yay secret"

@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)

    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')

@app.route('/number_guess', methods = ['POST'])
def guess():
    session["guess"] = int(request.form["guess"])
    return redirect ('/')

if __name__=="__main__":
    app.run(debug=True)