from flask import Flask

app = Flask(__name__)


app.config['DEBUG'] = True

@app.route('/hello/<veggie>')
def hello(veggie):
    if veggie.lower() == 'carrot':
        return 'I love {}s'.format(veggie, 200)
    else:
        return 'Not found', 404

    @app.route('/number/<int:value>')
    def number(value):
        print value + 1
        return 'yeah'


if __name__=='__main__':
    app.run()
