from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Prosta aplikacja DevOps</h1><p>Witaj w mojej aplikacji napisanej we Flask!</p>"

@app.route('/hello/<name>')
def hello(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return f"<h1>Otrzymano dane: {request.form['data']}</h1>"
    return '''
        <form method="post">
            <input name="data" placeholder="Wpisz coś">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
