# Assignment: Ninja Gold
# Create a simple game to test your understanding of flask, 
# and implement the functionality below.

# For this assignment, you're going to create a mini-game that helps a ninja 
# make some money! 
# When you start the game, your ninja should have 0 gold. 
# The ninja can go to different places (farm, cave, house, casino) and earn different
#  amounts of gold. 
# 
# In the case of a casino, your ninja can earn or LOSE up to 50 golds. 
# 
# Your job is to create a web app that allows this ninja to earn gold 
# and to display past activities of this ninja.

# Guidelines
# Refer to the wireframe below.
# Have the four forms appear when the user goes to http://localhost:5000.

# For the farm, your form would look something like
# <form action="/process_money" method="post">
#   <input type="hidden" name="building" value="farm" />
#   <input type="submit" value="Find Gold!"/>
# </form>

# In other words, you want to include a hidden value in the form and have each 
# form submit the form information to /process_money.
# Have /process_money determine how much gold the user should have.
# You should only have 2 routes -- '/' and '/process_money' 
# (reset can be another route if you implement this feature).

# Please make sure that...
# 1 when you visit, "localhost:5000/" you are seeing the page we described above 
# (in other words, we don't want to have to go to "/gold/index" or other URL to see 
# this app).
# 2 the forms are sent to "/process_money" and not any other URL.
# 3 the activities are stored in the session. No need to store anything in the database. 

# In order to generate a random number you can use the "random" python module:

from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range

@app.route('/')
def index():
    
    if 'yourGold' in session.keys():
      print '******your gold******' , session['yourGold']
      print '******current win******' , session['currentWin']
      print '******current place******' , session['currentPlace']
      try: 
        print '******current history******' , session['history']
      except KeyError:
        session['history']=[]
      # del session['yourGold']
      # del session['currentWin']
      # del session['currentPlace']
      #session.pop('history')
      # del session['yourGold']
      # del session['currentWin']
      # del session['currentPlace']
      # del session['history']
      
      return render_template('index.html')
    else:
      print '************HERE**************'
      session['yourGold'] = 0
      session['currentWin'] = 0
      session['currentPlace'] = 'Glens House'
      tempStringList = ['The Game Started']
      session['history']=[]
      return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    try:
      tempStringList = session['history']
    except KeyError:
      tempStringList = []
    if request.form['building'] == 'farm':
      session['currentPlace'] = 'farm'
      session['currentWin'] = int(random.randrange(9, 21))
      session['yourGold'] += session['currentWin']
      tempStringList = 'You just won ' + str(session['currentWin'])
      session['history'].append(tempStringList)
      return redirect('/')
    elif request.form['building'] == 'cave':
      session['currentPlace'] = 'cave'
      session['currentWin'] = random.randrange(4, 11)
      session['yourGold'] += session['currentWin']
      tempStringList = 'You just won ' + str(session['currentWin'])
      session['history'].append(tempStringList)
      return redirect('/')
    elif request.form['building'] == 'house':
      session['currentPlace'] = 'house'
      session['currentWin'] = random.randrange(1, 6)
      session['yourGold'] += session['currentWin']
      tempStringList = 'You just won ' + str(session['currentWin'])
      session['history'].append(tempStringList)
      return redirect('/')
    else:
      session['currentPlace'] = 'casino'
      session['currentWin'] = random.randrange(-51, 51)
      session['yourGold'] += session['currentWin']
      return redirect('/')



@app.route('/doreset', methods=['POST'])
def doreset():
   session.pop('yourGold')
   session.pop('currentWin')
   session.pop('currentPlace')
   session.pop('history')
   return redirect('/')

app.run(debug=True) # run our server

