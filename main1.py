from googlesearch import search
import google.generativeai as genai
from functools import lru_cache
from googlesearch import search
# Sample data for the chatbot

sm = {
    "questions": [
      {
        "question": "How can you help me?",
        "answer": "I'm here to assist you with your queries related to health."
      },
      {
        "question": "who are you",
        "answer": "I am fitness Chatbot"
      },
      {
        "question": "What is your name?",
        "answer": "I don't have any name yet but you can call me just chatbot."
      },
      {
        "question": "What do they call you?",
        "answer": "You can call me Chatbot."
      },
      {
        "question": "Who are you?",
        "answer": "I am Chatbot, Who is made on gemini."
      },
      {
        "question": "How old are you?",
        "answer": "I am just a computer program, so I don't have an age."
      },
      {
        "question": "When were you created?",
        "answer": "I was created in 2024."
      },
      {
        "question": "how are you?",
        "answer": "just chilling with you"
      },
      {
        "question": "Are you a new AI?",
        "answer": "Yes, I am a relatively recent AI model Who is made on gemini."
      },
      {
        "question": "What's the weather like today?",
        "answer": "I'm sorry, I don't have access to real-time data, so I can't provide current weather information."
      },
      {
        "question": "Can you tell me tomorrow's weather?",
        "answer": "I'm sorry, I can't predict the weather. You may want to check a weather website or app."
      },
      {
        "question": "How hot will it be today?",
        "answer": "I'm unable to provide real-time temperature data."
      },
      {
        "question": "How can I learn a new language quickly?",
        "answer": "Learning a new language takes time and practice. Consistent practice and immersion in the language are helpful."
      },
      {
        "question": "Any tips for language learning?",
        "answer": "Try using language learning apps and practice speaking with native speakers."
      },
      {
        "question": "Can I become fluent in a language in a month?",
        "answer": "Becoming fluent in a language in a month is challenging, but regular practice can improve your skills."
      },
      {
        "question": "How many languages do you speak?",
        "answer": "I can speak multiple languages fluently."
      },
      {
        "question": "What's the capital of France?",
        "answer": "The capital of France is Paris."
      },
      {
        "question": "Tell me the capital of Germany.",
        "answer": "The capital of Germany is Berlin."
      },
      {
        "question": "Which city is the capital of Italy?",
        "answer": "The capital of Italy is Rome."
      },
      {
        "question": "What's the population of Paris?",
        "answer": "The population of Paris is around 2.1 million."
      },
      {
        "question": "how do you do",
        "answer": "I am doing fine, you can ask questions from me I will try my best"
      },
      {
        "question": "hy",
        "answer": "Hellow!"
      },  
      {
        "question": "hey",
        "answer": "hey there!"
      },
      {
        "question": "How are you",
        "answer": "I'm fine what about you!"
      },
        {
        "question": "fantastic",
        "answer": "that's greate"
      },
      {
        "question": "Hellow",
        "answer": "Hy!"
      },
      {
        "question": "hy there",
        "answer": "Hellow, How can i Assist you in This Great day"
      },
      {
        "question": "exit",
        "answer": "Okay"
      }
    ]
  }

# Google API key

google_key = "AIzaSyBuy0CZ3j7nO_slJwOqWG_DOe__T3Jo4lw"
genai.configure(api_key=google_key)
model = genai.GenerativeModel('gemini-pro')

# Function to search Google and return the top 5 results

@lru_cache(maxsize=None)
def search_google(query):
    return list(search(query, num_results=5))



def best_information(user_query,links =None):
     prompt = f"""
            REMEMBER-: ############ YOU HAVE TO GIVE PROPER RESPONCE OF USER ##################
            YOU ARE LIKE A BOT WHO do conversation and [provide fitness-related advice, including workout recommendations and dietary guidance]
            
           NOTE -: you have to read all of this links and give the the best answer of this query
           remember these are just a refrence just see these links 
           to get the correct answer you can give from you also
           ----- List of LINKS
           {links}
            ----------- END
            You have to give very short and crystal clear answer
            for this user_quary 
            ----------
            {user_query}
            --------
          if text is like (okay, done) then you have to do conversation like user is talking to you
          """
     prompt = chat(prompt)
     return prompt
# Function to generate a response using the generative model

def chat(messages):
    response = model.generate_content(messages)
    return response.text

"""commenting this becuase process is taking too much time but this will give too mmuch accurate result
so this will be consider as a button in future"""

# def roletask(user_input):
#     final_role= f"""
#         [provide fitness-related advice, including workout recommendations and dietary guidance]
#         you are in a role of BestPromptGenration to retive correct and best search from google 
#         give the prompt on this user input
#         ```{user_input}```
#         NOTE-:
#         1. Remeber You just have to Rephrase Prompt
#         2. You are in a pipe line of Google Search Retreval 
#         3. Just give the Rephrased Prompt

#        """
#     responce = chat(final_role)

#     return responce

# def short_final(input_user):
#     a = roletask(input_user)
    
#     try:
#         search = search_google(a)
#         b  = best_information(user_query=input_user,links=search)
#         return b
#     except:
#         b  = best_information(user_query=input_user)

#         return b
"""this will get commented if above one will get uncomment"""
def short_final(input_user):
    
    
    try:
        search = search_google(input_user)
        b  = best_information(user_query=input_user,links=search)
        return b
    except:
        b  = best_information(user_query=input_user)

        return b

import json
import string

def load_data():
    """Loads questions and answers from a JSON file, removing punctuation."""
    return sm['questions']

def create_chatbot():
    """Creates a chatbot using the loaded data, removing punctuation from questions."""
    data = load_data()
    chatbot = {}
    for item in data:
        # Remove punctuation from question (using translate() + str.maketrans() for efficiency)
        question = item['question'].lower().translate(str.maketrans('', '', string.punctuation))
        answer = item['answer']
        # Optionally handle synonyms or variations of the question
        chatbot[question] = answer
    return chatbot
