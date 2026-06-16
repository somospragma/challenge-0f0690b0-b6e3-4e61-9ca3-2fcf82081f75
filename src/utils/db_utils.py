import boto3
from src.models.transaction_model import Transaction

class DynamoDBUtil:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('Transactions')

    def save_transaction(self, transaction: Transaction):
        self.table.put_item(
            Item={
                'id': transaction.id,
                'amount': transaction.amount,
                'timestamp': transaction.timestamp,
                'type': transaction.type
            }
        )