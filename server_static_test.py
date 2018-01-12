from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index_static_test.html")
app.run(debug=True) # run our server
