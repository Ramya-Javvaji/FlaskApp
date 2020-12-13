from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key = b'RamyaSree'


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('test.html')


@app.route('/myform')
def my_form():
    return render_template('myform.html')


@app.route('/myform', methods=['POST'])
def my_form_post():
    text = request.form['text']
    session['text'] = text
    return redirect(url_for('skill'))


@app.route("/skill")
def skill():
    text = session.get('text')
    return render_template('testskill.html', name=text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
