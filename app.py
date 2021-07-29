from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route("/")
def home():
    return"Hello! this is the main page<h1>WELCOME<h1>"

@app.route("/<name>")#whatever I'll type,it grabs the value and passes to the function as parameter
def user(name):
    return f"hello{name}!"  

@app.route("/admin")
def admin():
     return redirect(url_for("home"))

if __name__ =="__main__":
    app.run()