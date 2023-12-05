from flask import Flask, request, render_template

from openai import OpenAI
from markupsafe import Markup

openai_client = OpenAI()

app = Flask(__name__)

valid_languages = ['English', 'German']
valid_poets = ['Rainer Maria Rilke', 'Lord Byron', 'Elizabeth Bishop', 'Sophie Albrecht', 'William Blake']



if __name__ == '__main__':
    app.run(debug=True)
