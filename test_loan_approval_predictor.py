import pytest
from loan_approval_predictor import app

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.get_json() == {'message': 'Naveen is working!'}
    
def test_prediction_approved(client):
    test_data = {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome": 50000,
    "LoanAmount": 500,
    "Credit_History": 1.0
}
    resp = client.post('/predict', json=test_data)
    assert resp.status_code == 200
    assert resp.get_json() == {'Loan Approval Status': 'Approved'}
    