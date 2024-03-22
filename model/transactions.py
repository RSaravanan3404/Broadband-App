import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')

from model.users import User
from datetime import date


class Transactions(object): 

    _transactions: list[dict] = []

    def getTransactions(self) -> list[dict]:
        return Transactions._transactions
    

    def getTransactionDetails(self, user: User) -> list[list]:
        table = []
        for transaction in Transactions._transactions:
            if transaction.get("User") == user:
                name = transaction.get("User").name
                date = transaction.get("Date")
                type = transaction.get("Type")
                amount = transaction.get("Amount")
                table.append([name, date, type, amount])

        return table
    

    def addTransction(self, user: User, amount: int, type: str) -> None:
        Transactions._transactions.append({
            "User": user,
            "Date": date.today(),
            "Type": type,
            "Amount": amount
        })


    