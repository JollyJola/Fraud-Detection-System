import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home(): 
    return render_template("index.html")


@app.route('/detect', methods=['POST'])
def predict(): 
    fields = [float(x) for x in request.form.values()]
    fieldArray = [np.array(fields)]
    prediction = model.predict(fieldArray)

    if prediction == 0:
        return(render_template('/predict', prediction_text= "This transaction is not fraudulent"))
    else: 
        return(render_template('/predict', prediction_text= "This transaction is fraudulent"))

