from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, How are you Engineer! Hope you are doing good."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
