from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello():
    return "Dynamic data from the back-end!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)