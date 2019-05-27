import predict
import train as t
import status as stat

from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"status": "ok"})

@app.route('/submit')
@stat.check_status
def submit():
    predict.predict_and_submit()

@app.route('/train')
@stat.check_status
def train():
    t.train()
        

if __name__ == "__main__":
    stat.set_ready()
    # app.run(host='0.0.0.0', debug = True) #, threaded=False, processes=1)
    app.run(host='0.0.0.0', debug = True, threaded=True, processes=1)