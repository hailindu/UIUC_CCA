from flask import Flask, request

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value
    data = request.get_json()
    seed_value = data['num']
    return 'MP2 Success', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
