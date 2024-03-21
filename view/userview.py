from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess
from getpass import getpass
from utilities import *


useraccess = UserAccess()

# Profile and Accessess
def profileAccess(status: bool):
    choice = input("1.View profile\n2.Edit profile\n3.Exit\nEnter your choice: ")
    match choice:
        case "1":
            useraccess.viewProfile()
        case "2":
            # edit profile..
            useraccess.viewProfile()
            choice = input("What do you want to edit(1.Name/2.Date of birth/3.password): ")
            name, dob, password = None, None, None
            match choice:
                case "1":
                    name = input("Enter your new name: ")
                case "2":
                    dob = input("Enter the correct date of birth splitted by '/' DD/MM/YYYY: ")
                case "3":
                    email = input("Enter your email id: ")
                    user = useraccess.isExist(email=email)
                    if user:
                        password = getpass(prompt="Password: ")
                        if useraccess.logIn(user=user, password=password):
                            password = input("Enter the new password: ")
                case _:
                    print("Invalid operation..")
            changes = {"name": name,
                    "dob": dob,
                    "password": password
                    }
            if useraccess.editProfile(changes):
                print("Modifications have been added.")

        case "3":
            status = False
        case _:
            print("Invalid operation.")

    if status:
        profileAccess(status=status)


# Plans and Accessess
def planAccess(status: bool):
    choice = input("1.View All plans\n2.View current plans\n3.Upgrade plan\n\
                   4.Downgrade plan\n5.Cancel plan\n6.View Transactions\n7.Exit\nEnter your choice: ")
    match choice:
        case "1":
            system('cls')
            useraccess.viewAllPlans()

        case "2":
            system('cls')
            useraccess.viewCurrentPlan()
            
        case "3":
            system('cls')
            useraccess.viewCurrentPlan()
            upgradeDuration = input("Enter the number of months You need to upgrade(1 month validity is 28 days. ) Enter only months: ")
            useraccess.upgradePlan(duration=upgradeDuration)

        case "3":
            system('cls')
            useraccess.viewCurrentPlan()
            downgradeDuration = input("Enter the number of months You need to downgrade(1 month validity is 28 days. ) Enter only months: ")
            refund = useraccess.downgradePlan(duration=downgradeDuration)
            if refund:
                print(f"{refund} rupees refunded")

        case "5":
            system('cls')
            useraccess.viewCurrentPlan()
            refund = useraccess.cancelPlan()
            if refund:
                print(f"{refund} rupees refunded")

        case "6":
            system('cls')
            useraccess.viewTransactions()
        
        case "7":
            status = False

        case _:
            system('cls')
            print("Invalid operation.")

    if status:
        planAccess(status=status)


def feedbackAccess(status: bool):
    choice = input("1.View All feedbacks\n2.View Your feedbacks\n3.Leave feedback\nEnter your choice: ")
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


# Log In
def logIn():
    email = input("Enter your email: ")
    user = useraccess.isExist(email=email)
    if user:
        password = getpass(prompt="Password: ")
        isLogged = useraccess.logIn(user=user, password=password)
        if isLogged:
            system('cls')
            print("You're logged in successfully..")
        while isLogged:
            # view profile..
            response = input("1.Profile\n2.Plans\n3.Feedbacks\n4.Exit\nEnter your choice: ")
            profile = False
            plans = False
            feedback = False
            match response:
                case "1":
                    profile = True
                case "2":
                    plans = True
                case "3":
                    feedback = True
                case _:
                    pass

            if profile:
                profileAccess(status=profile)
            elif plans:
                planAccess(status=plans)
            elif feedback:
                pass # call feedback function..
            
            choice = input("Do you want to log out(Yes/No): ").capitalize()
            if choice == "Yes":
                isLogged = False
            system('cls')


# Sign Up
def signUp():
    email = input("Enter your email: ")
    while not check_mail(mail=email):
        system('cls')
        email = input("Enter a valid email id..")
    user = useraccess.isExist(email=email)

    if not user:
        name = input("Enter your name: ")
        dob = input("Enter you date of birth splitted by '/' DD/MM/YYYY: ")
        password = input("Set a strong password..")
        confirm_password = input("Confirm password: ")
        while password != confirm_password:
            confirm_password = input("Enter the correct password to confirm: ")
        if useraccess.signUp(email=email, name=name, dob=dob, password=password):
            system('cls')
            print("You're Signed In successfully..")
            return
    system('cls') 
    print("User with this email already exist enter the valid email id..")


# Main View
def view(choice=None):
    choice = input("1.Log In\n2.Sign Up\n3.Exit\nEnter your choice: ")
    match choice:
        case "1":
            logIn()
        case "2":
            signUp()
        case "3":
            pass
        case _:
            print("Invalid Operation..")

    choice = input("do you want to LogIn(Yes or No): ").capitalize()
    if choice == "Yes":
        logIn()
    

view()