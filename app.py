import predict
import train as t

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"status": "ok"})

@app.route('/submit')
def submit():
    predict.predict_and_submit()
    return jsonify({"status": "ok"})


@app.route('/train')
def train():
    t.train()
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True, threaded=False, processes=1)