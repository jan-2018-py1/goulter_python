from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>/<myid>')
def show_user_profile(username,myid):
    print "*" * 80, username
    print "*" * 80, myid
    return render_template("index.html", user = username, id1 = myid)
app.run(debug=True)
