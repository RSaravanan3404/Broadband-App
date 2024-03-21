import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')

from model.users import User
from datetime import date


class Transactions(object): 

    _transactions: list[dict] = []

    def getTransactions(self) -> list[dict]:
        return Transactions._transactions
    

    def getTransactionDetails(self, user: User):
        table = []
        for transaction in Transactions._transactions:
            current_transaction = []
            for detail in transaction:
                current_transaction.append(transaction[detail])
            table.append(current_transaction)

        return table
    

    def addTransction(self, user: User, amount: int, type: str):
        Transactions._transactions.append({
            "User": user,
            "Date": date.today(),
            "Type": type,
            "Amount": amount
        })


    