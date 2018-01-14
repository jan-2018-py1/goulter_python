# Assignment: Great Number Game
# Create a site that when a user loads it creates a random number between 1-100 
# and stores the number in session. 

# Allow the user to guess at the number and 
# tell them when they are too high or too low. 

# If they guess the correct number tell them and offer to play again.
# In order to remove something from the session, you must "pop" it off of the session dictionary.

# Set session like so:
# session['someKey'] = 50
# # Remove something from session like so:
# session.pop('someKey')

# In order to generate a random number you can use the "random" python module:

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range

#We can simply check if the key exists, and if it doesn't, then generate it.
#If it does exist, do nothing.


# Programmatically: if 'answer' not in session: #generate key

@app.route('/')
def index():
  if 'answer' in session.keys():
    print session['answer']
    return render_template("index.html")
  else:
      session['answer'] = random.randrange(0, 101)
      print session['answer']
      return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
  session['guess'] = int(request.form['guess'])
  return redirect('/')

@app.route('/doreset', methods=['POST'])
def doreset():
   session.pop('answer')
   session.pop('guess')
   return redirect('/')

# All you really need to do is store the INT guess 
# (Note: important, because everything sent is actually a STRING) in session.



app.run(debug=True) # run our server

# However, there's one minor issue...
# Everytime you POST to your /process route, 
# it sends an internal GET request to your / method (that's what redirect does), 
# meaning that it regenerates your session['answer'] everytime you POST with the form.