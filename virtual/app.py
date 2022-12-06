from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"
@app.route('/')
def index():
    title = "Extract keyword from email"
    return render_template('index.html', title=title)

@app.route('/result', methods=["POST"])
def getKeywords():
    content = request.form.get("email_content")
    newContent = "Extract keywords from the text: " + content
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= newContent,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )
    keywords = response.choices[0].text
    return render_template('result.html', content=content, response=keywords)