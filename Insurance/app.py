import numpy as np
import pickle
import math
from flask import Flask, request,jsonify,render_template

app = Flask(__name__,template_folder = "template",static_folder="staticFiles")  # assign flask
model = pickle.load(open('build.pkl','rb'))   # import module

@app.route('/')
def home():
    return render_template('index.html')  # read index.html file

@app.route('/predict',methods = ['POST']) # transfer data from html python / server

def predict():
    int_features = [int(x) for x in request.form.values()] # request for data values
    final_features = [np.array(int_features)]  # convert into array
    prediction = model.predict(final_features) # 
    return render_template('index.html',Prediction_text="The Insurance Price {}".format(np.exp(prediction)))

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port = 8080)