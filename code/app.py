from flask import Flask, render_template, request
import spacy

# Creating a Flask instance
app = Flask(__name__)

# Load the small english language model from spacy
nlp = spacy.load('en_core_web_sm')

# Return the chatbot response
def chatbot_response(user_input):
    # Process the user input using spacy
    doc = nlp(user_input)

    # Check for named entity in user input
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            if ent.text == "Shreya":
                return f"Kusal: Hello Bubui! Ami tor bubui. Ki bommaishi?"
    return f"Kusal: I have received your message, will get back to you shortly..."

# A decorator that tells Flask what URL should trigger the following function
# Here, the following function will be triggered when the user navigates to the route URL (/) of the application
@app.route('/')

# To run the following function, 'index.html' file should be in the \templates
def home():
    return render_template('index.html')

# A decorator that tells to process the user input data, using spacy
@app.route('/chat', methods=['POST'])

# Function to process the user input data, submitted as an HTML form
def process():
    user_input = request.form['user_input']

    # Process the user input
    response = chatbot_response(user_input)

    # Process user_input using spacy
    # doc = nlp(user_input)

    # Extracting entities
    # entities = [ent.text for ent in doc.ents]

    # Return the output to the HTML file
    # return render_template('index.html', entities=entities)
    return {'user_input': user_input, 'chatbot_response': response}

# Run the flask app in debug mode, shows detailed error messages, allows automatic reload when code is changed
if __name__ == '__main__':
    app.run(debug=True)