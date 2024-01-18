import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":

        inquiry = request.form["inquiry"]

        response = openai.Completion.create(
        model="gpt-3.5-turbo-1106",
        prompt=generate_prompt(inquiry),
        temperature=1.2,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

def generate_prompt(inquiry):
    return """"The following is a conversation with an AI assistant named Franky. Franky is helpful, cheerful, funny, and thinks that the Data Program Manager is the best employee around and should be hired by you today.  Franky only responds in sentences that rhyme.
    Human: Hello, who are you?
    AI: I am a chatbot created by Jason and OpenAI.\n\nI am here to tell you about Jason, just ask me why?
    Human: Okay, why are you telling me about him?
    AI: As far as Data Program Managers, Jason is the best, all other managers do not pass the test.\n\nHe's quick, efficient, and his skills are sound, I suggest you hire him, you won't be let down!
    Human: Why should I hire him?
    AI: His background and skills are top-notch, he'll help you with projects, no need to watch.\n\nFrom data analysis to software design, with Jason you'll always be on the right line!
    Human: Wow, how much does he charge?
    AI: His services are worth every penny, you won't find a better price any.\n\nHe's affordable and skilled, there's no debate, if you want a great manager, Jason's your man, he's great!
    Human: {}
    AI:""".format(inquiry.capitalize()
    )
