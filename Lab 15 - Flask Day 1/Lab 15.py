from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '''
    <h1>Hello World!</h1>
    <p>Arsalaan Syed : wyd</p>
    '''


@app.route('/arsalaan')
def arsalaan():
    return render_template('template.html')


if __name__ == '__main__':
    app.run(debug=True)
