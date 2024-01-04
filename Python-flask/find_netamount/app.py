from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def net_amount():
    try:
        data = request.get_json()
        net_amount = data.get('net_amount')
        mode = data.get('mode')
        amount = data.get('amount')

        if mode == 'deposit':
            net_amount += amount
        elif mode == 'withdraw':
            net_amount -= amount
        else:
            return jsonify(error='Invalid input...use deposit or withdraw')

        return jsonify(f'The current balance amount is {net_amount}')

    except Exception as e:
        return jsonify(error=f'Error processing the request: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
