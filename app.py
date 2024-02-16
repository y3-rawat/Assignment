# Importing necessary modules
from flask import Flask, render_template, request
import main1 as main1
import string 
from difflib import SequenceMatcher

# Creating a Flask app instance
app = Flask(__name__)
first_time = True
def get_response(chatbot, user_input):
    global first_time
    """Returns the response from the chatbot based on the user's input."""
    user_input = user_input.lower().translate(str.maketrans('', '', string.punctuation))
    max_similarity = 0
    best_match = None
    for question in chatbot:
        similarity = SequenceMatcher(None, user_input, question).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = question
    if max_similarity >= 0.7:
        return chatbot[best_match]
    else:
        if first_time:
            first_time = False
            response = main1.short_final(user_input)
            return response
        else:
            return main1.chat(user_input)


# Defining the route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# Defining the route for getting bot response

@app.route("/get")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    chatbot = main1.create_chatbot()
    if userText in chatbot:
        response = chatbot[userText]
        return response
    else:
        
        try:
            response = get_response(chatbot, userText)
            return response
        except Exception as e:
            try:
                response = get_response(chatbot, userText)
                return response
            except:
                try:
                    response = get_response(chatbot, userText)
                    return response
                except:
                    return f"An error occurred: {str(e)}  Trying again"


