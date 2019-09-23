
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Flask!'

app = Flask(__name__)

# Load the model
model = pickle.load(open('/home/putrisqiana/mysite/modelnew.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    datas = request.get_json(force=True)
    output=[]
    for data in datas:
    # Make prediction using model loaded from disk as per the data.
        prediction = model.predict(np.array([[data['BILL_AMT3'], data['LIMIT_BAL'], data['AGE']]]))

    # Take the first value of prediction
    #output = int(prediction[0])
        if prediction==0:
            output.append('Customer can get the credit')
        else:
            output.append('Customer cant get the credit')

    return jsonify(output)