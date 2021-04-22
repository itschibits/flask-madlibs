from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from random import choice

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


STORIES = [silly_story, excited_story]
# random_story = None

@app.route('/')
def show_form():
    """shows a madlib form"""
    # random_story = choice(STORIES)
    return render_template(
        "questions.html",
        prompts=excited_story.prompts
        )


@app.route('/results')
def show_story():
    """Takes in answers from form and generates a madlibs story """
    answers = request.args
    text = excited_story.generate(answers)
    print('this is our answers ', answers)

    return render_template('story.html', story=text)
    