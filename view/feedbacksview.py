from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess


def feedbackAccess(status: bool, useraccess: UserAccess):
    choice = input("1.View All feedbacks\n2.View Your feedbacks\n3.Leave feedback\n4.Exit\nEnter your choice: ")
    match choice:
        case "1":
            system('cls')
            useraccess.viewAllFeedbacks()
        case "2":
            system('cls')
            useraccess.viewYourFeedback()
        case "3":
            system('cls')
            rating = int(input("Enter your rating out of 5: "))
            feedback = input("Leave your feedback here: ")
            useraccess.leaveFeedback(rating=rating, feedback=feedback)
        case _:
            status = False
    if status:
        feedbackAccess(status=status, useraccess=useraccess)
        