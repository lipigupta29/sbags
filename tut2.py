from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():


    return render_template("index.html")

@app.route("/about")
def lipi():
    name = 'lipi'
    return render_template('about.html',name = name)
app.run(debug = True )

@app.route("/bootstarp")
def bootstarp():

    return render_template('bootstrap.html')

app.run(debug = True )




