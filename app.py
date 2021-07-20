from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/album')
def album():
    return render_template("album.html")

@app.route('/formulario')
def formulario():
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)