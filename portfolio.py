# Assignment: Portfolio
# Build a server document that can handle 3 different route requests.

# Root
# Root will always be the first page your user will see. If you remember,
# root is located at "/". This simply means that when a user sends a 
# request to your website's url, without adding anything after the trailing slash, 
# they will send a request to "/". This time, have your root route display a template
#  with a message welcoming users to your portfolio.

# Projects
# If a user adds /projects to your website's url 
# (in this case localhost:5000, display an HTML page with a list of 
# the projects you've done.

# About 
# If a user sends a request to /about display a template with a 
# short paragraph about yourself.

from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def welcome():
  #return 'Hello World!'  # Return the string 'Hello World!' as a response.
  return render_template('welcome.html')    # Render the template and return it!

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.run(debug=True)      # Run the app in debug mode.
