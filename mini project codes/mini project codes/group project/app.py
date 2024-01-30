import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle. load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/check')
def check():
    return render_template('check.html')
@app.route('/result', methods=['GET', 'POST'])
def predictions():
    if request.method == 'POST':
        Sex = request. form[ 'Sex' ]
        name = request.form['name']
        HighBP = request.form['HighBP']
        Highchol = request.form['Highchol']
        Age = request. form["Age"]
        BMI = request.form['BMI']
        Smoker = request. form['Smoker']
        Stroke = request.form['Stroke']
        HvyAlcoholConsump = request.form['HvyAlcoholConsump']
        DiffWalk = request.form['DiffWalk']
        HeartDiseaseorAttack = request.form['HeartDiseaseorAttack']
        PhysActivity = request.form['PhysActivity']
        NoDocbcCost = request. form['NoDocbcCost']
        GenHlth = request. form['GenHlth']
        MentHIth = request.form['MentHIth']
        PhysHlth = request. form[ 'PhysHlth']
        Education = request.form['Education']
        Income = request.form['Income'] 
        
        input_data = [HighBP, Age, Highchol, BMI, Smoker, Stroke, HvyAlcoholConsump, DiffWalk,
HeartDiseaseorAttack, PhysActivity, NoDocbcCost, GenHlth, MentHIth, PhysHlth, Education, Income]
        print(input_data)
        input_data_as_nparray = np.asarray(input_data)
        input_data_reshaped = input_data_as_nparray.reshape(1, -1)
        prediction = model.predict(input_data_reshaped)
        print(prediction)
        if (prediction == 0):
            return render_template('result.html', result='Not having Diabetes', name=name, Sex=Sex)
        elif (prediction == 1):
            return render_template('result.html', result='Pre-Diabetes', name=name, Sex=Sex)
        else:
            return render_template('result.html', result='Having Diabetes', name=name, Sex=Sex)
    return render_template('check.html')

if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)