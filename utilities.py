import re
import datetime
from tabulate import tabulate

# plans and subscriptions
initialPlanDuration = 28
planAttributes = ["Plan", "Datalimit", "Speed", "PlanDuration", "Price", 
                  "isCancellable", "isDowngradable", "Detuction"]


# feedbacks and ratings
feedbackAttributes = ["User", "Rating", "Feedback"]


# transactions
transactionAttributes = ["User", "Date", "Type", "Amount"]

EMAIL = r'^[a-z0-9\.\_]{1,}@\w+.\w+'
PASSWORD_REGEX = r'^\d{8}$'

def check_mail(mail: str) -> bool:
    return True if re.search(EMAIL, mail) else False


def check_password(password: str) -> bool:
    return bool(re.search(PASSWORD_REGEX, password))


def printTable(head: list, table: list[tuple]) -> None:
    print(tabulate(table, headers=head, tablefmt='rounded_outline'))


def isTrue(attribute):
    if attribute:
        return "Yes"
    return "No"


def jsonParser(json: dict):
    keys, values = [], []
    for key, value in json.items():
        keys.append(key)
        values.append(value)
    return keys, values


def calculateAge(dob: str):
    born_year = int(dob.split("/")[-1])
    current_year = int(datetime.date.today().year)
    age = current_year - born_year
    return age