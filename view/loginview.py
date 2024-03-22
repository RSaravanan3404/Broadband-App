from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess
from view.plansview import planAccess
from view.profile import profileAccess
from view.feedbacksview import feedbackAccess
from getpass import getpass


def logIn(useraccess: UserAccess):
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
                profileAccess(status=profile, useraccess=useraccess)
            elif plans:
                planAccess(status=plans, useraccess=useraccess)
            elif feedback:
                feedbackAccess(status=feedback, useraccess=useraccess)
            
            choice = input("Do you want to log out(Yes/No): ").capitalize()
            if choice == "Yes":
                isLogged = False
            system('cls')
            