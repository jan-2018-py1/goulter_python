from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from datetime import datetime
import re
import md5
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'dbloginregistration')

# our index route will handle rendering our form

#1
@app.route('/')
def index():
  #session['date'] =  datetime.now().strftime("%m/%d/%Y")
  return render_template("registrationForm.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# WE ARE WAITING FOR A POST REQUEST
@app.route('/process', methods=['POST'])
def process():
  #do validation
  #setup the regex to check for just letters in the first and last names.
  ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')
  EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
  #some test values
  #A23456789
  #23456789A
  #ABCDEFGh9
  #9ABCDEFGh
  PW_U_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]*[A-Z]+[a-zA-Z0-9.+_-]*$')
  PW_NUM_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]*[0-9]+[a-zA-Z0-9.+_-]*$')
  BDAY_VALID_REGEX = re.compile(r'^[0-9]{2}\/{1}[0-9]{2}\/[0-9]{4}$')
  
  confPw = request.form['confpassword']
  query = "INSERT INTO tblusers (first_name, last_name, email, password, created_at, updated_at) VALUES (:fname, :lname, :email, :pw, NOW(), NOW())"
  
  # 1. First Name - letters only, at least 2 characters and that it was submitted
  # 2. Last Name - letters only, at least 2 characters and that it was submitted
  # 3. Email - Valid Email format, and that it was submitted
  # 4. Password - at least 8 characters, and that it was submitted
  # 5. Password Confirmation - matches password

  if not request.form['firstname'] or not request.form['lastname'] or not request.form['email'] or not request.form['password'] :
    flash(u"You have not entered all the required data",'flashErrorMessages')
    return redirect('/') 
  else:
    if len(request.form['firstname']) < 2 or len(request.form['lastname']) < 2 or len(request.form['firstname']) < 2:# or len(lname) < 1 or len (session['pw']) < 1 or len(confPw) < 1 :
      flash(u"1. ->First Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"2. ->Last Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"3. Email - Valid Email format, and that it was submitted",'flashErrorMessages')
      flash(u"4. Password - at least 8 characters, and that it was submitted",'flashErrorMessages')
      flash(u"5. Password Confirmation - matches password",'flashErrorMessages')
      return redirect('/') 
    elif not request.form['firstname'].isalpha() or not request.form['lastname'].isalpha() :
      flash(u"first and last name must contain only alpha letters",'flashErrorMessages')
      return redirect('/') 
    elif not EMAIL_REGEX.match(request.form['email']):
      flash(u"1. First Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"2. Last Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"3. -> Email - Valid Email format, and that it was submitted",'flashErrorMessages')
      flash(u"4. Password - at least 8 characters, and that it was submitted",'flashErrorMessages')
      flash(u"5. Password Confirmation - matches password",'flashErrorMessages')
      return redirect('/')
    elif len(request.form['password']) < 8:
      flash(u"1. First Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"2. Last Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"3. Email - Valid Email format, and that it was submitted",'flashErrorMessages')
      flash(u"4. --> Password - at least 8 characters, and that it was submitted",'flashErrorMessages')
      flash(u"5. Password Confirmation - matches password",'flashErrorMessages')
      return redirect('/')
    elif (request.form['password'] != request.form['confpassword']):
      flash(u"1. First Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"2. Last Name - letters only, at least 2 characters",'flashErrorMessages')
      flash(u"3. Email - Valid Email format, and that it was submitted",'flashErrorMessages')
      flash(u"4. Password - at least 8 characters, and that it was submitted",'flashErrorMessages')
      flash(u"5. --> Password Confirmation - matches password",'flashErrorMessages')
      return redirect('/')
    else:

      data = {
                'fname': request.form['firstname'],
                'lname': request.form['lastname'],
                'email': request.form['email'],
                'pw' : md5.new(request.form['password']).hexdigest()
            }
     
      new_user = mysql.query_db(query, data) #when there is an insert, we get back the id of the row inserted to.
      session['uid']=new_user #this means we have a logged in user.
      myUsers = mysql.query_db("SELECT * FROM tblusers")
      return redirect('/dashboard')

@app.route('/dashboard') # this is the success of a register!
def dashboard():
  query = "SELECT * FROM tblusers WHERE id = :user_id" #being able to show this dashboard means there is an active session, someone is logged in.
  data = {
          "user_id":session["uid"]
      }   
  user = mysql.query_db(query, data) #when there is a select, we get back a list of dictionaries converted from the rows of data selected.
  print user
  return render_template("dashboard.html", user = user[0]) 
  #when dashboard.html access user.first_name, it's from user.  
  #USER from mysql.query_db(query, data) IS an list of one dictionary. user[0] is a dictioary.
  #[{u'first_name': u'Tom', u'last_name': u'Jones', u'created_at': datetime.datetime(2018, 2, 1, 17, 48, 40), 
  # u'updated_at': datetime.datetime(2018, 2, 1, 17, 48,40), u'email': u'1@1.com', u'password': u'123456789H', u'id': 31L}]

@app.route("/login", methods=["POST"])
def login():
	query = "SELECT * FROM tblusers WHERE email = :post_email"
	data = {
		"post_email":request.form["email"]
	}
	user = mysql.query_db(query, data) # []
	print user

	

	if len(user) > 0:
		user = user[0]
		if user["password"] ==  md5.new(request.form['password']).hexdigest():
			session["uid"] = user["id"]
			return redirect("/dashboard")
	flash("Email and password not found")
	return redirect("/")

	# 	else:
	# 		flash("Incorrect Password")
	# 		return redirect("/")
	# else:
	# 	flash("No email found")
# 	return redirect("/")

#fresh login method one
# @app.route('/login', methods=['GET'])
# def login():
#   return  render_template('loginForm.html')

# ANOTHER WAY TO CHECK THE  LOGIN DATA
#  @app.route('/loginCheck', methods=['POST'])
# def loginCheck():
#   myemail = request.form['email']
#   mypassword = request.form['password']
#   users = mysql.query_db("SELECT * FROM tblusers")
#   for row in users:
#     if row['email'] == myemail and row['password'] == mypassword:
#       return render_template('loginSuccess.html')
#     else:
#       return redirect('/login')

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")
app.run(debug=True) # run our server

