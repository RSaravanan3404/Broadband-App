from os import system
import sys
sys.path.insert(0, 'C:/Users/srgee/Questions/mr.cooper Broadband service-app')
from controller.usercontroll import UserAccess
from getpass import getpass


def profileAccess(status: bool, useraccess: UserAccess):
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
                system('cls')
                print("Modifications have been added.")

        case "3":
            status = False
        case _:
            print("Invalid operation.")

    if status:
        profileAccess(status=status, useraccess=useraccess)