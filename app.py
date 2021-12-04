from flask import Flask
from flask import request, jsonify
import os
from google.cloud import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'

DIALOGFLOW_PROJECT_ID = 'chatbot-j-xqv9'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'me'

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def root():
    return "Hello World"

@app.route('/api/getMessage', methods=['POST'])
def home():
    return ""


#def sendMessage(mobnum, message):


if __name__ == '__main__':
    app.run()