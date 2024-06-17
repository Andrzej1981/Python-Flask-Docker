from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/app')
def aplikacja():
    return '<h1>Aplikacja internetowa!</h1>'

if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=False,port=4080)