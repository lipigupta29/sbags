from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():

    return render_template("index.html")

@app.route("/about")
def lipi():
    name = 'lipi'
    return render_template('about.html',name = name)
app.run(debug = False )

print("Hello world")
<<<<<<< Updated upstream
print("chchchchchchchc")
=======
print("KKK")
print("lakakalalakakala")
>>>>>>> Stashed changes
