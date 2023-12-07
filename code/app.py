from flask import Flask, render_template

# Creating a Flask instance
app = Flask(__name__)

# A decorator that tells Flask what URL should trigger the following function
# Here, the following function will be triggered when the user navigates to the route URL (/) of the application
@app.route('/')

# To run the following function, 'index.html' file should be in the \templates
def home():
    return render_template('index.html')

# Run the flask app in debug mode, shows detailed error messages, allows automatic reload when code is changed
if __name__ == '__main__':
    app.run(debug=True)