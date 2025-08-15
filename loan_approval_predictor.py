from flask import Flask, request
import pickle


app= Flask(__name__)

@app.route(rule="/ping",methods=["GET"])
def pinger():
    return {'message': 'Everything is working!'}


@app.route(rule="/predict", methods=["POST"])
def prediction():
    loan_req = request.get_json()
    # Load your model and make a prediction
    # For example:
    # model = pickle.load(open("model.pkl", "rb"))
    # prediction = model.predict([data["feature1"], data["feature2"]])
    print(loan_req)
    if loan_req['Gender']=="Male":
        Gender=0
    else:
        Gender=1
    if loan_req['Married']=="Yes":
        Married=0
    else:
        Married=1
    Applicant_Income = loan_req['ApplicantIncome']
    Loan_Amount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']
    features = [[Gender, Married, Applicant_Income, Loan_Amount, Credit_History]]
    model = pickle.load(open("./classifier.pkl", "rb"))
    prediction = model.predict(features)
    print(prediction)
    if prediction == 1:
        return {'Loan Approval Status': 'Approved'}
    else: 
        return {'Loan Approval Status': 'Rejected'}

