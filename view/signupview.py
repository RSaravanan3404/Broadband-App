from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess
from model.utilities import *


def signUp(useraccess: UserAccess) -> None:
    '''
    Checks if the person is new to the application and asking all the details and signs him/her in.
    '''
    email = input("Enter your email: ")
    while not check_mail(mail=email):
        system('cls')
        email = input("Enter a valid email id..")
    user = useraccess.isExist(email=email)

    if not user:
        name = input("Enter your name: ")
        dob = input("Enter you date of birth splitted by '/' DD/MM/YYYY: ")
        password = input("Set a strong password..")
        while not check_password(password=password):
            password = input("Enter a strong password: ")
        confirm_password = input("Confirm password: ")
        while password != confirm_password:
            confirm_password = input("Enter the correct password to confirm: ")
        if useraccess.signUp(email=email, name=name, dob=dob, password=password):
            system('cls')
            print("You're Signed In successfully..")
            return
    system('cls') 
    print("User with this email already exist enter the valid email id..")