# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request, render_template,jsonify
import json
import joblib
import numpy as np


# Flask constructor takes the name of
# current module (__name__) as argument.

app = Flask(__name__)
transformer = joblib.load('heartdisease.pkl')



# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


@app.route("/",methods=['GET',"POST"])
def home():
    return render_template("index.html")


@app.route("/predict",methods=['POST'])
def main():
    print("1:", [X for X in request.form.values()])
    print("2:", [type(X) for X in request.form.values()])
    int_features = [float(X) for X in request.form.values()]
    final_features = [np.array(int_features)]
    print("Final_features: ", final_features)
    prediction = transformer.predict(final_features).tolist()
    print("prediction: ", prediction)
    output = round(prediction[0],2)
    print("output: ", output)
    return render_template("index.html", prediction_text = 'HEART DISEASE PREDICTION is: {}'.format(output))
   


if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port = 8000)





