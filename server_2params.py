from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("2paramindex.html", phrase="hello", times=5)
app.run(debug=True)