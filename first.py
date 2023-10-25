# Import the Flask library
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle requests to that route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask app on the local development server
if __name__ == '__main__':
    app.run(debug=True)
