
from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        result = a + b
        return f'The Result: {result}'
    else:
        return 'Error: Please provide value for the parameters "a" and "b".'

if __name__ == '__main__':
    app.run(debug=True)

