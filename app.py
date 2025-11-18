from flask import Flask
import main

app = Flask(__name__)

@app.route('/')
def home():
    return "Web App"

@app.route('/run')
def run_program():
    return main.run_tab_text()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')