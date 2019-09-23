# Analytic-Model-Deployment

In this repositories, we want to test the model deployment of Credit Scoring using Random Forest Classifier Algorithm. In this case, there was a data of customer that ever take a credit scoring from A company. Then, we have to make model to test the new customer will get the credit from A company or not. 

We need to use PythonAnywhere.com and Postman to run this model and to test the model. But, in this model deployment, because the server is online. So this model can be test in another computer by using API. 

1. First step, we need to make a model by using Random Forest Algorithm using Python3 Language. It can be made using Jupyter notebook, google collabs, kaggle or you can use python anywhere. Then after the model was built, we need to do Serialization (change the model to pkl). You can see the code for making the model in 'modelnew.py' file. But if you only need the pkl files, you can donwload 'modelnew.pkl'.

2. Next after the model was build, we need to make a code to run a model so it can be connected to online platform. For the code of building a server, you can see in 'server.py'. Or you can placed in on flask if you use a PythonAnywhere.com to run a code (you can see the code of flask in 'flask_app.py'.

3. Next, you need to open website in PythonAnywhere.com that can be added the API so it can be connected. In this case, you can use my address to check if this model is work or not. In webapps on PythonEverywhere, you need to reload the web before testing it on Postman. You can used putrisqiana.pythonanywhere.com/api as my web and added the input data to be testing in PostMan, Body then Raw. This is the example of the output that you can input in postman.
Ex : 
-[{"BILL_AMT3":23881.0,"LIMIT_BAL":300000.0,"AGE":40},
- {"BILL_AMT3":4328.0,"LIMIT_BAL":350000.0,"AGE":55},
- {"BILL_AMT3":53415.0,"LIMIT_BAL":400000.0,"AGE":54},
- {"BILL_AMT3":17203.0,"LIMIT_BAL":200000.0,"AGE":41},
- {"BILL_AMT3":2500.0,"LIMIT_BAL":350000.0,"AGE":56},
- {"BILL_AMT3":79384.0,"LIMIT_BAL":380000.0,"AGE":36},
- {"BILL_AMT3":2758.0,"LIMIT_BAL":340000.0,"AGE":56},
- {"BILL_AMT3":76304.0,"LIMIT_BAL":430000.0,"AGE":61},
- {"BILL_AMT3":49764.0,"LIMIT_BAL":410000.0,"AGE":36},
- {"BILL_AMT3":91815.0,"LIMIT_BAL":330000.0,"AGE":63}]

I used 3 feature to check the credit scoring of the customer. There was Bill Amount 3, Limit Ballance and Age. 
- Bill Amount 3 is the amount of the third month of customer credit that can be used as the variable to credit scoring, because the amount of this last month can be affected to how the customer pay the credit in the next month.
- Limit Ballance is the amount of maximum ballance that customer can get from A company for their credit. It can be affected because the amount of the credit can affect the customer to pay.
- Age is the last variable that can be affected to this credit scoring because age can make a different behaviour by the old or young the customer is. 

Then the output in body output will be 
- [
-     "Customer can get the credit",
-     "Customer cant get the credit",
-     "Customer cant get the credit",
-     "Customer can get the credit",
-     "Customer cant get the credit",
-     "Customer can get the credit",
-     "Customer cant get the credit",
-     "Customer cant get the credit",
-     "Customer can get the credit",
-     "Customer cant get the credit"
- ]

By It result we can see that who is the customer that can get the credit or not. 
"Customer can get the credit" is the result of customer who can take the credit by A company.
"Customer cant get the credit" is the result of customer who cant take the credit by A company.

Notes : 
- flask-salary-predictor
This is project predicts the salary of the employee based on the experience.
- Model
model.py trains and saves the model to the disk.
-Server
server.py contains all the requiered for flask and to manage APIs.
-Request
request.py contains the python code to process POST request to server.

