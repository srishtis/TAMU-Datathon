import numpy as np
from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import load_model_single_prediction

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    test_string = request.form['test_string']
    test_string = str(test_string)
    print(type(test_string))
    load_model_single_prediction.single_predict(test_string)

if __name__ == "__main__":
    app.run(debug=True)