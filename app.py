from flask import Flask, request, render_template

from openai import OpenAI
from markupsafe import Markup

openai_client = OpenAI()

app = Flask(__name__)

valid_languages = ['English', 'German']
valid_poets = ['Rainer Maria Rilke', 'Lord Byron', 'Elizabeth Bishop', 'Sophie Albrecht', 'William Blake']

@app.route('/', methods=['GET', 'POST'])
def index():
    poem = ""
    if request.method == 'POST':
        poet = request.form.get('poet')
        language = request.form.get('language')
        # Use OpenAI bindings to generate a poem
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You impersonate famous historic poets. I'll give you a prompt, and you'll write a poem of maximum eight lines in the style of that poet. Make sure not to mention the poet's name in your poem. Every poem you write should be winter-themed."},
                {"role": "user", "content": f"Write a poem in the style of {poet} in {language}."},
            ]
        )
        poem = response.choices[0].message.content
        poem = Markup(poem.replace('\n', '<br>'))
    return render_template('index.html', valid_languages=valid_languages, valid_poets=valid_poets, poem=poem)

if __name__ == '__main__':
    app.run(debug=True)
