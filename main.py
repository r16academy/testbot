from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return "<h1>Hello, APIs hit!</h1>"

if __name__ == '__main__':
    app.run(debug=True)