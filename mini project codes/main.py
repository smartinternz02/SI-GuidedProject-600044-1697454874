import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('templates/model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return predict_diabetes(request.form)
    return render_template('index.html')

@app.route('/check')
def check():
    return render_template('check.html')

def predict_diabetes(form_data):
    # Ensure all the expected fields are present in the form data
    required_fields = ['HighBP', 'Age', 'Highchol', 'BMI', 'Smoker', 'Stroke',
                       'HvyAlcoholConsump', 'DiffWalk', 'HeartDiseaseorAttack',
                       'PhysActivity', 'NoDocbcCost', 'GenHlth', 'MentHIth', 'PhysHlth',
                       'Education', 'Income']

    if not all(field in form_data for field in required_fields):
        return render_template('check.html', error='Missing fields in the form')

    input_data = [float(form_data[field]) for field in required_fields]
    input_data_as_nparray = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data_as_nparray)

    if prediction == 0:
        result = 'Not having Diabetes'
    elif prediction == 1:
        result = 'Pre-Diabetes'
    else:
        result = 'Having Diabetes'

    name = form_data.get('name', '')
    sex = form_data.get('Sex', '')

    return render_template('result.html', result=result, name=name, Sex=sex)

if __name__ == '__main':
    app.run(debug=True)
