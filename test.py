from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'A New! Index Page'

if __name__ == '__main__':
    app.run(port=8080)