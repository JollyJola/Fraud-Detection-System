import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home(): 
    return render_template("index.html")

@app.route('/transaction/')
def transaction(): 
    return render_template("transaction.html")

@app.route('/predict/', methods=['POST'])
def predict(): 
    # if request.method == 'POST':
    nameOrig = request.form.get("nameOrig")
    oldbalanceOrg = request.form.get("oldbalanceOrg")
    newbalanceOrig = request.form.get("newbalanceOrig")
    amount = request.form.get("amount")
    nameDest = request.form.get("nameDest")
    oldbalanceDest = request.form.get("oldbalanceDest")
    newbalanceDest = request.form.get("newbalanceDest")
    type = request.form.get("type")
    isFlaggedFraud = request.form.get("isFlaggedFraud")

    fields = np.array([type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest, isFlaggedFraud])
    fields2 = [float(x) for x in fields]
    fieldArray = [np.array(fields2)]

    prediction = model.predict(fieldArray)

    if prediction == 0:
        return(render_template('transaction.html', prediction_text= "This transaction is not fraudulent"))
    else: 
        return(render_template('transaction.html', prediction_text= "This transaction is fraudulent"))


if __name__ == "__main__":
    app.run()