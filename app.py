import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 讀取 Render 提供的 PORT，預設 5000
    app.run(host='0.0.0.0', port=port)
