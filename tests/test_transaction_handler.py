import json
from src.handlers.transaction_handler import lambda_handler

def test_lambda_handler():
    event = {
        'transactions': [
            {
                'id': '1',
                'amount': 100.0,
                'timestamp': '2023-01-01T00:00:00Z',
                'type': 'deposit'
            }
        ]
    }
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert response['body'] == 'Transactions processed successfully'