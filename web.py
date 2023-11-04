import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name_,template_folder='template')

model = pickle.load(open(r"F:\Model_AIMl\id3_random_forest.pkl", 'rb'))


@app.route('/')
def home():
    return render_template('tennis.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)
    mapping = {'Outlook': {'Overcast': 0, 'Rain': 1, 'Sunny': 2},
               'Humidity': {'High': 0, 'Normal': 1},
               'Wind': {'Strong': 0, 'Weak': 1},
               'Play Tennis': {'No': 0, 'Yes': 1}}
    value = {i for i in mapping['Play Tennis'] if mapping['Play Tennis'][i] == prediction}
    value = str(value)
    return render_template('tennis.html', prediction_text='Will he go to play Tennis : {}'.format(value))


if __name__ == "__main__":
    app.run()