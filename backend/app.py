from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API en ligne !"})

if __name__ == '__main__':
    app.run(debug=True)

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
