from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)




@app.route("/")
def hello():
    return """
    <a href='/skill'> skill </a>"""


@app.route("/skill")
def skill():
    return render_template('portfolio.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
