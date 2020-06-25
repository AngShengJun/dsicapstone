# Import Libraries
from flask import Flask, jsonify, request, flash
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
from flask import render_template
import Requiredfn

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

model = pickle.load(open("finalized_model.sav", "rb"))
cv = pickle.load(open("finalized_cv.sav", "rb"))

# root end point
@app.route('/predict_class', methods = ["GET", "POST"])
def landing():

    output = None

    if request.method == "POST":
        text = request.form["motive"]
        text2 = Requiredfn.selftext_to_words2(text)
        tokens = cv.transform(text2)
        result = model.predict(tokens)
        if result[0] == 1:
            output = 'bombing attack'
        elif result[0] == 0:
            output = 'non-bombing attack'
    
    return render_template("index.html", output = output)

    
    