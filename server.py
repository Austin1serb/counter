from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'asd123' # set a secret key for security purposes

@app.route('/')
def index():
    if 'number' in session:
        session['number'] += 1
    else:
        session['number'] = 0

    return render_template("index.html")
     

@app.route('/click')
def index1():
    session['number'] += 1
    return redirect("/")


@app.route('/reset')
def index2():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5003)
