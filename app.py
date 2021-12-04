from flask import Flask
from flask import request, jsonify
import os
from google.cloud import dialogflow
from google.api_core.exceptions import InvalidArgument
import requests
from werkzeug.datastructures import LanguageAccept

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
    # Main Code
    message = request.form.get('Body')
    mobnum = request.form.get('From')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(
        text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(
            session=session, query_input=query_input)
    except InvalidArgument:
        raise


# def sendMessage(mobnum, message):


if __name__ == '__main__':
    app.run()
