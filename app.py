from flask import Flask, render_template
from config import config
from test.test_mongodb import insert as mongo_insert

app = Flask(__name__)
app.config.from_object(config)

@app.route('/temp')
def temp():
    user = {'username': 'Alice', 'age': 25}
    return render_template('temp.html', user=user)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mongo')
def mongo():
    mongo_insert()
    return 'success'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)
