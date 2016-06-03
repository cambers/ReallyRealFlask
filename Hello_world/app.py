from flask import Flask

app = Flask(__name__)

#error handling
app.config['DEBUG'] = True


@app.route('/')

@app.route('/hello')
def hello_world():
    return 'hello world!!!!!!!!'

@app.route('/test/<search_query>')
def test(search_query):
    return 'This is your {}'.format(search_query)

@app.route('/integer/<int:value>')
def integer(value):
    print value + 1
    return 'Correct'

@app.route('/float/<float:value>')
def float(value):
    print value + 1
    return 'Awesome'

@app.route('/path/<path:value>')
def path(value):
    print value
    return 'correct'

@app.route('/name/<name>')
def index(name):
    if name.lower() == 'michael':
        return 'Hello {}'.format(name), 200
    else:
        return 'Not Found', 404



if __name__=="__main__":
    app.run()


