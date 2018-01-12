from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

# WE ARE WAITING FOR A POST REQUEST
@app.route('/users', methods=['POST'])

def create_user():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   email = request.form['email']
   # redirects back to the '/' route
  
   return redirect('/')


# experiment
# def create_user():
#    print "Got Post Info"
#    # we'll talk about the following two lines after we learn a little more
#    # about forms
#    name = request.form['name']
#    email = request.form['email']
#    # Here's the line that changed. We're rendering a template from a post route now.
#    return render_template('about.html')
app.run(debug=True) # run our server
