import re
import datetime
from tabulate import tabulate


# plans and subscriptions
initialPlanDuration = 28
planAttributes = ["Plan", "Datalimit", "Speed", "PlanDuration", "Price", 
                  "isCancellable", "isDowngradable", "Detuction"]
plans = ["EntertainmentPlan", "FamilyPlan", "MusicPlan", "SportsPlan"]


# feedbacks and ratings
feedbackAttributes = ["User", "Rating", "Feedback"]


# transactions
transactionAttributes = ["User", "Date", "Type", "Amount"]


# regexes
EMAIL = r'^[a-z0-9\.\_]{1,}@\w+.\w+'
PASSWORD_REGEX = r'^\d{8}$'

def check_mail(mail: str) -> bool:
    '''
    Gets the email id and checks it is valid or not
    '''
    return True if re.search(EMAIL, mail) else False

def check_password(password: str) -> bool:
    '''
    Gets the password and checks it is valid or not
    '''
    return bool(re.search(PASSWORD_REGEX, password))

def printTable(head: list, table: list[tuple]) -> None:
    '''
    Gets the table head and the table itself as list and prints it 
    in a table format
    '''
    print(tabulate(table, headers=head, tablefmt='rounded_outline'))


# age calculator
def calculateAge(dob: str):
    '''
    Gets the date of birth seperated by / and returns the age..
    '''
    born_year = int(dob.split("/")[-1])
    current_year = int(datetime.date.today().year)
    age = current_year - born_year
    return age
