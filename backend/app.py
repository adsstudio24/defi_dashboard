import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/defi')
def get_defi_data():
    response = requests.get("https://api.llama.fi/protocols").json()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
