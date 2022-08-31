#import libraries
import numpy as np
from joblib import load
from flask import Flask, request, jsonify, render_template
#import pickle

#Initialize the flask App
app = Flask(__name__)
#model = pickle.load(open('Hours_trending_US.pkl', 'rb'))
model = load("Hours_trending_US.joblib")
model2 = load("views_US.joblib")


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    print(request.form)
    print("snuffaluffagus")
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    print('heffalumps')
    print(int_features)
    final_features = [np.array(int_features)]
    print("woozles")
    print(final_features)
    print("THIS IS SO FUCKING CLOSE TO WORKING")
    prediction = model.predict(final_features)
    print(prediction)

    output = round(prediction[0], 2) 

    return render_template('index.html', prediction_text='Approximate days until video trends: {:.2f}'.format(output/24))
    #return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict2',methods=['POST'])
def predict2():
    print(request.form)
    print("snuffaluffagus")
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    print('heffalumps')
    print(int_features)
    final_features = [np.array(int_features)]
    print("woozles")
    print(final_features)
    print("THIS IS SO FUCKING CLOSE TO WORKING")
    prediction2 = model2.predict(final_features)
    print(prediction2)

    output = round(prediction2[0], 2) 

    return render_template('index.html', prediction_text2='Predicted views until: {:.0f}'.format(output))
    #return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5501, debug=True)

    
