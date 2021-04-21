from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from random import choice

from stories import silly_story, excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


STORIES = [silly_story, excited_story]


@app.route('/')
def madlibs_form():
    """Return homepage"""

    return render_template(
        "questions.html",
        words=choice(STORIES).prompts,
        )

