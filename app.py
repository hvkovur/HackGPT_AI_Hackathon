from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders the index.html in the templates folder

if __name__ == '__main__':
    app.run(debug=True)
