from flask import Flask

app = Flask(__name__)

#error handling aka see cool flask debugging output + u dont have to restart yr server everytime
#start the server in 1 window, open another and edit yr code while its running
app.config["DEBUG"] = True

@app.route('/')

@app.route('/hello')
def hello():
    return 'Boring', 404

@app.route('/test/<query>')
def search(query):
    return query

#URLs are always converted to a string, use flask converters:
#the print value + 1 is printed in firebug
@app.route('/integer/<int:value>')
def int_type(value):
    print value + 1     
    return 'correct'

@app.route('/float/<float:value>')
def float_type(value):
    print value + 1
    return "correct"    

#the above response object(return 'Correct') actually returns a tuple with 3 values > (response, status, headers)
#the default is (response, 200 ok, content type= 'html/text') Check out Firebug to see it.

#Put your own status code
@app.route('/name/<name>')
def index(name):
    if name.lower() == "michael":
        return 'Hello, {}'.format(name), 200
    else:
        return 'Not Found', 404





if __name__=='__main__':
    app.run()
