from flask import Flask
from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017/')
db = client.mildy

app = Flask(__name__)

@app.route('/')
def hello_world():
    print(db.command("serverStatus"))
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0')